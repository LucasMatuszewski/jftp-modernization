package com.myjavaworld.jftp;

import java.io.File;
import java.awt.Rectangle;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.ResourceBundle;

import javax.help.HelpSet;

import com.myjavaworld.ftp.FTPConstants;
import junit.framework.TestCase;

/** Child JVM used so legacy static home snapshots never touch a real profile. */
public final class StartupStateProbe extends TestCase {
    public static void main(String[] args) throws Exception {
        File home = new File(System.getProperty("user.home")).getCanonicalFile();
        File temporary = new File(System.getProperty("java.io.tmpdir")).getCanonicalFile();
        if (home.equals(temporary) || !home.toPath().startsWith(temporary.toPath())) {
            throw new IllegalArgumentException("This fixture requires an isolated home below java.io.tmpdir");
        }
        String operation = args[0];
        if ("desktop-seed".equals(operation)) {
            Path files = Files.createDirectories(home.toPath().resolve("files"));
            Files.write(files.resolve("hello.txt"), "synthetic JFTP startup fixture".getBytes("UTF-8"));
            JFTPPreferences prefs = JFTP.loadPreferences();
            prefs.setLocale(Locale.ENGLISH);
            prefs.setCheckForUpdates(false);
            prefs.setLocalDirectory(files.toString());
            prefs.setWindowBounds(new Rectangle(80, 80, 1280, 800));
            JFTP.savePreferences(prefs);
        } else if ("resources".equals(operation)) {
            for (Locale locale : new Locale[] { Locale.ENGLISH, Locale.GERMAN,
                    Locale.TRADITIONAL_CHINESE }) {
                ResourceBundle bundle = ResourceBundle.getBundle("com.myjavaworld.jftp.JFTP", locale);
                if (!Locale.ENGLISH.equals(locale)) {
                    assertEquals(locale, bundle.getLocale());
                }
                assertTrue(bundle.getString("text.notConnected").length() > 0);
            }
            assertTrue(JFTPUtil.getIcon("jftp16.gif").getIconWidth() > 0);
            ClassLoader loader = StartupStateProbe.class.getClassLoader();
            assertNotNull(HelpSet.findHelpSet(loader, "helpset/helpSet", ".xml", Locale.ENGLISH));
            assertNotNull(Class.forName(RemoteHost.DEFAULT_FTP_CLIENT_CLASS_NAME));
            assertNotNull(Class.forName(RemoteHost.DEFAULT_LIST_PARSER_CLASS_NAME));
        } else if ("defaults".equals(operation)) {
            JFTPPreferences prefs = JFTP.loadPreferences();
            assertTrue(prefs.isPassive());
            assertFalse(prefs.isUseProxy());
            assertEquals(FTPConstants.TYPE_BINARY, prefs.getDefaultTransferType());
            assertEquals(Integer.valueOf(FTPConstants.TYPE_ASCII), prefs.getTransferTypes().get("TXT"));
            assertTrue(FavoritesManager.getFavorites().isEmpty());
        } else if ("write".equals(operation)) {
            JFTPPreferences prefs = JFTP.loadPreferences();
            prefs.setLocale(Locale.GERMAN);
            prefs.setPassive(false);
            prefs.setCheckForUpdates(false);
            prefs.setLocalDirectory(new File(System.getProperty("user.home"), "files").getAbsolutePath());
            JFTP.savePreferences(prefs);
            RemoteHost favorite = new RemoteHost("Synthetic favorite", "127.0.0.1", 2121,
                    "synthetic-user", "synthetic-password", "synthetic-account");
            favorite.setInitialRemoteDirectory("/fixtures");
            FavoritesManager.saveFavorites(Collections.singletonList(favorite));
        } else if ("read".equals(operation)) {
            JFTPPreferences prefs = JFTP.loadPreferences();
            assertEquals(Locale.GERMAN, prefs.getLocale());
            assertFalse(prefs.isPassive());
            assertFalse(prefs.getCheckForUpdates());
            assertEquals(new File(System.getProperty("user.home"), "files").getAbsolutePath(),
                    prefs.getLocalDirectory());
            List favorites = FavoritesManager.getFavorites();
            assertEquals(1, favorites.size());
            RemoteHost favorite = (RemoteHost) favorites.get(0);
            assertEquals("Synthetic favorite", favorite.getName());
            assertEquals("127.0.0.1", favorite.getHostName());
            assertEquals(2121, favorite.getPort());
            assertEquals("synthetic-user", favorite.getUser());
            assertEquals("synthetic-password", favorite.getPassword());
            assertEquals("synthetic-account", favorite.getAccount());
            assertEquals("/fixtures", favorite.getInitialRemoteDirectory());
        } else {
            throw new IllegalArgumentException(operation);
        }
        System.out.println("STARTUP-STATE-PROBE " + operation + " OK");
    }
}
