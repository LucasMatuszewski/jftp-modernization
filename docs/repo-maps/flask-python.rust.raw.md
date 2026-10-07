# Repository map

src/flask/logging.py:L31: def has_level_handler(logger: logging.Logger) -> bool:
src/flask/__init__.py:L47: def __getattr__(name: str) -> t.Any:
src/flask/debughelpers.py:L23: class DebugFilesKeyError(KeyError, AssertionError):
src/flask/json/tag.py:L82: def to_python(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L114: def to_python(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L143: def to_python(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L169: def to_python(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L187: def to_python(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L201: def to_python(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L215: def to_python(self, value: t.Any) -> t.Any:
src/flask/helpers.py:L533: def send_from_directory(
src/flask/app.py:L966: def ensure_sync(self, func: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
src/flask/sessions.py:L185: def get_cookie_name(self, app: Flask) -> str:
src/flask/sessions.py:L317: def get_signing_serializer(self, app: Flask) -> URLSafeTimedSerializer | None:
src/flask/sansio/app.py:L605: def add_url_rule(
src/flask/sansio/blueprints.py:L87: def add_url_rule(
src/flask/sansio/blueprints.py:L413: def add_url_rule(
src/flask/sansio/scaffold.py:L368: def add_url_rule(
src/flask/app.py:L1129: def make_response(self, rv: ft.ResponseReturnValue) -> Response:
src/flask/helpers.py:L146: def make_response(*args: t.Any) -> Response:
src/flask/helpers.py:L52: def stream_with_context(
src/flask/helpers.py:L58: def stream_with_context(
src/flask/helpers.py:L63: def stream_with_context(
src/flask/json/__init__.py:L13: def dumps(obj: t.Any, **kwargs: t.Any) -> str:
src/flask/json/provider.py:L41: def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
src/flask/json/provider.py:L166: def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
src/flask/json/tag.py:L321: def dumps(self, value: t.Any) -> str:
src/flask/helpers.py:L407: def send_file(
src/flask/ctx.py:L92: def setdefault(self, name: str, default: t.Any = None) -> t.Any:
src/flask/sessions.py:L92: def setdefault(self, key: str, default: t.Any = None) -> t.Any:
src/flask/json/__init__.py:L77: def loads(s: str | bytes, **kwargs: t.Any) -> t.Any:
src/flask/json/provider.py:L59: def loads(self, s: str | bytes, **kwargs: t.Any) -> t.Any:
src/flask/json/provider.py:L181: def loads(self, s: str | bytes, **kwargs: t.Any) -> t.Any:
src/flask/json/tag.py:L325: def loads(self, value: str) -> t.Any:
src/flask/json/tag.py:L219: class TaggedJSONSerializer:
src/flask/sessions.py:L189: def get_cookie_domain(self, app: Flask) -> str | None:
src/flask/sessions.py:L209: def get_cookie_httponly(self, app: Flask) -> bool:
src/flask/sessions.py:L229: def get_cookie_partitioned(self, app: Flask) -> bool:
src/flask/sessions.py:L201: def get_cookie_path(self, app: Flask) -> str:
src/flask/sessions.py:L222: def get_cookie_samesite(self, app: Flask) -> str | None:
src/flask/sessions.py:L216: def get_cookie_secure(self, app: Flask) -> bool:
src/flask/sessions.py:L237: def get_expiration_time(self, app: Flask, session: SessionMixin) -> datetime | None:
src/flask/sessions.py:L247: def should_set_cookie(self, app: Flask, session: SessionMixin) -> bool:
src/flask/helpers.py:L28: def get_debug_flag() -> bool:
src/flask/sansio/blueprints.py:L233: def record_once(self, func: DeferredSetupFunction) -> None:
src/flask/ctx.py:L67: def get(self, name: str, default: t.Any | None = None) -> t.Any:
src/flask/sansio/scaffold.py:L296: def get(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
src/flask/sessions.py:L88: def get(self, key: str, default: t.Any = None) -> t.Any:
src/flask/json/tag.py:L87: def tag(self, value: t.Any) -> dict[str, t.Any]:
src/flask/json/tag.py:L289: def tag(self, value: t.Any) -> t.Any:
src/flask/cli.py:L37: class NoAppException(click.UsageError):
src/flask/cli.py:L1130: def main() -> None:
src/flask/app.py:L425: def create_url_adapter(self, request: Request | None) -> MapAdapter | None:
src/flask/app.py:L1386: def app_context(self) -> AppContext:
src/flask/helpers.py:L577: def get_root_path(import_name: str) -> str:
src/flask/sansio/scaffold.py:L642: def register_error_handler(
src/flask/json/tag.py:L309: def _untag_scan(self, value: t.Any) -> t.Any:
src/flask/debughelpers.py:L81: def attach_enctype_error_multidict(request: Request) -> None:
src/flask/wrappers.py:L212: def on_json_loading_failed(self, e: ValueError | None) -> t.Any:
src/flask/sessions.py:L263: def open_session(self, app: Flask, request: Request) -> SessionMixin | None:
src/flask/sessions.py:L337: def open_session(self, app: Flask, request: Request) -> SecureCookieSession | None:
src/flask/app.py:L281: def get_send_file_max_age(self, filename: str | None) -> int | None:
src/flask/blueprints.py:L55: def get_send_file_max_age(self, filename: str | None) -> int | None:
src/flask/cli.py:L405: class AppGroup(click.Group):
src/flask/debughelpers.py:L91: def __getitem__(self, key: str) -> t.Any:
src/flask/sessions.py:L84: def __getitem__(self, key: str) -> t.Any:
src/flask/globals.py:L24: _cv_app: ContextVar[AppContext] = ContextVar("flask.app_ctx")
src/flask/globals.py:L42: _cv_request: ContextVar[RequestContext] = ContextVar("flask.request_ctx")
src/flask/globals.py:L17: _no_app_msg = """\
src/flask/globals.py:L35: _no_req_msg = """\
src/flask/globals.py:L25: app_ctx: AppContext = LocalProxy(  # type: ignore[assignment]
src/flask/globals.py:L28: current_app: Flask = LocalProxy(  # type: ignore[assignment]
src/flask/globals.py:L31: g: _AppCtxGlobals = LocalProxy(  # type: ignore[assignment]
src/flask/globals.py:L46: request: Request = LocalProxy(  # type: ignore[assignment]
src/flask/globals.py:L43: request_ctx: RequestContext = LocalProxy(  # type: ignore[assignment]
src/flask/globals.py:L49: session: SessionMixin = LocalProxy(  # type: ignore[assignment]
src/flask/cli.py:L333: def load_app(self) -> Flask:
src/flask/config.py:L304: def from_mapping(
src/flask/config.py:L218: def from_object(self, obj: object | str) -> None:
src/flask/config.py:L187: def from_pyfile(
src/flask/json/tag.py:L256: def register(
src/flask/sansio/blueprints.py:L273: def register(self, app: App, options: dict[str, t.Any]) -> None:
src/flask/app.py:L385: def create_jinja_environment(self) -> Environment:
src/flask/logging.py:L58: def create_logger(app: App) -> logging.Logger:
src/flask/sansio/app.py:L686: def add_template_filter(
src/flask/sansio/app.py:L765: def add_template_global(
src/flask/sansio/app.py:L727: def add_template_test(
src/flask/sansio/app.py:L510: def auto_find_instance_path(self) -> str:
src/flask/sansio/app.py:L479: def create_jinja_environment(self) -> Environment:
src/flask/sansio/app.py:L498: def make_aborter(self) -> Aborter:
src/flask/sansio/app.py:L482: def make_config(self, instance_relative: bool = False) -> Config:
src/flask/sansio/scaffold.py:L754: def find_package(import_name: str) -> tuple[str | None, str]:
src/flask/templating.py:L52: class DispatchingJinjaLoader(BaseLoader):
src/flask/signals.py:L6: _signals = Namespace()
src/flask/signals.py:L16: appcontext_popped = _signals.signal("appcontext-popped")
src/flask/signals.py:L15: appcontext_pushed = _signals.signal("appcontext-pushed")
src/flask/signals.py:L14: appcontext_tearing_down = _signals.signal("appcontext-tearing-down")
src/flask/signals.py:L9: before_render_template = _signals.signal("before-render-template")
src/flask/signals.py:L13: got_request_exception = _signals.signal("got-request-exception")
src/flask/signals.py:L17: message_flashed = _signals.signal("message-flashed")
src/flask/signals.py:L11: request_finished = _signals.signal("request-finished")
src/flask/signals.py:L10: request_started = _signals.signal("request-started")
src/flask/signals.py:L12: request_tearing_down = _signals.signal("request-tearing-down")
src/flask/signals.py:L8: template_rendered = _signals.signal("template-rendered")
src/flask/cli.py:L706: def load_dotenv(
src/flask/cli.py:L774: def show_server_banner(debug: bool, app_import_path: str | None) -> None:
src/flask/helpers.py:L36: def get_load_dotenv(default: bool = True) -> bool:
src/flask/cli.py:L293: class ScriptInfo:
src/flask/ctx.py:L78: def pop(self, name: str, default: t.Any = _sentinel) -> t.Any:
src/flask/ctx.py:L256: def pop(self, exc: BaseException | None = _sentinel) -> None:  # type: ignore
src/flask/ctx.py:L396: def pop(self, exc: BaseException | None = _sentinel) -> None:  # type: ignore
src/flask/debughelpers.py:L107: def _dump_loader_info(loader: BaseLoader) -> t.Iterator[str]:
src/flask/json/tag.py:L73: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L103: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L122: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L137: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L150: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L163: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L181: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L195: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L209: def check(self, value: t.Any) -> bool:
src/flask/json/tag.py:L77: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L110: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L125: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L140: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L153: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L166: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L184: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L198: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L212: def to_json(self, value: t.Any) -> t.Any:
src/flask/json/tag.py:L297: def untag(self, value: dict[str, t.Any]) -> t.Any:
src/flask/sessions.py:L176: def is_null_session(self, obj: object) -> bool:
src/flask/sessions.py:L277: def save_session(
src/flask/sessions.py:L351: def save_session(
src/flask/testing.py:L27: class EnvironBuilder(werkzeug.test.EnvironBuilder):
src/flask/app.py:L1360: def do_teardown_appcontext(
src/flask/app.py:L1326: def do_teardown_request(
src/flask/ctx.py:L357: def match_request(self) -> None:
src/flask/sessions.py:L164: def make_null_session(self, app: Flask) -> NullSession:
src/flask/cli.py:L875: class SeparatedPathType(click.Path):
src/flask/cli.py:L617: def get_command(self, ctx: click.Context, name: str) -> click.Command | None:
src/flask/cli.py:L644: def list_commands(self, ctx: click.Context) -> list[str]:
src/flask/cli.py:L230: def locate_app(
src/flask/cli.py:L236: def locate_app(
src/flask/cli.py:L241: def locate_app(
src/flask/cli.py:L200: def prepare_import(path: str) -> str:
src/flask/sansio/blueprints.py:L380: def extend(
src/flask/json/provider.py:L75: def _prepare_response_obj(
src/flask/json/__init__.py:L108: def load(fp: t.IO[t.AnyStr], **kwargs: t.Any) -> t.Any:
src/flask/json/provider.py:L67: def load(self, fp: t.IO[t.AnyStr], **kwargs: t.Any) -> t.Any:
src/flask/sansio/blueprints.py:L34: class BlueprintSetupState:
src/flask/sansio/blueprints.py:L461: def add_app_template_filter(
src/flask/sansio/blueprints.py:L535: def add_app_template_global(
src/flask/sansio/blueprints.py:L497: def add_app_template_test(
src/flask/sansio/blueprints.py:L246: def make_setup_state(
src/flask/app.py:L922: def finalize_request(
src/flask/app.py:L1407: def request_context(self, environ: WSGIEnvironment) -> RequestContext:
src/flask/typing.py:L51: AfterRequestCallable = t.Union[
src/flask/typing.py:L50: AppOrBlueprintKey = t.Optional[str]  # The App key is None, whereas blueprints are named
src/flask/typing.py:L55: BeforeFirstRequestCallable = t.Union[
src/flask/typing.py:L58: BeforeRequestCallable = t.Union[
src/flask/typing.py:L85: ErrorHandlerCallable = t.Union[
src/flask/typing.py:L27: HeaderValue = t.Union[str, list[str], tuple[str, ...]]
src/flask/typing.py:L30: HeadersValue = t.Union[
src/flask/typing.py:L48: ResponseClass = t.TypeVar("ResponseClass", bound="Response")
src/flask/typing.py:L37: ResponseReturnValue = t.Union[
src/flask/typing.py:L12: ResponseValue = t.Union[
src/flask/typing.py:L90: RouteCallable = t.Union[
src/flask/typing.py:L62: ShellContextProcessorCallable = t.Callable[[], dict[str, t.Any]]
src/flask/typing.py:L63: TeardownCallable = t.Union[
src/flask/typing.py:L67: TemplateContextProcessorCallable = t.Union[
src/flask/typing.py:L71: TemplateFilterCallable = t.Callable[..., t.Any]
src/flask/typing.py:L72: TemplateGlobalCallable = t.Callable[..., t.Any]
src/flask/typing.py:L73: TemplateTestCallable = t.Callable[..., bool]
src/flask/typing.py:L74: URLDefaultCallable = t.Callable[[str, dict[str, t.Any]], None]
src/flask/typing.py:L75: URLValuePreprocessorCallable = t.Callable[
src/flask/json/__init__.py:L47: def dump(obj: t.Any, fp: t.IO[str], **kwargs: t.Any) -> None:
src/flask/json/provider.py:L49: def dump(self, obj: t.Any, fp: t.IO[str], **kwargs: t.Any) -> None:
src/flask/app.py:L534: def make_shell_context(self) -> dict[str, t.Any]:
src/flask/cli.py:L788: class CertParamType(click.ParamType):
src/flask/cli.py:L531: class FlaskGroup(AppGroup):
src/flask/cli.py:L120: def find_app_by_string(module: ModuleType, app_name: str) -> Flask:
src/flask/cli.py:L41: def find_best_app(module: ModuleType) -> Flask:
src/flask/cli.py:L665: def make_context(
src/flask/cli.py:L686: def parse_args(self, ctx: click.Context, args: list[str]) -> list[str]:
src/flask/cli.py:L380: def with_appcontext(f: F) -> F:
src/flask/app.py:L506: def update_template_context(self, context: dict[str, t.Any]) -> None:
src/flask/sansio/app.py:L597: def iter_blueprints(self) -> t.ValuesView[Blueprint]:
src/flask/templating.py:L60: def get_source(
src/flask/templating.py:L111: def list_templates(self) -> list[str]:
src/flask/helpers.py:L635: def _split_blueprint_path(name: str) -> list[str]:
src/flask/json/provider.py:L89: def response(self, *args: t.Any, **kwargs: t.Any) -> Response:
src/flask/json/provider.py:L189: def response(self, *args: t.Any, **kwargs: t.Any) -> Response:
src/flask/app.py:L980: def async_to_sync(
src/flask/app.py:L879: def dispatch_request(self) -> ft.ResponseReturnValue:
src/flask/app.py:L904: def full_dispatch_request(self) -> Response:
src/flask/app.py:L811: def handle_exception(self, e: Exception) -> Response:
src/flask/app.py:L744: def handle_http_exception(
src/flask/app.py:L779: def handle_user_exception(
src/flask/app.py:L864: def log_exception(
src/flask/app.py:L953: def make_default_options_response(self) -> Response:
src/flask/app.py:L1271: def preprocess_request(self) -> ft.ResponseReturnValue | None:
src/flask/app.py:L1298: def process_response(self, response: Response) -> Response:
src/flask/app.py:L478: def raise_routing_exception(self, request: Request) -> t.NoReturn:
src/flask/app.py:L308: def send_static_file(self, filename: str) -> Response:
src/flask/app.py:L1479: def wsgi_app(
src/flask/blueprints.py:L82: def send_static_file(self, filename: str) -> Response:
src/flask/ctx.py:L238: class AppContext:
src/flask/ctx.py:L287: class RequestContext:
src/flask/debughelpers.py:L50: class FormDataRoutingRedirect(AssertionError):
src/flask/sansio/app.py:L932: def handle_url_build_error(
src/flask/sansio/app.py:L911: def inject_url_defaults(self, endpoint: str, values: dict[str, t.Any]) -> None:
src/flask/sansio/app.py:L883: def should_ignore_error(self, error: BaseException | None) -> bool:
src/flask/sansio/app.py:L848: def trap_http_exception(self, e: Exception) -> bool:
src/flask/sessions.py:L298: class SecureCookieSessionInterface(SessionInterface):
src/flask/views.py:L78: def dispatch_request(self) -> ft.ResponseReturnValue:
src/flask/views.py:L182: def dispatch_request(self, **kwargs: t.Any) -> ft.ResponseReturnValue:
src/flask/testing.py:L204: def open(
src/flask/app.py:L1423: def test_request_context(self, *args: t.Any, **kwargs: t.Any) -> RequestContext:
src/flask/debughelpers.py:L124: def explain_template_loading_attempts(
src/flask/sansio/app.py:L523: def create_global_jinja_loader(self) -> DispatchingJinjaLoader:
src/flask/helpers.py:L394: def _prepare_send_file_kwargs(**kwargs: t.Any) -> dict[str, t.Any]:
src/flask/sansio/scaffold.py:L284: def _method_route(
src/flask/app.py:L1003: def url_for(
src/flask/helpers.py:L249: def redirect(
