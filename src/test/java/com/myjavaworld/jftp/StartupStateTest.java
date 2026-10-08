package com.myjavaworld.jftp;

import java.io.File;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Comparator;
import java.util.concurrent.TimeUnit;

import junit.framework.TestCase;

/** Basic startup-state characterization; each probe starts with an isolated home. */
public class StartupStateTest extends TestCase {
    private Path home;

    protected void setUp() throws Exception {
        home = Files.createTempDirectory("jftp-state-test-");
    }

    protected void tearDown() throws Exception {
        try (java.util.stream.Stream<Path> paths = Files.walk(home)) {
            Path[] entries = paths.sorted(Comparator.reverseOrder()).toArray(Path[]::new);
            for (Path entry : entries) {
                Files.delete(entry);
            }
        }
    }

    public void testFirstStartCreatesReadableDefaults() throws Exception {
        probe("defaults");
        assertTrue(Files.size(home.resolve(".jftp/data/preferences.ser")) > 0);
    }

    public void testSettingsAndFavoritesSurviveAnotherJvm() throws Exception {
        probe("write");
        probe("read");
    }

    public void testStartupResourcesAreOnClasspath() throws Exception {
        probe("resources");
    }

    private void probe(String operation) throws Exception {
        File java = new File(System.getProperty("java.home"), "bin/java.exe");
        if (!java.isFile()) {
            java = new File(System.getProperty("java.home"), "bin/java");
        }
        Path log = home.resolve(operation + ".log");
        Process process = new ProcessBuilder(java.getAbsolutePath(),
                "-Duser.home=" + home.toAbsolutePath(), "-Djava.awt.headless=true",
                "-cp", System.getProperty("surefire.test.class.path",
                        System.getProperty("java.class.path")),
                StartupStateProbe.class.getName(), operation)
                .redirectErrorStream(true).redirectOutput(log.toFile()).start();
        try {
            assertTrue("Probe timed out: " + operation, process.waitFor(30, TimeUnit.SECONDS));
            String output = new String(Files.readAllBytes(log), StandardCharsets.UTF_8);
            assertEquals(output, 0, process.exitValue());
        } finally {
            if (process.isAlive()) {
                process.destroyForcibly();
                process.waitFor(5, TimeUnit.SECONDS);
            }
        }
    }
}
