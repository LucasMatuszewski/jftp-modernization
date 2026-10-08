# Repository map export

- Implementation: rust
- Examined source: "/home/lucas/.cache/legacy-map-review-20261007/flask"
- Examined revision: "2c1b30d0503cfb064f1cb252e6614a06915a362a"; dirty working copy: False
- Candidates seen: 26
- Files selected / parsed: 26 / 24
- Definitions found / selected: 502 / 502
- Captured definitions omitted: 0
- Selection mode / rendering: ranked / grouped
- Declaration snippets clipped: 0
- Map budget: 16384 estimated tokens
- Truncated: no; exclusions, unsupported files and parse failures still limit coverage
- Skipped entries / parse failures: 0 / 0
- Original generation wall time: 0.106947 seconds (measured subprocess wall time)
- Raw content: 56011 Unicode characters, 56011 UTF-8 bytes, approximately 14003 tokens
- Whole annotated report: approximately 14356 tokens
- Token estimator: ceil(Unicode characters / 4); a size estimate, not a model tokenizer
- Raw map SHA-256: 06658c9ac954abbc3e888cde0bd3ba6e4147f685d7fdf64a14c12724f475a7d5
- Evidence sidecars: "sidecars/flask-python.rust/flask-python.rust.raw.md", "sidecars/flask-python.rust/flask-python.rust.meta.json", "sidecars/flask-python.rust/flask-python.rust.inventory.json"

Generation status `complete` means the selected map was published, not that every repository file or relationship was analyzed. Read the sidecars for scope, skips, parser failures and the original working-copy fingerprint.

---

# Repository map

## src/flask/__init__.py

```text
L47:     def __getattr__(name: str) -> t.Any:
```

## src/flask/app.py

```text
L65: T_shell_context_processor = t.TypeVar(
L66:     "T_shell_context_processor", bound=ft.ShellContextProcessorCallable
L67: )
L68: T_teardown = t.TypeVar("T_teardown", bound=ft.TeardownCallable)
L69: T_template_filter = t.TypeVar("T_template_filter", bound=ft.TemplateFilterCallable)
L70: T_template_global = t.TypeVar("T_template_global", bound=ft.TemplateGlobalCallable)
L71: T_template_test = t.TypeVar("T_template_test", bound=ft.TemplateTestCallable)
  ...
L74: def _make_timedelta(value: timedelta | int | None) -> timedelta | None:
  ...
L81: class Flask(App):
  ...
L226:     def __init__(
L227:         self,
L228:         import_name: str,
L229:         static_url_path: str | None = None,
L230:         static_folder: str | os.PathLike[str] | None = "static",
L231:         static_host: str | None = None,
L232:         host_matching: bool = False,
L233:         subdomain_matching: bool = False,
L234:         template_folder: str | os.PathLike[str] | None = "templates",
L235:         instance_path: str | None = None,
L236:         instance_relative_config: bool = False,
L237:         root_path: str | None = None,
L238:     ):
  ...
L281:     def get_send_file_max_age(self, filename: str | None) -> int | None:
  ...
L308:     def send_static_file(self, filename: str) -> Response:
  ...
L330:     def open_resource(
L331:         self, resource: str, mode: str = "rb", encoding: str | None = None
L332:     ) -> t.IO[t.AnyStr]:
  ...
L363:     def open_instance_resource(
L364:         self, resource: str, mode: str = "rb", encoding: str | None = "utf-8"
L365:     ) -> t.IO[t.AnyStr]:
  ...
L385:     def create_jinja_environment(self) -> Environment:
  ...
L425:     def create_url_adapter(self, request: Request | None) -> MapAdapter | None:
  ...
L478:     def raise_routing_exception(self, request: Request) -> t.NoReturn:
  ...
L506:     def update_template_context(self, context: dict[str, t.Any]) -> None:
  ...
L534:     def make_shell_context(self) -> dict[str, t.Any]:
  ...
L546:     def run(
L547:         self,
L548:         host: str | None = None,
L549:         port: int | None = None,
L550:         debug: bool | None = None,
L551:         load_dotenv: bool = True,
L552:         **options: t.Any,
L553:     ) -> None:
  ...
L669:     def test_client(self, use_cookies: bool = True, **kwargs: t.Any) -> FlaskClient:
  ...
L727:     def test_cli_runner(self, **kwargs: t.Any) -> FlaskCliRunner:
  ...
L744:     def handle_http_exception(
L745:         self, e: HTTPException
L746:     ) -> HTTPException | ft.ResponseReturnValue:
  ...
L779:     def handle_user_exception(
L780:         self, e: Exception
L781:     ) -> HTTPException | ft.ResponseReturnValue:
  ...
L811:     def handle_exception(self, e: Exception) -> Response:
  ...
L864:     def log_exception(
L865:         self,
L866:         exc_info: (tuple[type, BaseException, TracebackType] | tuple[None, None, None]),
L867:     ) -> None:
  ...
L879:     def dispatch_request(self) -> ft.ResponseReturnValue:
  ...
L904:     def full_dispatch_request(self) -> Response:
  ...
L922:     def finalize_request(
L923:         self,
L924:         rv: ft.ResponseReturnValue | HTTPException,
L925:         from_error_handler: bool = False,
L926:     ) -> Response:
  ...
L953:     def make_default_options_response(self) -> Response:
  ...
L966:     def ensure_sync(self, func: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
  ...
L980:     def async_to_sync(
L981:         self, func: t.Callable[..., t.Coroutine[t.Any, t.Any, t.Any]]
L982:     ) -> t.Callable[..., t.Any]:
  ...
L1003:     def url_for(
L1004:         self,
L1005:         /,
L1006:         endpoint: str,
L1007:         *,
L1008:         _anchor: str | None = None,
L1009:         _method: str | None = None,
L1010:         _scheme: str | None = None,
L1011:         _external: bool | None = None,
L1012:         **values: t.Any,
L1013:     ) -> str:
  ...
L1129:     def make_response(self, rv: ft.ResponseReturnValue) -> Response:
  ...
L1271:     def preprocess_request(self) -> ft.ResponseReturnValue | None:
  ...
L1298:     def process_response(self, response: Response) -> Response:
  ...
L1326:     def do_teardown_request(
L1327:         self,
L1328:         exc: BaseException | None = _sentinel,  # type: ignore[assignment]
L1329:     ) -> None:
  ...
L1360:     def do_teardown_appcontext(
L1361:         self,
L1362:         exc: BaseException | None = _sentinel,  # type: ignore[assignment]
L1363:     ) -> None:
  ...
L1386:     def app_context(self) -> AppContext:
  ...
L1407:     def request_context(self, environ: WSGIEnvironment) -> RequestContext:
  ...
L1423:     def test_request_context(self, *args: t.Any, **kwargs: t.Any) -> RequestContext:
  ...
L1479:     def wsgi_app(
L1480:         self, environ: WSGIEnvironment, start_response: StartResponse
L1481:     ) -> cabc.Iterable[bytes]:
  ...
L1529:     def __call__(
L1530:         self, environ: WSGIEnvironment, start_response: StartResponse
L1531:     ) -> cabc.Iterable[bytes]:
```

## src/flask/blueprints.py

```text
L18: class Blueprint(SansioBlueprint):
L19:     def __init__(
L20:         self,
L21:         name: str,
L22:         import_name: str,
L23:         static_folder: str | os.PathLike[str] | None = None,
L24:         static_url_path: str | None = None,
L25:         template_folder: str | os.PathLike[str] | None = None,
L26:         url_prefix: str | None = None,
L27:         subdomain: str | None = None,
L28:         url_defaults: dict[str, t.Any] | None = None,
L29:         root_path: str | None = None,
L30:         cli_group: str | None = _sentinel,  # type: ignore
L31:     ) -> None:
  ...
L55:     def get_send_file_max_age(self, filename: str | None) -> int | None:
  ...
L82:     def send_static_file(self, filename: str) -> Response:
  ...
L104:     def open_resource(
L105:         self, resource: str, mode: str = "rb", encoding: str | None = "utf-8"
L106:     ) -> t.IO[t.AnyStr]:
```

## src/flask/cli.py

```text
L37: class NoAppException(click.UsageError):
  ...
L41: def find_best_app(module: ModuleType) -> Flask:
  ...
L94: def _called_with_wrong_args(f: t.Callable[..., Flask]) -> bool:
  ...
L120: def find_app_by_string(module: ModuleType, app_name: str) -> Flask:
  ...
L200: def prepare_import(path: str) -> str:
  ...
L229: @t.overload
L230: def locate_app(
L231:     module_name: str, app_name: str | None, raise_if_not_found: t.Literal[True] = True
L232: ) -> Flask:
  ...
L235: @t.overload
L236: def locate_app(
L237:     module_name: str, app_name: str | None, raise_if_not_found: t.Literal[False] = ...
L238: ) -> Flask | None:
  ...
L241: def locate_app(
L242:     module_name: str, app_name: str | None, raise_if_not_found: bool = True
L243: ) -> Flask | None:
  ...
L267: def get_version(ctx: click.Context, param: click.Parameter, value: t.Any) -> None:
  ...
L283: version_option = click.Option(
L284:     ["--version"],
L285:     help="Show the Flask version.",
L286:     expose_value=False,
L287:     callback=get_version,
L288:     is_flag=True,
L289:     is_eager=True,
L290: )
  ...
L293: class ScriptInfo:
  ...
L305:     def __init__(
L306:         self,
L307:         app_import_path: str | None = None,
L308:         create_app: t.Callable[..., Flask] | None = None,
L309:         set_debug_flag: bool = True,
L310:         load_dotenv_defaults: bool = True,
L311:     ) -> None:
L312:         #: Optionally the import path for the Flask application.
  ...
L333:     def load_app(self) -> Flask:
  ...
L375: pass_script_info = click.make_pass_decorator(ScriptInfo, ensure=True)
  ...
L377: F = t.TypeVar("F", bound=t.Callable[..., t.Any])
  ...
L380: def with_appcontext(f: F) -> F:
  ...
L394:     @click.pass_context
L395:     def decorator(ctx: click.Context, /, *args: t.Any, **kwargs: t.Any) -> t.Any:
  ...
L405: class AppGroup(click.Group):
  ...
L413:     def command(  # type: ignore[override]
L414:         self, *args: t.Any, **kwargs: t.Any
L415:     ) -> t.Callable[[t.Callable[..., t.Any]], click.Command]:
  ...
L422:         def decorator(f: t.Callable[..., t.Any]) -> click.Command:
  ...
L429:     def group(  # type: ignore[override]
L430:         self, *args: t.Any, **kwargs: t.Any
L431:     ) -> t.Callable[[t.Callable[..., t.Any]], click.Group]:
  ...
L440: def _set_app(ctx: click.Context, param: click.Option, value: str | None) -> str | None:
  ...
L453: _app_option = click.Option(
L454:     ["-A", "--app"],
L455:     metavar="IMPORT",
L456:     help=(
L457:         "The Flask application or factory function to load, in the form 'module:name'."
L458:         " Module can be a dotted import or file path. Name is not required if it is"
L459:         " 'app', 'application', 'create_app', or 'make_app', and can be 'name(args)' to"
L460:         " pass arguments."
L461:     ),
L462:     is_eager=True,
L463:     expose_value=False,
L464:     callback=_set_app,
L465: )
  ...
L468: def _set_debug(ctx: click.Context, param: click.Option, value: bool) -> bool | None:
L469:     # If the flag isn't provided, it will default to False. Don't use
L470:     # that, let debug be set by env in that case.
  ...
L485: _debug_option = click.Option(
L486:     ["--debug/--no-debug"],
L487:     help="Set debug mode.",
L488:     expose_value=False,
L489:     callback=_set_debug,
L490: )
  ...
L493: def _env_file_callback(
L494:     ctx: click.Context, param: click.Option, value: str | None
L495: ) -> str | None:
  ...
L517: _env_file_option = click.Option(
L518:     ["-e", "--env-file"],
L519:     type=click.Path(exists=True, dir_okay=False),
L520:     help=(
L521:         "Load environment variables from this file, taking precedence over"
L522:         " those set by '.env' and '.flaskenv'. Variables set directly in the"
L523:         " environment take highest precedence. python-dotenv must be installed."
L524:     ),
L525:     is_eager=True,
L526:     expose_value=False,
L527:     callback=_env_file_callback,
L528: )
  ...
L531: class FlaskGroup(AppGroup):
  ...
L563:     def __init__(
L564:         self,
L565:         add_default_commands: bool = True,
L566:         create_app: t.Callable[..., Flask] | None = None,
L567:         add_version_option: bool = True,
L568:         load_dotenv: bool = True,
L569:         set_debug_flag: bool = True,
L570:         **extra: t.Any,
L571:     ) -> None:
  ...
L600:     def _load_plugin_commands(self) -> None:
  ...
L617:     def get_command(self, ctx: click.Context, name: str) -> click.Command | None:
  ...
L644:     def list_commands(self, ctx: click.Context) -> list[str]:
  ...
L665:     def make_context(
L666:         self,
L667:         info_name: str | None,
L668:         args: list[str],
L669:         parent: click.Context | None = None,
L670:         **extra: t.Any,
L671:     ) -> click.Context:
L672:         # Set a flag to tell app.run to become a no-op. If app.run was
L673:         # not in a __name__ == __main__ guard, it would start the server
L674:         # when importing, blocking whatever command is being called.
  ...
L686:     def parse_args(self, ctx: click.Context, args: list[str]) -> list[str]:
  ...
L699: def _path_is_ancestor(path: str, other: str) -> bool:
  ...
L706: def load_dotenv(
L707:     path: str | os.PathLike[str] | None = None, load_defaults: bool = True
L708: ) -> bool:
  ...
L774: def show_server_banner(debug: bool, app_import_path: str | None) -> None:
  ...
L788: class CertParamType(click.ParamType):
  ...
L796:     def __init__(self) -> None:
  ...
L799:     def convert(
L800:         self, value: t.Any, param: click.Parameter | None, ctx: click.Context | None
L801:     ) -> t.Any:
  ...
L836: def _validate_key(ctx: click.Context, param: click.Parameter, value: t.Any) -> t.Any:
  ...
L875: class SeparatedPathType(click.Path):
  ...
L881:     def convert(
L882:         self, value: t.Any, param: click.Parameter | None, ctx: click.Context | None
L883:     ) -> t.Any:
  ...
L890: @click.command("run", short_help="Run a development server.")
L891: @click.option("--host", "-h", default="127.0.0.1", help="The interface to bind to.")
L892: @click.option("--port", "-p", default=5000, help="The port to bind to.")
L893: @click.option(
L894:     "--cert",
L895:     type=CertParamType(),
L896:     help="Specify a certificate file to use HTTPS.",
L897:     is_eager=True,
L898: )
L899: @click.option(
L900:     "--key",
L901:     type=click.Path(exists=True, dir_okay=False, resolve_path=True),
L902:     callback=_validate_key,
L903:     expose_value=False,
L904:     help="The key file to use when specifying a certificate.",
L905: )
L906: @click.option(
L907:     "--reload/--no-reload",
L908:     default=None,
L909:     help="Enable or disable the reloader. By default the reloader "
L910:     "is active if debug is enabled.",
L911: )
L912: @click.option(
L913:     "--debugger/--no-debugger",
L914:     default=None,
L915:     help="Enable or disable the debugger. By default the debugger "
L916:     "is active if debug is enabled.",
L917: )
L918: @click.option(
L919:     "--with-threads/--without-threads",
L920:     default=True,
L921:     help="Enable or disable multithreading.",
L922: )
L923: @click.option(
L924:     "--extra-files",
L925:     default=None,
L926:     type=SeparatedPathType(),
L927:     help=(
L928:         "Extra files that trigger a reload on change. Multiple paths"
L929:         f" are separated by {os.path.pathsep!r}."
L930:     ),
L931: )
L932: @click.option(
L933:     "--exclude-patterns",
L934:     default=None,
L935:     type=SeparatedPathType(),
L936:     help=(
L937:         "Files matching these fnmatch patterns will not trigger a reload"
L938:         " on change. Multiple patterns are separated by"
L939:         f" {os.path.pathsep!r}."
L940:     ),
L941: )
L942: @pass_script_info
L943: def run_command(
L944:     info: ScriptInfo,
L945:     host: str,
L946:     port: int,
L947:     reload: bool,
L948:     debugger: bool,
L949:     with_threads: bool,
L950:     cert: ssl.SSLContext | tuple[str, str | None] | t.Literal["adhoc"] | None,
L951:     extra_files: list[str] | None,
L952:     exclude_patterns: list[str] | None,
L953: ) -> None:
  ...
L971:             def app(
L972:                 environ: WSGIEnvironment, start_response: StartResponse
L973:             ) -> cabc.Iterable[bytes]:
  ...
L1007: @click.command("shell", short_help="Run a shell in the app context.")
L1008: @with_appcontext
L1009: def shell_command() -> None:
  ...
L1056: @click.command("routes", short_help="Show the routes for the app.")
L1057: @click.option(
L1058:     "--sort",
L1059:     "-s",
L1060:     type=click.Choice(("endpoint", "methods", "domain", "rule", "match")),
L1061:     default="endpoint",
L1062:     help=(
L1063:         "Method to sort routes by. 'match' is the order that Flask will match routes"
L1064:         " when dispatching a request."
L1065:     ),
L1066: )
L1067: @click.option("--all-methods", is_flag=True, help="Show HEAD and OPTIONS methods.")
L1068: @with_appcontext
L1069: def routes_command(sort: str, all_methods: bool) -> None:
  ...
L1118: cli = FlaskGroup(
L1119:     name="flask",
L1120:     help="""\
L1121: A general utility script for Flask applications.
L1122: 
L1123: An application to load must be given with the '--app' option,
L1124: 'FLASK_APP' environment variable, or with a 'wsgi.py' or 'app.py' file
L1125: in the current directory.
L1126: """,
L1127: )
  ...
L1130: def main() -> None:
```

## src/flask/config.py

```text
L17: T = t.TypeVar("T")
  ...
L20: class ConfigAttribute(t.Generic[T]):
  ...
L23:     def __init__(
L24:         self, name: str, get_converter: t.Callable[[t.Any], T] | None = None
L25:     ) -> None:
  ...
L29:     @t.overload
L30:     def __get__(self, obj: None, owner: None) -> te.Self:
  ...
L32:     @t.overload
L33:     def __get__(self, obj: App, owner: type[App]) -> T:
  ...
L35:     def __get__(self, obj: App | None, owner: type[App] | None = None) -> T | te.Self:
  ...
L46:     def __set__(self, obj: App, value: t.Any) -> None:
  ...
L50: class Config(dict):  # type: ignore[type-arg]
  ...
L94:     def __init__(
L95:         self,
L96:         root_path: str | os.PathLike[str],
L97:         defaults: dict[str, t.Any] | None = None,
L98:     ) -> None:
  ...
L102:     def from_envvar(self, variable_name: str, silent: bool = False) -> bool:
  ...
L126:     def from_prefixed_env(
L127:         self, prefix: str = "FLASK", *, loads: t.Callable[[str], t.Any] = json.loads
L128:     ) -> bool:
  ...
L187:     def from_pyfile(
L188:         self, filename: str | os.PathLike[str], silent: bool = False
L189:     ) -> bool:
  ...
L218:     def from_object(self, obj: object | str) -> None:
  ...
L256:     def from_file(
L257:         self,
L258:         filename: str | os.PathLike[str],
L259:         load: t.Callable[[t.IO[t.Any]], t.Mapping[str, t.Any]],
L260:         silent: bool = False,
L261:         text: bool = True,
L262:     ) -> bool:
  ...
L304:     def from_mapping(
L305:         self, mapping: t.Mapping[str, t.Any] | None = None, **kwargs: t.Any
L306:     ) -> bool:
  ...
L323:     def get_namespace(
L324:         self, namespace: str, lowercase: bool = True, trim_namespace: bool = True
L325:     ) -> dict[str, t.Any]:
  ...
L366:     def __repr__(self) -> str:
```

## src/flask/ctx.py

```text
L26: _sentinel = object()
  ...
L29: class _AppCtxGlobals:
  ...
L52:     def __getattr__(self, name: str) -> t.Any:
  ...
L58:     def __setattr__(self, name: str, value: t.Any) -> None:
  ...
L61:     def __delattr__(self, name: str) -> None:
  ...
L67:     def get(self, name: str, default: t.Any | None = None) -> t.Any:
  ...
L78:     def pop(self, name: str, default: t.Any = _sentinel) -> t.Any:
  ...
L92:     def setdefault(self, name: str, default: t.Any = None) -> t.Any:
  ...
L104:     def __contains__(self, item: str) -> bool:
  ...
L107:     def __iter__(self) -> t.Iterator[str]:
  ...
L110:     def __repr__(self) -> str:
  ...
L117: def after_this_request(
L118:     f: ft.AfterRequestCallable[t.Any],
L119: ) -> ft.AfterRequestCallable[t.Any]:
  ...
L152: F = t.TypeVar("F", bound=t.Callable[..., t.Any])
  ...
L155: def copy_current_request_context(f: F) -> F:
  ...
L189:     def wrapper(*args: t.Any, **kwargs: t.Any) -> t.Any:
  ...
L196: def has_request_context() -> bool:
  ...
L228: def has_app_context() -> bool:
  ...
L238: class AppContext:
  ...
L245:     def __init__(self, app: Flask) -> None:
  ...
L251:     def push(self) -> None:
  ...
L256:     def pop(self, exc: BaseException | None = _sentinel) -> None:  # type: ignore
  ...
L274:     def __enter__(self) -> AppContext:
  ...
L278:     def __exit__(
L279:         self,
L280:         exc_type: type | None,
L281:         exc_value: BaseException | None,
L282:         tb: TracebackType | None,
L283:     ) -> None:
  ...
L287: class RequestContext:
  ...
L309:     def __init__(
L310:         self,
L311:         app: Flask,
L312:         environ: WSGIEnvironment,
L313:         request: Request | None = None,
L314:         session: SessionMixin | None = None,
L315:     ) -> None:
  ...
L337:     def copy(self) -> RequestContext:
  ...
L357:     def match_request(self) -> None:
  ...
L367:     def push(self) -> None:
L368:         # Before we push the request context we have to ensure that there
L369:         # is an application context.
  ...
L396:     def pop(self, exc: BaseException | None = _sentinel) -> None:  # type: ignore
  ...
L433:     def __enter__(self) -> RequestContext:
  ...
L437:     def __exit__(
L438:         self,
L439:         exc_type: type | None,
L440:         exc_value: BaseException | None,
L441:         tb: TracebackType | None,
L442:     ) -> None:
  ...
L445:     def __repr__(self) -> str:
```

## src/flask/debughelpers.py

```text
L17: class UnexpectedUnicodeError(AssertionError, UnicodeError):
  ...
L23: class DebugFilesKeyError(KeyError, AssertionError):
  ...
L28:     def __init__(self, request: Request, key: str) -> None:
  ...
L46:     def __str__(self) -> str:
  ...
L50: class FormDataRoutingRedirect(AssertionError):
  ...
L57:     def __init__(self, request: Request) -> None:
  ...
L81: def attach_enctype_error_multidict(request: Request) -> None:
  ...
L90:     class newcls(oldcls):  # type: ignore[valid-type, misc]
L91:         def __getitem__(self, key: str) -> t.Any:
  ...
L107: def _dump_loader_info(loader: BaseLoader) -> t.Iterator[str]:
  ...
L124: def explain_template_loading_attempts(
L125:     app: App,
L126:     template: str,
L127:     attempts: list[
L128:         tuple[
L129:             BaseLoader,
L130:             Scaffold,
L131:             tuple[str, str | None, t.Callable[[], bool] | None] | None,
L132:         ]
L133:     ],
L134: ) -> None:
```

## src/flask/globals.py

```text
L17: _no_app_msg = """\
L18: Working outside of application context.
L19: 
L20: This typically means that you attempted to use functionality that needed
L21: the current application. To solve this, set up an application context
L22: with app.app_context(). See the documentation for more information.\
L23: """
L24: _cv_app: ContextVar[AppContext] = ContextVar("flask.app_ctx")
L25: app_ctx: AppContext = LocalProxy(  # type: ignore[assignment]
L26:     _cv_app, unbound_message=_no_app_msg
L27: )
L28: current_app: Flask = LocalProxy(  # type: ignore[assignment]
L29:     _cv_app, "app", unbound_message=_no_app_msg
L30: )
L31: g: _AppCtxGlobals = LocalProxy(  # type: ignore[assignment]
L32:     _cv_app, "g", unbound_message=_no_app_msg
L33: )
  ...
L35: _no_req_msg = """\
L36: Working outside of request context.
L37: 
L38: This typically means that you attempted to use functionality that needed
L39: an active HTTP request. Consult the documentation on testing for
L40: information about how to avoid this problem.\
L41: """
L42: _cv_request: ContextVar[RequestContext] = ContextVar("flask.request_ctx")
L43: request_ctx: RequestContext = LocalProxy(  # type: ignore[assignment]
L44:     _cv_request, unbound_message=_no_req_msg
L45: )
L46: request: Request = LocalProxy(  # type: ignore[assignment]
L47:     _cv_request, "request", unbound_message=_no_req_msg
L48: )
L49: session: SessionMixin = LocalProxy(  # type: ignore[assignment]
L50:     _cv_request, "session", unbound_message=_no_req_msg
L51: )
```

## src/flask/helpers.py

```text
L28: def get_debug_flag() -> bool:
  ...
L36: def get_load_dotenv(default: bool = True) -> bool:
  ...
L51: @t.overload
L52: def stream_with_context(
L53:     generator_or_function: t.Iterator[t.AnyStr],
L54: ) -> t.Iterator[t.AnyStr]:
  ...
L57: @t.overload
L58: def stream_with_context(
L59:     generator_or_function: t.Callable[..., t.Iterator[t.AnyStr]],
L60: ) -> t.Callable[[t.Iterator[t.AnyStr]], t.Iterator[t.AnyStr]]:
  ...
L63: def stream_with_context(
L64:     generator_or_function: t.Iterator[t.AnyStr] | t.Callable[..., t.Iterator[t.AnyStr]],
L65: ) -> t.Iterator[t.AnyStr] | t.Callable[[t.Iterator[t.AnyStr]], t.Iterator[t.AnyStr]]:
  ...
L108:         def decorator(*args: t.Any, **kwargs: t.Any) -> t.Any:
  ...
L114:     def generator() -> t.Iterator[t.AnyStr]:
  ...
L146: def make_response(*args: t.Any) -> Response:
  ...
L195: def url_for(
L196:     endpoint: str,
L197:     *,
L198:     _anchor: str | None = None,
L199:     _method: str | None = None,
L200:     _scheme: str | None = None,
L201:     _external: bool | None = None,
L202:     **values: t.Any,
L203: ) -> str:
  ...
L249: def redirect(
L250:     location: str, code: int = 302, Response: type[BaseResponse] | None = None
L251: ) -> BaseResponse:
  ...
L273: def abort(code: int | BaseResponse, *args: t.Any, **kwargs: t.Any) -> t.NoReturn:
  ...
L296: def get_template_attribute(template_name: str, attribute: str) -> t.Any:
  ...
L318: def flash(message: str, category: str = "message") -> None:
  ...
L352: def get_flashed_messages(
L353:     with_categories: bool = False, category_filter: t.Iterable[str] = ()
L354: ) -> list[str] | list[tuple[str, str]]:
  ...
L394: def _prepare_send_file_kwargs(**kwargs: t.Any) -> dict[str, t.Any]:
  ...
L407: def send_file(
L408:     path_or_file: os.PathLike[t.AnyStr] | str | t.IO[bytes],
L409:     mimetype: str | None = None,
L410:     as_attachment: bool = False,
L411:     download_name: str | None = None,
L412:     conditional: bool = True,
L413:     etag: bool | str = True,
L414:     last_modified: datetime | int | float | None = None,
L415:     max_age: None | (int | t.Callable[[str | None], int | None]) = None,
L416: ) -> Response:
  ...
L533: def send_from_directory(
L534:     directory: os.PathLike[str] | str,
L535:     path: os.PathLike[str] | str,
L536:     **kwargs: t.Any,
L537: ) -> Response:
  ...
L577: def get_root_path(import_name: str) -> str:
  ...
L634: @cache
L635: def _split_blueprint_path(name: str) -> list[str]:
```

## src/flask/json/__init__.py

```text
L13: def dumps(obj: t.Any, **kwargs: t.Any) -> str:
  ...
L47: def dump(obj: t.Any, fp: t.IO[str], **kwargs: t.Any) -> None:
  ...
L77: def loads(s: str | bytes, **kwargs: t.Any) -> t.Any:
  ...
L108: def load(fp: t.IO[t.AnyStr], **kwargs: t.Any) -> t.Any:
  ...
L138: def jsonify(*args: t.Any, **kwargs: t.Any) -> Response:
```

## src/flask/json/provider.py

```text
L19: class JSONProvider:
  ...
L38:     def __init__(self, app: App) -> None:
  ...
L41:     def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
  ...
L49:     def dump(self, obj: t.Any, fp: t.IO[str], **kwargs: t.Any) -> None:
  ...
L59:     def loads(self, s: str | bytes, **kwargs: t.Any) -> t.Any:
  ...
L67:     def load(self, fp: t.IO[t.AnyStr], **kwargs: t.Any) -> t.Any:
  ...
L75:     def _prepare_response_obj(
L76:         self, args: tuple[t.Any, ...], kwargs: dict[str, t.Any]
L77:     ) -> t.Any:
  ...
L89:     def response(self, *args: t.Any, **kwargs: t.Any) -> Response:
  ...
L108: def _default(o: t.Any) -> t.Any:
  ...
L124: class DefaultJSONProvider(JSONProvider):
  ...
L166:     def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
  ...
L181:     def loads(self, s: str | bytes, **kwargs: t.Any) -> t.Any:
  ...
L189:     def response(self, *args: t.Any, **kwargs: t.Any) -> Response:
```

## src/flask/json/tag.py

```text
L60: class JSONTag:
  ...
L69:     def __init__(self, serializer: TaggedJSONSerializer) -> None:
  ...
L73:     def check(self, value: t.Any) -> bool:
  ...
L77:     def to_json(self, value: t.Any) -> t.Any:
  ...
L82:     def to_python(self, value: t.Any) -> t.Any:
  ...
L87:     def tag(self, value: t.Any) -> dict[str, t.Any]:
  ...
L93: class TagDict(JSONTag):
  ...
L103:     def check(self, value: t.Any) -> bool:
  ...
L110:     def to_json(self, value: t.Any) -> t.Any:
  ...
L114:     def to_python(self, value: t.Any) -> t.Any:
  ...
L119: class PassDict(JSONTag):
  ...
L122:     def check(self, value: t.Any) -> bool:
  ...
L125:     def to_json(self, value: t.Any) -> t.Any:
L126:         # JSON objects may only have string keys, so don't bother tagging the
L127:         # key here.
  ...
L133: class TagTuple(JSONTag):
  ...
L137:     def check(self, value: t.Any) -> bool:
  ...
L140:     def to_json(self, value: t.Any) -> t.Any:
  ...
L143:     def to_python(self, value: t.Any) -> t.Any:
  ...
L147: class PassList(JSONTag):
  ...
L150:     def check(self, value: t.Any) -> bool:
  ...
L153:     def to_json(self, value: t.Any) -> t.Any:
  ...
L159: class TagBytes(JSONTag):
  ...
L163:     def check(self, value: t.Any) -> bool:
  ...
L166:     def to_json(self, value: t.Any) -> t.Any:
  ...
L169:     def to_python(self, value: t.Any) -> t.Any:
  ...
L173: class TagMarkup(JSONTag):
  ...
L181:     def check(self, value: t.Any) -> bool:
  ...
L184:     def to_json(self, value: t.Any) -> t.Any:
  ...
L187:     def to_python(self, value: t.Any) -> t.Any:
  ...
L191: class TagUUID(JSONTag):
  ...
L195:     def check(self, value: t.Any) -> bool:
  ...
L198:     def to_json(self, value: t.Any) -> t.Any:
  ...
L201:     def to_python(self, value: t.Any) -> t.Any:
  ...
L205: class TagDateTime(JSONTag):
  ...
L209:     def check(self, value: t.Any) -> bool:
  ...
L212:     def to_json(self, value: t.Any) -> t.Any:
  ...
L215:     def to_python(self, value: t.Any) -> t.Any:
  ...
L219: class TaggedJSONSerializer:
  ...
L249:     def __init__(self) -> None:
  ...
L256:     def register(
L257:         self,
L258:         tag_class: type[JSONTag],
L259:         force: bool = False,
L260:         index: int | None = None,
L261:     ) -> None:
  ...
L289:     def tag(self, value: t.Any) -> t.Any:
  ...
L297:     def untag(self, value: dict[str, t.Any]) -> t.Any:
  ...
L309:     def _untag_scan(self, value: t.Any) -> t.Any:
  ...
L321:     def dumps(self, value: t.Any) -> str:
  ...
L325:     def loads(self, value: str) -> t.Any:
```

## src/flask/logging.py

```text
L15: @LocalProxy
L16: def wsgi_errors_stream() -> t.TextIO:
  ...
L31: def has_level_handler(logger: logging.Logger) -> bool:
  ...
L52: default_handler = logging.StreamHandler(wsgi_errors_stream)
  ...
L58: def create_logger(app: App) -> logging.Logger:
```

## src/flask/sansio/app.py

```text
L43: T_shell_context_processor = t.TypeVar(
L44:     "T_shell_context_processor", bound=ft.ShellContextProcessorCallable
L45: )
L46: T_teardown = t.TypeVar("T_teardown", bound=ft.TeardownCallable)
L47: T_template_filter = t.TypeVar("T_template_filter", bound=ft.TemplateFilterCallable)
L48: T_template_global = t.TypeVar("T_template_global", bound=ft.TemplateGlobalCallable)
L49: T_template_test = t.TypeVar("T_template_test", bound=ft.TemplateTestCallable)
  ...
L52: def _make_timedelta(value: timedelta | int | None) -> timedelta | None:
  ...
L59: class App(Scaffold):
  ...
L282:     def __init__(
L283:         self,
L284:         import_name: str,
L285:         static_url_path: str | None = None,
L286:         static_folder: str | os.PathLike[str] | None = "static",
L287:         static_host: str | None = None,
L288:         host_matching: bool = False,
L289:         subdomain_matching: bool = False,
L290:         template_folder: str | os.PathLike[str] | None = "templates",
L291:         instance_path: str | None = None,
L292:         instance_relative_config: bool = False,
L293:         root_path: str | None = None,
L294:     ) -> None:
  ...
L413:     def _check_setup_finished(self, f_name: str) -> None:
  ...
L425:     @cached_property
L426:     def name(self) -> str:
  ...
L442:     @cached_property
L443:     def logger(self) -> logging.Logger:
  ...
L469:     @cached_property
L470:     def jinja_env(self) -> Environment:
  ...
L479:     def create_jinja_environment(self) -> Environment:
  ...
L482:     def make_config(self, instance_relative: bool = False) -> Config:
  ...
L498:     def make_aborter(self) -> Aborter:
  ...
L510:     def auto_find_instance_path(self) -> str:
  ...
L523:     def create_global_jinja_loader(self) -> DispatchingJinjaLoader:
  ...
L536:     def select_jinja_autoescape(self, filename: str) -> bool:
  ...
L549:     @property
L550:     def debug(self) -> bool:
  ...
L562:     @debug.setter
L563:     def debug(self, value: bool) -> None:
  ...
L569:     @setupmethod
L570:     def register_blueprint(self, blueprint: Blueprint, **options: t.Any) -> None:
  ...
L597:     def iter_blueprints(self) -> t.ValuesView[Blueprint]:
  ...
L604:     @setupmethod
L605:     def add_url_rule(
L606:         self,
L607:         rule: str,
L608:         endpoint: str | None = None,
L609:         view_func: ft.RouteCallable | None = None,
L610:         provide_automatic_options: bool | None = None,
L611:         **options: t.Any,
L612:     ) -> None:
  ...
L663:     @setupmethod
L664:     def template_filter(
L665:         self, name: str | None = None
L666:     ) -> t.Callable[[T_template_filter], T_template_filter]:
  ...
L679:         def decorator(f: T_template_filter) -> T_template_filter:
  ...
L685:     @setupmethod
L686:     def add_template_filter(
L687:         self, f: ft.TemplateFilterCallable, name: str | None = None
L688:     ) -> None:
  ...
L697:     @setupmethod
L698:     def template_test(
L699:         self, name: str | None = None
L700:     ) -> t.Callable[[T_template_test], T_template_test]:
  ...
L720:         def decorator(f: T_template_test) -> T_template_test:
  ...
L726:     @setupmethod
L727:     def add_template_test(
L728:         self, f: ft.TemplateTestCallable, name: str | None = None
L729:     ) -> None:
  ...
L740:     @setupmethod
L741:     def template_global(
L742:         self, name: str | None = None
L743:     ) -> t.Callable[[T_template_global], T_template_global]:
  ...
L758:         def decorator(f: T_template_global) -> T_template_global:
  ...
L764:     @setupmethod
L765:     def add_template_global(
L766:         self, f: ft.TemplateGlobalCallable, name: str | None = None
L767:     ) -> None:
  ...
L778:     @setupmethod
L779:     def teardown_appcontext(self, f: T_teardown) -> T_teardown:
  ...
L812:     @setupmethod
L813:     def shell_context_processor(
L814:         self, f: T_shell_context_processor
L815:     ) -> T_shell_context_processor:
  ...
L823:     def _find_error_handler(
L824:         self, e: Exception, blueprints: list[str]
L825:     ) -> ft.ErrorHandlerCallable | None:
  ...
L848:     def trap_http_exception(self, e: Exception) -> bool:
  ...
L883:     def should_ignore_error(self, error: BaseException | None) -> bool:
  ...
L893:     def redirect(self, location: str, code: int = 302) -> BaseResponse:
  ...
L911:     def inject_url_defaults(self, endpoint: str, values: dict[str, t.Any]) -> None:
  ...
L932:     def handle_url_build_error(
L933:         self, error: BuildError, endpoint: str, values: dict[str, t.Any]
L934:     ) -> str:
```

## src/flask/sansio/blueprints.py

```text
L17: DeferredSetupFunction = t.Callable[["BlueprintSetupState"], None]
L18: T_after_request = t.TypeVar("T_after_request", bound=ft.AfterRequestCallable[t.Any])
L19: T_before_request = t.TypeVar("T_before_request", bound=ft.BeforeRequestCallable)
L20: T_error_handler = t.TypeVar("T_error_handler", bound=ft.ErrorHandlerCallable)
L21: T_teardown = t.TypeVar("T_teardown", bound=ft.TeardownCallable)
L22: T_template_context_processor = t.TypeVar(
L23:     "T_template_context_processor", bound=ft.TemplateContextProcessorCallable
L24: )
L25: T_template_filter = t.TypeVar("T_template_filter", bound=ft.TemplateFilterCallable)
L26: T_template_global = t.TypeVar("T_template_global", bound=ft.TemplateGlobalCallable)
L27: T_template_test = t.TypeVar("T_template_test", bound=ft.TemplateTestCallable)
L28: T_url_defaults = t.TypeVar("T_url_defaults", bound=ft.URLDefaultCallable)
L29: T_url_value_preprocessor = t.TypeVar(
L30:     "T_url_value_preprocessor", bound=ft.URLValuePreprocessorCallable
L31: )
  ...
L34: class BlueprintSetupState:
  ...
L41:     def __init__(
L42:         self,
L43:         blueprint: Blueprint,
L44:         app: App,
L45:         options: t.Any,
L46:         first_registration: bool,
L47:     ) -> None:
L48:         #: a reference to the current application
  ...
L87:     def add_url_rule(
L88:         self,
L89:         rule: str,
L90:         endpoint: str | None = None,
L91:         view_func: ft.RouteCallable | None = None,
L92:         **options: t.Any,
L93:     ) -> None:
  ...
L119: class Blueprint(Scaffold):
  ...
L174:     def __init__(
L175:         self,
L176:         name: str,
L177:         import_name: str,
L178:         static_folder: str | os.PathLike[str] | None = None,
L179:         static_url_path: str | None = None,
L180:         template_folder: str | os.PathLike[str] | None = None,
L181:         url_prefix: str | None = None,
L182:         subdomain: str | None = None,
L183:         url_defaults: dict[str, t.Any] | None = None,
L184:         root_path: str | None = None,
L185:         cli_group: str | None = _sentinel,  # type: ignore[assignment]
L186:     ):
  ...
L213:     def _check_setup_finished(self, f_name: str) -> None:
  ...
L223:     @setupmethod
L224:     def record(self, func: DeferredSetupFunction) -> None:
  ...
L232:     @setupmethod
L233:     def record_once(self, func: DeferredSetupFunction) -> None:
  ...
L240:         def wrapper(state: BlueprintSetupState) -> None:
  ...
L246:     def make_setup_state(
L247:         self, app: App, options: dict[str, t.Any], first_registration: bool = False
L248:     ) -> BlueprintSetupState:
  ...
L255:     @setupmethod
L256:     def register_blueprint(self, blueprint: Blueprint, **options: t.Any) -> None:
  ...
L273:     def register(self, app: App, options: dict[str, t.Any]) -> None:
  ...
L379:     def _merge_blueprint_funcs(self, app: App, name: str) -> None:
L380:         def extend(
L381:             bp_dict: dict[ft.AppOrBlueprintKey, list[t.Any]],
L382:             parent_dict: dict[ft.AppOrBlueprintKey, list[t.Any]],
L383:         ) -> None:
  ...
L412:     @setupmethod
L413:     def add_url_rule(
L414:         self,
L415:         rule: str,
L416:         endpoint: str | None = None,
L417:         view_func: ft.RouteCallable | None = None,
L418:         provide_automatic_options: bool | None = None,
L419:         **options: t.Any,
L420:     ) -> None:
  ...
L443:     @setupmethod
L444:     def app_template_filter(
L445:         self, name: str | None = None
L446:     ) -> t.Callable[[T_template_filter], T_template_filter]:
  ...
L454:         def decorator(f: T_template_filter) -> T_template_filter:
  ...
L460:     @setupmethod
L461:     def add_app_template_filter(
L462:         self, f: ft.TemplateFilterCallable, name: str | None = None
L463:     ) -> None:
  ...
L472:         def register_template(state: BlueprintSetupState) -> None:
  ...
L477:     @setupmethod
L478:     def app_template_test(
L479:         self, name: str | None = None
L480:     ) -> t.Callable[[T_template_test], T_template_test]:
  ...
L490:         def decorator(f: T_template_test) -> T_template_test:
  ...
L496:     @setupmethod
L497:     def add_app_template_test(
L498:         self, f: ft.TemplateTestCallable, name: str | None = None
L499:     ) -> None:
  ...
L510:         def register_template(state: BlueprintSetupState) -> None:
  ...
L515:     @setupmethod
L516:     def app_template_global(
L517:         self, name: str | None = None
L518:     ) -> t.Callable[[T_template_global], T_template_global]:
  ...
L528:         def decorator(f: T_template_global) -> T_template_global:
  ...
L534:     @setupmethod
L535:     def add_app_template_global(
L536:         self, f: ft.TemplateGlobalCallable, name: str | None = None
L537:     ) -> None:
  ...
L548:         def register_template(state: BlueprintSetupState) -> None:
  ...
L553:     @setupmethod
L554:     def before_app_request(self, f: T_before_request) -> T_before_request:
  ...
L563:     @setupmethod
L564:     def after_app_request(self, f: T_after_request) -> T_after_request:
  ...
L573:     @setupmethod
L574:     def teardown_app_request(self, f: T_teardown) -> T_teardown:
  ...
L583:     @setupmethod
L584:     def app_context_processor(
L585:         self, f: T_template_context_processor
L586:     ) -> T_template_context_processor:
  ...
L595:     @setupmethod
L596:     def app_errorhandler(
L597:         self, code: type[Exception] | int
L598:     ) -> t.Callable[[T_error_handler], T_error_handler]:
  ...
L603:         def decorator(f: T_error_handler) -> T_error_handler:
L604:             def from_blueprint(state: BlueprintSetupState) -> None:
  ...
L612:     @setupmethod
L613:     def app_url_value_preprocessor(
L614:         self, f: T_url_value_preprocessor
L615:     ) -> T_url_value_preprocessor:
  ...
L624:     @setupmethod
L625:     def app_url_defaults(self, f: T_url_defaults) -> T_url_defaults:
```

## src/flask/sansio/scaffold.py

```text
L25: _sentinel = object()
  ...
L27: F = t.TypeVar("F", bound=t.Callable[..., t.Any])
L28: T_after_request = t.TypeVar("T_after_request", bound=ft.AfterRequestCallable[t.Any])
L29: T_before_request = t.TypeVar("T_before_request", bound=ft.BeforeRequestCallable)
L30: T_error_handler = t.TypeVar("T_error_handler", bound=ft.ErrorHandlerCallable)
L31: T_teardown = t.TypeVar("T_teardown", bound=ft.TeardownCallable)
L32: T_template_context_processor = t.TypeVar(
L33:     "T_template_context_processor", bound=ft.TemplateContextProcessorCallable
L34: )
L35: T_url_defaults = t.TypeVar("T_url_defaults", bound=ft.URLDefaultCallable)
L36: T_url_value_preprocessor = t.TypeVar(
L37:     "T_url_value_preprocessor", bound=ft.URLValuePreprocessorCallable
L38: )
L39: T_route = t.TypeVar("T_route", bound=ft.RouteCallable)
  ...
L42: def setupmethod(f: F) -> F:
  ...
L45:     def wrapper_func(self: Scaffold, *args: t.Any, **kwargs: t.Any) -> t.Any:
  ...
L52: class Scaffold:
  ...
L75:     def __init__(
L76:         self,
L77:         import_name: str,
L78:         static_folder: str | os.PathLike[str] | None = None,
L79:         static_url_path: str | None = None,
L80:         template_folder: str | os.PathLike[str] | None = None,
L81:         root_path: str | None = None,
L82:     ):
L83:         #: The name of the package or module that this object belongs
L84:         #: to. Do not change this once it is set by the constructor.
  ...
L217:     def __repr__(self) -> str:
  ...
L220:     def _check_setup_finished(self, f_name: str) -> None:
  ...
L223:     @property
L224:     def static_folder(self) -> str | None:
  ...
L233:     @static_folder.setter
L234:     def static_folder(self, value: str | os.PathLike[str] | None) -> None:
  ...
L240:     @property
L241:     def has_static_folder(self) -> bool:
  ...
L248:     @property
L249:     def static_url_path(self) -> str | None:
  ...
L264:     @static_url_path.setter
L265:     def static_url_path(self, value: str | None) -> None:
  ...
L271:     @cached_property
L272:     def jinja_loader(self) -> BaseLoader | None:
  ...
L284:     def _method_route(
L285:         self,
L286:         method: str,
L287:         rule: str,
L288:         options: dict[str, t.Any],
L289:     ) -> t.Callable[[T_route], T_route]:
  ...
L295:     @setupmethod
L296:     def get(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
  ...
L303:     @setupmethod
L304:     def post(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
  ...
L311:     @setupmethod
L312:     def put(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
  ...
L319:     @setupmethod
L320:     def delete(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
  ...
L327:     @setupmethod
L328:     def patch(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
  ...
L335:     @setupmethod
L336:     def route(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
  ...
L360:         def decorator(f: T_route) -> T_route:
  ...
L367:     @setupmethod
L368:     def add_url_rule(
L369:         self,
L370:         rule: str,
L371:         endpoint: str | None = None,
L372:         view_func: ft.RouteCallable | None = None,
L373:         provide_automatic_options: bool | None = None,
L374:         **options: t.Any,
L375:     ) -> None:
  ...
L435:     @setupmethod
L436:     def endpoint(self, endpoint: str) -> t.Callable[[F], F]:
  ...
L453:         def decorator(f: F) -> F:
  ...
L459:     @setupmethod
L460:     def before_request(self, f: T_before_request) -> T_before_request:
  ...
L486:     @setupmethod
L487:     def after_request(self, f: T_after_request) -> T_after_request:
  ...
L507:     @setupmethod
L508:     def teardown_request(self, f: T_teardown) -> T_teardown:
  ...
L541:     @setupmethod
L542:     def context_processor(
L543:         self,
L544:         f: T_template_context_processor,
L545:     ) -> T_template_context_processor:
  ...
L558:     @setupmethod
L559:     def url_value_preprocessor(
L560:         self,
L561:         f: T_url_value_preprocessor,
L562:     ) -> T_url_value_preprocessor:
  ...
L583:     @setupmethod
L584:     def url_defaults(self, f: T_url_defaults) -> T_url_defaults:
  ...
L597:     @setupmethod
L598:     def errorhandler(
L599:         self, code_or_exception: type[Exception] | int
L600:     ) -> t.Callable[[T_error_handler], T_error_handler]:
  ...
L635:         def decorator(f: T_error_handler) -> T_error_handler:
  ...
L641:     @setupmethod
L642:     def register_error_handler(
L643:         self,
L644:         code_or_exception: type[Exception] | int,
L645:         f: ft.ErrorHandlerCallable,
L646:     ) -> None:
  ...
L656:     @staticmethod
L657:     def _get_exc_class_and_code(
L658:         exc_class_or_code: type[Exception] | int,
L659:     ) -> tuple[type[Exception], int | None]:
  ...
L701: def _endpoint_from_view_func(view_func: ft.RouteCallable) -> str:
  ...
L709: def _find_package_path(import_name: str) -> str:
  ...
L754: def find_package(import_name: str) -> tuple[str | None, str]:
```

## src/flask/sessions.py

```text
L24: class SessionMixin(MutableMapping[str, t.Any]):
  ...
L27:     @property
L28:     def permanent(self) -> bool:
  ...
L32:     @permanent.setter
L33:     def permanent(self, value: bool) -> None:
  ...
L52: class SecureCookieSession(CallbackDict[str, t.Any], SessionMixin):
  ...
L74:     def __init__(
L75:         self,
L76:         initial: c.Mapping[str, t.Any] | c.Iterable[tuple[str, t.Any]] | None = None,
L77:     ) -> None:
L78:         def on_update(self: te.Self) -> None:
  ...
L84:     def __getitem__(self, key: str) -> t.Any:
  ...
L88:     def get(self, key: str, default: t.Any = None) -> t.Any:
  ...
L92:     def setdefault(self, key: str, default: t.Any = None) -> t.Any:
  ...
L97: class NullSession(SecureCookieSession):
  ...
L103:     def _fail(self, *args: t.Any, **kwargs: t.Any) -> t.NoReturn:
  ...
L114: class SessionInterface:
  ...
L164:     def make_null_session(self, app: Flask) -> NullSession:
  ...
L176:     def is_null_session(self, obj: object) -> bool:
  ...
L185:     def get_cookie_name(self, app: Flask) -> str:
  ...
L189:     def get_cookie_domain(self, app: Flask) -> str | None:
  ...
L201:     def get_cookie_path(self, app: Flask) -> str:
  ...
L209:     def get_cookie_httponly(self, app: Flask) -> bool:
  ...
L216:     def get_cookie_secure(self, app: Flask) -> bool:
  ...
L222:     def get_cookie_samesite(self, app: Flask) -> str | None:
  ...
L229:     def get_cookie_partitioned(self, app: Flask) -> bool:
  ...
L237:     def get_expiration_time(self, app: Flask, session: SessionMixin) -> datetime | None:
  ...
L247:     def should_set_cookie(self, app: Flask, session: SessionMixin) -> bool:
  ...
L263:     def open_session(self, app: Flask, request: Request) -> SessionMixin | None:
  ...
L277:     def save_session(
L278:         self, app: Flask, session: SessionMixin, response: Response
L279:     ) -> None:
  ...
L287: session_json_serializer = TaggedJSONSerializer()
  ...
L290: def _lazy_sha1(string: bytes = b"") -> t.Any:
  ...
L298: class SecureCookieSessionInterface(SessionInterface):
  ...
L317:     def get_signing_serializer(self, app: Flask) -> URLSafeTimedSerializer | None:
  ...
L337:     def open_session(self, app: Flask, request: Request) -> SecureCookieSession | None:
  ...
L351:     def save_session(
L352:         self, app: Flask, session: SessionMixin, response: Response
L353:     ) -> None:
```

## src/flask/signals.py

```text
L6: _signals = Namespace()
  ...
L8: template_rendered = _signals.signal("template-rendered")
L9: before_render_template = _signals.signal("before-render-template")
L10: request_started = _signals.signal("request-started")
L11: request_finished = _signals.signal("request-finished")
L12: request_tearing_down = _signals.signal("request-tearing-down")
L13: got_request_exception = _signals.signal("got-request-exception")
L14: appcontext_tearing_down = _signals.signal("appcontext-tearing-down")
L15: appcontext_pushed = _signals.signal("appcontext-pushed")
L16: appcontext_popped = _signals.signal("appcontext-popped")
L17: message_flashed = _signals.signal("message-flashed")
```

## src/flask/templating.py

```text
L24: def _default_template_ctx_processor() -> dict[str, t.Any]:
  ...
L39: class Environment(BaseEnvironment):
  ...
L45:     def __init__(self, app: App, **options: t.Any) -> None:
  ...
L52: class DispatchingJinjaLoader(BaseLoader):
  ...
L57:     def __init__(self, app: App) -> None:
  ...
L60:     def get_source(
L61:         self, environment: BaseEnvironment, template: str
L62:     ) -> tuple[str, str | None, t.Callable[[], bool] | None]:
  ...
L67:     def _get_source_explained(
L68:         self, environment: BaseEnvironment, template: str
L69:     ) -> tuple[str, str | None, t.Callable[[], bool] | None]:
  ...
L91:     def _get_source_fast(
L92:         self, environment: BaseEnvironment, template: str
L93:     ) -> tuple[str, str | None, t.Callable[[], bool] | None]:
  ...
L101:     def _iter_loaders(self, template: str) -> t.Iterator[tuple[Scaffold, BaseLoader]]:
  ...
L111:     def list_templates(self) -> list[str]:
  ...
L126: def _render(app: Flask, template: Template, context: dict[str, t.Any]) -> str:
  ...
L138: def render_template(
L139:     template_name_or_list: str | Template | list[str | Template],
L140:     **context: t.Any,
L141: ) -> str:
  ...
L153: def render_template_string(source: str, **context: t.Any) -> str:
  ...
L165: def _stream(
L166:     app: Flask, template: Template, context: dict[str, t.Any]
L167: ) -> t.Iterator[str]:
  ...
L173:     def generate() -> t.Iterator[str]:
  ...
L188: def stream_template(
L189:     template_name_or_list: str | Template | list[str | Template],
L190:     **context: t.Any,
L191: ) -> t.Iterator[str]:
  ...
L207: def stream_template_string(source: str, **context: t.Any) -> t.Iterator[str]:
```

## src/flask/testing.py

```text
L27: class EnvironBuilder(werkzeug.test.EnvironBuilder):
  ...
L49:     def __init__(
L50:         self,
L51:         app: Flask,
L52:         path: str = "/",
L53:         base_url: str | None = None,
L54:         subdomain: str | None = None,
L55:         url_scheme: str | None = None,
L56:         *args: t.Any,
L57:         **kwargs: t.Any,
L58:     ) -> None:
  ...
L88:     def json_dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
  ...
L97: _werkzeug_version = ""
  ...
L100: def _get_werkzeug_version() -> str:
  ...
L109: class FlaskClient(Client):
  ...
L125:     def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
  ...
L135:     @contextmanager
L136:     def session_transaction(
L137:         self, *args: t.Any, **kwargs: t.Any
L138:     ) -> t.Iterator[SessionMixin]:
  ...
L185:     def _copy_environ(self, other: WSGIEnvironment) -> WSGIEnvironment:
  ...
L193:     def _request_from_builder_args(
L194:         self, args: tuple[t.Any, ...], kwargs: dict[str, t.Any]
L195:     ) -> BaseRequest:
  ...
L204:     def open(
L205:         self,
L206:         *args: t.Any,
L207:         buffered: bool = False,
L208:         follow_redirects: bool = False,
L209:         **kwargs: t.Any,
L210:     ) -> TestResponse:
  ...
L249:     def __enter__(self) -> FlaskClient:
  ...
L255:     def __exit__(
L256:         self,
L257:         exc_type: type | None,
L258:         exc_value: BaseException | None,
L259:         tb: TracebackType | None,
L260:     ) -> None:
  ...
L265: class FlaskCliRunner(CliRunner):
  ...
L271:     def __init__(self, app: Flask, **kwargs: t.Any) -> None:
  ...
L275:     def invoke(  # type: ignore
L276:         self, cli: t.Any = None, args: t.Any = None, **kwargs: t.Any
L277:     ) -> Result:
```

## src/flask/typing.py

```text
L12: ResponseValue = t.Union[
L13:     "Response",
L14:     str,
L15:     bytes,
L16:     list[t.Any],
L17:     # Only dict is actually accepted, but Mapping allows for TypedDict.
L18:     t.Mapping[str, t.Any],
L19:     t.Iterator[str],
L20:     t.Iterator[bytes],
L21:     cabc.AsyncIterable[str],  # for Quart, until App is generic.
L22:     cabc.AsyncIterable[bytes],
L23: ]
  ...
L27: HeaderValue = t.Union[str, list[str], tuple[str, ...]]
  ...
L30: HeadersValue = t.Union[
L31:     "Headers",
L32:     t.Mapping[str, HeaderValue],
L33:     t.Sequence[tuple[str, HeaderValue]],
L34: ]
  ...
L37: ResponseReturnValue = t.Union[
L38:     ResponseValue,
L39:     tuple[ResponseValue, HeadersValue],
L40:     tuple[ResponseValue, int],
L41:     tuple[ResponseValue, int, HeadersValue],
L42:     "WSGIApplication",
L43: ]
  ...
L48: ResponseClass = t.TypeVar("ResponseClass", bound="Response")
  ...
L50: AppOrBlueprintKey = t.Optional[str]
L51: AfterRequestCallable = t.Union[
L52:     t.Callable[[ResponseClass], ResponseClass],
L53:     t.Callable[[ResponseClass], t.Awaitable[ResponseClass]],
L54: ]
L55: BeforeFirstRequestCallable = t.Union[
L56:     t.Callable[[], None], t.Callable[[], t.Awaitable[None]]
L57: ]
L58: BeforeRequestCallable = t.Union[
L59:     t.Callable[[], t.Optional[ResponseReturnValue]],
L60:     t.Callable[[], t.Awaitable[t.Optional[ResponseReturnValue]]],
L61: ]
L62: ShellContextProcessorCallable = t.Callable[[], dict[str, t.Any]]
L63: TeardownCallable = t.Union[
L64:     t.Callable[[t.Optional[BaseException]], None],
L65:     t.Callable[[t.Optional[BaseException]], t.Awaitable[None]],
L66: ]
L67: TemplateContextProcessorCallable = t.Union[
L68:     t.Callable[[], dict[str, t.Any]],
L69:     t.Callable[[], t.Awaitable[dict[str, t.Any]]],
L70: ]
L71: TemplateFilterCallable = t.Callable[..., t.Any]
L72: TemplateGlobalCallable = t.Callable[..., t.Any]
L73: TemplateTestCallable = t.Callable[..., bool]
L74: URLDefaultCallable = t.Callable[[str, dict[str, t.Any]], None]
L75: URLValuePreprocessorCallable = t.Callable[
L76:     [t.Optional[str], t.Optional[dict[str, t.Any]]], None
L77: ]
  ...
L85: ErrorHandlerCallable = t.Union[
L86:     t.Callable[[t.Any], ResponseReturnValue],
L87:     t.Callable[[t.Any], t.Awaitable[ResponseReturnValue]],
L88: ]
  ...
L90: RouteCallable = t.Union[
L91:     t.Callable[..., ResponseReturnValue],
L92:     t.Callable[..., t.Awaitable[ResponseReturnValue]],
L93: ]
```

## src/flask/views.py

```text
L9: F = t.TypeVar("F", bound=t.Callable[..., t.Any])
  ...
L11: http_method_funcs = frozenset(
L12:     ["get", "post", "head", "options", "delete", "put", "trace", "patch"]
L13: )
  ...
L16: class View:
  ...
L78:     def dispatch_request(self) -> ft.ResponseReturnValue:
  ...
L85:     @classmethod
L86:     def as_view(
L87:         cls, name: str, *class_args: t.Any, **class_kwargs: t.Any
L88:     ) -> ft.RouteCallable:
  ...
L106:             def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
  ...
L115:             def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
  ...
L138: class MethodView(View):
  ...
L165:     def __init_subclass__(cls, **kwargs: t.Any) -> None:
  ...
L182:     def dispatch_request(self, **kwargs: t.Any) -> ft.ResponseReturnValue:
```

## src/flask/wrappers.py

```text
L18: class Request(RequestBase):
  ...
L59:     @property
L60:     def max_content_length(self) -> int | None:
  ...
L88:     @max_content_length.setter
L89:     def max_content_length(self, value: int | None) -> None:
  ...
L92:     @property
L93:     def max_form_memory_size(self) -> int | None:
  ...
L115:     @max_form_memory_size.setter
L116:     def max_form_memory_size(self, value: int | None) -> None:
  ...
L119:     @property  # type: ignore[override]
L120:     def max_form_parts(self) -> int | None:
  ...
L142:     @max_form_parts.setter
L143:     def max_form_parts(self, value: int | None) -> None:
  ...
L146:     @property
L147:     def endpoint(self) -> str | None:
  ...
L161:     @property
L162:     def blueprint(self) -> str | None:
  ...
L180:     @property
L181:     def blueprints(self) -> list[str]:
  ...
L197:     def _load_form_data(self) -> None:
  ...
L212:     def on_json_loading_failed(self, e: ValueError | None) -> t.Any:
  ...
L222: class Response(ResponseBase):
  ...
L246:     @property
L247:     def max_cookie_size(self) -> int:  # type: ignore
```

