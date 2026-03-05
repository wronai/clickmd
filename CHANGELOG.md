# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-07

### Added
- Initial release
- `md()` function for markdown rendering
- `echo()` smart function with auto-detection
- `MarkdownRenderer` class for advanced usage
- Syntax highlighting for:
  - Python (keywords, decorators, strings, comments)
  - TypeScript/JavaScript (keywords, strings, template literals)
  - JSON (keys, values, numbers, booleans)
  - YAML (keys, values, comments, lists)
  - Bash/Shell (commands, comments)
  - Markdown (headers, bold, links)
  - Log (status emojis, errors, warnings)
- Click decorators re-export (optional dependency)
- Zero-dependency core functionality
- Full test suite
- Examples and documentation

### Features
- Works without Click installed
- Auto-detects TTY for color output
- Supports custom output streams
- Type hints (py.typed marker)

## [Unreleased]

### Planned
- Table rendering
- Progress bars
- Box/panel rendering
- More language highlighters

## [1.0.2] - 2026-03-05

### Docs
- Update project/README.md
- Update project/context.md

### Other
- Update Makefile
- Update project/analysis.toon
- Update project/calls.mmd
- Update project/calls.png
- Update project/compact_flow.mmd
- Update project/compact_flow.png
- Update project/dashboard.html
- Update project/evolution.toon
- Update project/flow.mmd
- Update project/flow.png
- ... and 5 more files

## [1.0.1] - 2026-03-05

### Docs
- Update CHANGELOG.md
- Update README.md
- Update ROADMAP.md
- Update docs/API.md
- Update docs/CONTRIBUTING.md
- Update examples_output/api_response.md
- Update examples_output/basic.md
- Update examples_output/cli_app.md
- Update examples_output/cli_colors.md
- Update examples_output/config_viewer.md
- ... and 7 more files

### Test
- Update tests/__init__.py
- Update tests/test_core.py
- Update tests/test_decorators.py
- Update tests/test_logger.py
- Update tests/test_renderer.py

### Other
- Update .gitignore
- Update LICENSE
- Update Makefile
- Update __init__.py
- Update clickmd.functions.toon
- Update clickmd.toon
- Update clickmd.toon-schema.json
- Update decorators.py
- Update devtools.py
- Update examples/api_response.py
- ... and 38 more files
