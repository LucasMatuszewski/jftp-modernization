# Repository map

src/legacy-repo-map/src/policy.rs:L125: pub fn file_name(relative: &str) -> &str {
src/legacy-repo-map/src/policy.rs:L118: pub fn suffix_lower(name: &str) -> String {
src/legacy-repo-map/src/rank.rs:L433: fn assert_limit(files: &[(&str, Vec<Tag>)], max_edges: usize) {
src/legacy-repo-map/src/policy.rs:L278: fn class_match(pattern: &[char], start: usize, candidate: char) -> Option<(bool, usize)> {
src/legacy-repo-map/src/policy.rs:L164: fn has_secret_word(name: &str) -> bool {
src/legacy-repo-map/src/policy.rs:L189: pub fn safe_relative(relative: &str) -> Result<String, String> {
src/legacy-repo-map/tests/cli.rs:L77: fn map_text(&self) -> String {
src/legacy-repo-map/src/tags.rs:L11: macro_rules! vendored_query {
src/legacy-repo-map/src/rank.rs:L118: pub fn rank_definitions<'a>(
src/legacy-repo-map/tests/cli.rs:L50: fn write_bytes(&self, relative: &str, content: &[u8]) {
src/legacy-repo-map/tests/cli.rs:L56: fn map(&self, extra: &[&str]) -> Output {
src/legacy-repo-map/src/main.rs:L316: fn write_atomic(directory: &Path, name: &str, content: &str) -> Result<(), String> {
src/legacy-repo-map/tests/cli.rs:L348: fn byte_directory(parent: &Path, name: &[u8]) -> Option<PathBuf> {
src/legacy-repo-map/src/inventory.rs:L54: pub fn sha256_hex(data: &[u8]) -> String {
src/legacy-repo-map/tests/cli.rs:L735: fn assert_control_paths_are_skipped(fixture: &Fixture, git: bool) {
src/legacy-repo-map/tests/cli.rs:L93: fn git_commit(&self) -> bool {
src/legacy-repo-map/src/inventory.rs:L63: fn git_command(root: &Path) -> Command {
src/legacy-repo-map/src/inventory.rs:L201: fn os_reason(error: &std::io::Error) -> String {
src/legacy-repo-map/src/inventory.rs:L497: fn python_name_sort_key(name: &OsStr) -> Vec<u32> {
src/legacy-repo-map/src/inventory.rs:L522: fn python_name_sort_key(name: &OsStr) -> Vec<u32> {
src/legacy-repo-map/src/inventory.rs:L536: fn python_name_sort_key(name: &OsStr) -> Vec<u32> {
src/legacy-repo-map/src/inventory.rs:L291: pub fn safe_path_display(path: &str) -> String {
src/legacy-repo-map/src/inventory.rs:L91: fn git_output(root: &Path, args: &[&str]) -> Option<Vec<u8>> {
src/legacy-repo-map/src/inventory.rs:L96: fn git_text(root: &Path, args: &[&str]) -> Option<String> {
src/legacy-repo-map/src/inventory.rs:L211: fn open_regular(path: &Path) -> std::io::Result<File> {
src/legacy-repo-map/src/inventory.rs:L220: fn open_regular(path: &Path) -> std::io::Result<File> {
src/legacy-repo-map/src/inventory.rs:L354: fn next(&mut self) -> Option<Candidate> {
src/legacy-repo-map/src/inventory.rs:L572: fn next(&mut self) -> Result<Option<Candidate>, String> {
src/legacy-repo-map/src/inventory.rs:L657: fn next(&mut self) -> Result<Option<Candidate>, String> {
src/legacy-repo-map/src/main.rs:L167: fn parse_arguments(raw: Vec<String>) -> Result<Invocation, String> {
src/legacy-repo-map/src/tags.rs:L128: pub struct Extractor {
src/legacy-repo-map/src/tags.rs:L132: pub fn spec_for(language: &str) -> Option<(usize, &'static LanguageSpec)> {
src/legacy-repo-map/tests/cli.rs:L81: fn json(&self, name: &str) -> Value {
src/legacy-repo-map/tests/cli.rs:L46: fn write(&self, relative: &str, content: &str) {
src/legacy-repo-map/src/inventory.rs:L651: enum Candidates {
src/legacy-repo-map/src/inventory.rs:L324: struct GitCandidates {
src/legacy-repo-map/src/inventory.rs:L406: struct IgnoreChain {
src/legacy-repo-map/src/inventory.rs:L542: struct WalkCandidates {
src/legacy-repo-map/src/inventory.rs:L110: fn git_state(root: &Path) -> Result<GitState, String> {
src/legacy-repo-map/src/inventory.rs:L283: fn has_control_character(path: &str) -> bool {
src/legacy-repo-map/src/inventory.rs:L308: fn in_subtrees(relative: &str, subtrees: &[String]) -> bool {
src/legacy-repo-map/src/inventory.rs:L453: fn read_gitignore(directory: &Path, total_bytes: &mut u64) -> Result<Option<String>, String> {
src/legacy-repo-map/src/inventory.rs:L226: pub fn read_safe(root: &Path, relative: &str, max_file_bytes: u64) -> Result<(Vec<u8>, String), String> {
src/legacy-repo-map/src/main.rs:L336: fn python_strip(text: &str) -> &str {
src/legacy-repo-map/src/main.rs:L276: fn resolve_lenient(path: &Path) -> Result<PathBuf, String> {
src/legacy-repo-map/tests/cli.rs:L66: fn map_ok(&self, extra: &[&str]) -> Value {
src/legacy-repo-map/src/rank.rs:L47: fn py_sum(values: impl Iterator<Item = f64>) -> f64 {
src/legacy-repo-map/tests/cli.rs:L147: fn snapshot(root: &Path) -> BTreeMap<String, String> {
src/legacy-repo-map/src/rank.rs:L423: fn unreferenced() -> Vec<(&'static str, Vec<Tag>)> {
src/legacy-repo-map/src/main.rs:L364: fn run(arguments: Arguments) -> Result<String, String> {
src/legacy-repo-map/src/main.rs:L100: macro_rules! vendored {
src/legacy-repo-map/src/rank.rs:L319: fn capped(
src/legacy-repo-map/src/rank.rs:L332: fn fixture() -> Vec<(&'static str, Vec<Tag>)> {
src/legacy-repo-map/src/rank.rs:L411: fn mixed() -> Vec<(&'static str, Vec<Tag>)> {
src/legacy-repo-map/src/tags.rs:L185: pub fn extract(&mut self, language: &str, path: &str, source: &[u8]) -> Result<FileTags, ExtractError> {
src/legacy-repo-map/tests/cli.rs:L123: fn git(&self, arguments: &[&str]) -> bool {
src/legacy-repo-map/tests/cli.rs:L85: fn artifacts(&self) -> String {
src/legacy-repo-map/src/rank.rs:L75: fn pagerank(out: &[Vec<Edge>], personalization: &[(usize, f64)]) -> Option<Vec<f64>> {
src/legacy-repo-map/src/rank.rs:L66: fn stem(name: &str) -> &str {
src/legacy-repo-map/src/inventory.rs:L412: fn load(
src/legacy-repo-map/src/tags.rs:L143: fn load(spec: &LanguageSpec) -> Result<Loaded, String> {
src/legacy-repo-map/src/tags.rs:L230: fn names(language: &str, source: &str, kind: Kind) -> Vec<(usize, String)> {
src/legacy-repo-map/src/main.rs:L188: fn number<T: std::str::FromStr>(name: &str, text: String) -> Result<T, String> {
src/legacy-repo-map/src/inventory.rs:L434: fn ignored(&self, path: &Path, is_dir: bool) -> bool {
src/legacy-repo-map/tests/cli.rs:L19: struct Fixture {
src/legacy-repo-map/tests/cli.rs:L170: fn paths(value: &Value) -> Vec<String> {
src/legacy-repo-map/tests/cli.rs:L142: fn sha256(data: &[u8]) -> String {
src/legacy-repo-map/src/main.rs:L215: fn notices() -> String {
src/legacy-repo-map/src/inventory.rs:L388: fn finish(mut self, completed: bool) -> Result<(), String> {
src/legacy-repo-map/src/inventory.rs:L564: fn selected(&self, relative: &Path, is_directory: bool) -> bool {
src/legacy-repo-map/src/main.rs:L264: fn pretty(value: &Value) -> String {
src/legacy-repo-map/src/main.rs:L343: fn snippet(line: &str) -> String {
src/legacy-repo-map/src/policy.rs:L183: pub fn cli_relative(relative: &str) -> Result<String, String> {
src/legacy-repo-map/src/policy.rs:L218: pub fn fnmatch(name: &str, pattern: &str) -> bool {
src/legacy-repo-map/src/policy.rs:L314: fn fnmatch_follows_python_semantics() {
src/legacy-repo-map/src/policy.rs:L150: pub fn is_secret(relative: &str) -> bool {
src/legacy-repo-map/src/policy.rs:L137: pub fn kind_for(relative: &str, language: Option<&str>) -> &'static str {
src/legacy-repo-map/src/policy.rs:L129: pub fn language_for(relative: &str) -> Option<&'static str> {
src/legacy-repo-map/src/policy.rs:L371: fn relative_paths_are_bounded() {
src/legacy-repo-map/src/policy.rs:L330: fn secret_and_kind_classification() {
src/legacy-repo-map/src/policy.rs:L174: pub fn secret_name_pattern() -> String {
src/legacy-repo-map/src/policy.rs:L310: mod tests {
src/legacy-repo-map/src/rank.rs:L40: struct Edge {
src/legacy-repo-map/src/rank.rs:L28: pub struct RankFile<'a> {
src/legacy-repo-map/src/rank.rs:L34: pub struct RankedDefinition<'a> {
src/legacy-repo-map/src/rank.rs:L471: fn compensated_sum_matches_cpython() {
src/legacy-repo-map/src/rank.rs:L442: fn edge_limit_covers_a_self_edge_after_a_referenced_identifier() {
src/legacy-repo-map/src/rank.rs:L449: fn edge_limit_covers_definitions_that_are_never_referenced() {
src/legacy-repo-map/src/rank.rs:L402: fn edge_limit_is_reported() {
src/legacy-repo-map/src/rank.rs:L458: fn exact_edge_limit_is_accepted_and_keeps_the_order() {
src/legacy-repo-map/src/rank.rs:L371: fn focus_symbol_and_focus_file_move_to_the_front() {
src/legacy-repo-map/src/rank.rs:L313: fn order(files: &[(&str, Vec<Tag>)], focus_files: &[&str], focus_symbols: &[&str]) -> Vec<String> {
src/legacy-repo-map/src/rank.rs:L356: fn order_matches_the_python_reference() {
src/legacy-repo-map/src/rank.rs:L397: fn ranking_is_deterministic() {
src/legacy-repo-map/src/rank.rs:L305: fn tag(line: usize, kind: Kind, name: &str) -> Tag {
src/legacy-repo-map/src/rank.rs:L302: mod tests {
src/legacy-repo-map/tests/cli.rs:L1188: fn a_directory_ignored_by_an_enclosing_repository_is_still_mapped() {
src/legacy-repo-map/tests/cli.rs:L1164: fn a_safety_limit_fails_the_run_and_replaces_the_previous_map() {
src/legacy-repo-map/tests/cli.rs:L1010: fn broken_source_is_reported_and_partially_mapped() {
src/legacy-repo-map/tests/cli.rs:L556: fn budget_is_enforced_with_the_declared_estimator() {
src/legacy-repo-map/tests/cli.rs:L783: fn control_characters_in_paths_are_skipped_and_escaped() {
src/legacy-repo-map/tests/cli.rs:L953: fn crlf_unicode_paths_and_several_languages() {
src/legacy-repo-map/tests/cli.rs:L1130: fn definitions_on_one_source_line_produce_one_map_line() {
src/legacy-repo-map/tests/cli.rs:L910: fn descriptors_and_unsupported_files_stay_visible_without_fake_symbols() {
src/legacy-repo-map/tests/cli.rs:L1020: fn directory_walk_honors_gitignore_files_without_git() {
src/legacy-repo-map/tests/cli.rs:L854: fn file_and_size_limits_are_explicit() {
src/legacy-repo-map/tests/cli.rs:L581: fn focus_keeps_requested_definitions_first_and_reports_absent_names() {
src/legacy-repo-map/tests/cli.rs:L1049: fn git_selection_revision_and_dirty_state() {
src/legacy-repo-map/tests/cli.rs:L292: fn inventory_hashes_are_the_current_bytes_and_the_fingerprint_tracks_content() {
src/legacy-repo-map/tests/cli.rs:L1145: fn inventory_only_lists_files_without_a_symbol_map() {
src/legacy-repo-map/tests/cli.rs:L39: fn java() -> Self {
src/legacy-repo-map/tests/cli.rs:L669: fn links_are_not_followed_out_of_or_around_the_source() {
src/legacy-repo-map/tests/cli.rs:L231: fn literal_backslash_paths_keep_distinct_current_byte_identities() {
src/legacy-repo-map/tests/cli.rs:L198: fn maps_definitions_with_original_paths_and_lines() {
src/legacy-repo-map/tests/cli.rs:L26: fn new() -> Self {
src/legacy-repo-map/tests/cli.rs:L361: fn non_utf8_directories_count_leaves_and_enforce_file_cap() {
src/legacy-repo-map/tests/cli.rs:L403: fn non_utf8_directory_scoping_ignores_and_links_use_raw_paths() {
src/legacy-repo-map/tests/cli.rs:L507: fn optional_debug_tags_are_current_or_absent_on_every_run() {
src/legacy-repo-map/tests/cli.rs:L801: fn output_inside_the_source_is_refused_before_anything_is_written() {
src/legacy-repo-map/tests/cli.rs:L823: fn output_links_cannot_redirect_writes_into_the_source() {
src/legacy-repo-map/tests/cli.rs:L329: fn repeated_runs_are_byte_identical_and_leave_the_source_untouched() {
src/legacy-repo-map/tests/cli.rs:L1092: fn repository_configured_commands_are_not_executed() {
src/legacy-repo-map/tests/cli.rs:L621: fn secrets_binaries_and_oversized_files_are_listed_but_never_read() {
src/legacy-repo-map/tests/cli.rs:L179: fn skip_reason(inventory: &Value, path: &str) -> Option<String> {
src/legacy-repo-map/tests/cli.rs:L267: fn source_snippet_controls_are_sanitized_without_changing_bytes_or_lines() {
src/legacy-repo-map/tests/cli.rs:L696: fn special_files_do_not_block_the_scan() {
src/legacy-repo-map/tests/cli.rs:L188: fn strings(value: &Value) -> Vec<String> {
src/legacy-repo-map/tests/cli.rs:L878: fn subtree_exclusion_and_escape_attempts() {
src/legacy-repo-map/tests/cli.rs:L442: fn unmerged_non_utf8_paths_are_deduplicated_before_decoding() {
src/legacy-repo-map/tests/cli.rs:L542: fn unremovable_old_debug_tags_prevent_complete_publication() {
src/legacy-repo-map/tests/cli.rs:L985: fn unusual_line_separators_do_not_break_map_lines() {
src/legacy-repo-map/tests/cli.rs:L1221: fn usage_errors_and_informational_flags() {
src/legacy-repo-map/src/tags.rs:L173: pub enum ExtractError {
src/legacy-repo-map/src/tags.rs:L114: pub struct FileTags {
src/legacy-repo-map/src/tags.rs:L102: pub enum Kind {
src/legacy-repo-map/src/tags.rs:L20: pub struct LanguageSpec {
src/legacy-repo-map/src/tags.rs:L120: struct Loaded {
src/legacy-repo-map/src/tags.rs:L108: pub struct Tag {
src/legacy-repo-map/src/tags.rs:L320: fn broken_source_is_flagged_and_still_tagged() {
src/legacy-repo-map/src/tags.rs:L311: fn crlf_and_non_ascii_sources_keep_line_numbers() {
src/legacy-repo-map/src/tags.rs:L269: fn each_language_yields_a_real_definition() {
src/legacy-repo-map/src/tags.rs:L243: fn every_vendored_query_compiles_against_its_pinned_grammar() {
src/legacy-repo-map/src/tags.rs:L252: fn java_definitions_and_references_keep_original_lines() {
src/legacy-repo-map/src/tags.rs:L179: pub fn new() -> Self {
src/legacy-repo-map/src/tags.rs:L330: fn per_file_tag_limit_stops_the_run() {
src/legacy-repo-map/src/tags.rs:L139: pub fn query_sha256(spec: &LanguageSpec) -> String {
src/legacy-repo-map/src/tags.rs:L227: mod tests {
src/legacy-repo-map/src/inventory.rs:L319: enum Candidate {
src/legacy-repo-map/src/inventory.rs:L22: pub struct FileEntry {
src/legacy-repo-map/src/inventory.rs:L100: struct GitState {
src/legacy-repo-map/src/inventory.rs:L35: pub struct Inventory {
src/legacy-repo-map/src/inventory.rs:L47: pub struct ScanOptions<'a> {
src/legacy-repo-map/src/inventory.rs:L30: pub struct Skip {
src/legacy-repo-map/src/inventory.rs:L549: enum WalkStep {
src/legacy-repo-map/src/inventory.rs:L785: fn control_characters_are_detected_like_the_python_tool() {
src/legacy-repo-map/src/inventory.rs:L856: fn non_utf8_directory_descendants_consume_discovery_budget() {
src/legacy-repo-map/src/inventory.rs:L829: fn non_utf8_name_order_matches_python_surrogateescape() {
src/legacy-repo-map/src/inventory.rs:L844: fn non_utf8_name_order_preserves_windows_surrogates() {
src/legacy-repo-map/src/inventory.rs:L807: fn path_display_is_escaped_and_reversible() {
src/legacy-repo-map/src/inventory.rs:L667: pub fn scan<F>(root: &Path, options: &ScanOptions, mut visit: F) -> Result<Inventory, String>
src/legacy-repo-map/src/inventory.rs:L332: fn start(root: &Path, subtrees: &[String]) -> Result<Self, String> {
src/legacy-repo-map/src/inventory.rs:L555: fn start(root: &Path, subtrees: &[String]) -> Self {
src/legacy-repo-map/src/inventory.rs:L781: mod tests {
src/legacy-repo-map/src/inventory.rs:L892: fn walk_prunes_unselected_directories_before_descent() {
src/legacy-repo-map/src/inventory.rs:L908: fn walk_refuses_aggregate_ignore_bytes() {
src/legacy-repo-map/src/inventory.rs:L875: fn walk_refuses_excess_discovery_and_oversized_ignore_files() {
src/legacy-repo-map/src/main.rs:L147: struct Arguments {
src/legacy-repo-map/src/main.rs:L162: enum Invocation {
src/legacy-repo-map/src/main.rs:L357: struct ParsedFile {
src/legacy-repo-map/src/main.rs:L269: fn display(path: &Path) -> String {
src/legacy-repo-map/src/main.rs:L5: mod inventory;
src/legacy-repo-map/src/main.rs:L844: fn main() -> ExitCode {
src/legacy-repo-map/src/main.rs:L876: fn notices_print_every_pinned_text_in_full() {
src/legacy-repo-map/src/main.rs:L955: fn option_parsing_accepts_both_value_forms() {
src/legacy-repo-map/src/main.rs:L6: mod policy;
src/legacy-repo-map/src/main.rs:L223: fn policy_json() -> String {
src/legacy-repo-map/src/main.rs:L7: mod rank;
src/legacy-repo-map/src/main.rs:L867: fn reported_dependency_versions_match_the_lockfile() {
src/legacy-repo-map/src/main.rs:L934: fn snippets_stay_on_one_line() {
src/legacy-repo-map/src/main.rs:L927: fn strip_matches_python() {
src/legacy-repo-map/src/main.rs:L8: mod tags;
src/legacy-repo-map/src/main.rs:L863: mod tests {
