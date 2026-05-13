# Contributing to clickmd

Thank you for your interest in contributing to clickmd! This document provides guidelines and instructions for contributing.

### Prerequisites

- Python 3.10 or higher
- Git

# Clone the repository
git clone https://github.com/wronai/clickmd.git
cd clickmd

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# Install development dependencies
pip install -e ".[dev,click]"
```

# Run specific test file
pytest tests/test_renderer.py -v
```

## Project Structure

```
clickmd/
├── src/clickmd/          # Package source (src layout)
│   ├── __init__.py       # Public API: md(), echo(), menu(), select()
│   ├── renderer.py       # Core markdown renderer & syntax highlighting
│   ├── decorators.py     # Click decorator re-exports
│   ├── help.py           # Markdown help formatter for Click
│   ├── logger.py         # Markdown-aware structured logger
│   ├── progress.py       # Progress bars, spinners, live updates
│   ├── themes.py         # Color themes & NO_COLOR support
│   ├── devtools.py       # Debug, inspect, diff, tree tools
│   ├── rich_backend.py   # Optional Rich integration
│   └── py.typed          # PEP 561 type marker
├── tests/
│   ├── test_renderer.py
│   ├── test_core.py
│   ├── test_decorators.py
│   └── test_logger.py
├── examples/             # 17 demo scripts
├── docs/
│   ├── API.md
│   └── CONTRIBUTING.md
├── pyproject.toml        # Project config (hatchling)
├── Makefile
└── README.md
```

### Style

- Follow PEP 8
- Use type hints for all function signatures
- Maximum line length: 100 characters
- Use `ruff` for linting and formatting

### Documentation

- All public functions need docstrings
- Update README.md for new features
- Add examples for new functionality

### Testing

- Write tests for all new features
- Maintain >80% code coverage
- Test both with and without Click installed

## Adding New Syntax Highlighting

To add highlighting for a new language:

1. Add detection in `_highlight_line()`:

```python
def _highlight_line(self, lang: str, line: str) -> str:
    l = (lang or "text").lower()
    # ... existing languages ...
    if l in ("newlang", "nl"):
        return self._highlight_newlang(line)
    return self._c("white", line)
```

2. Implement the highlighter:

```python
def _highlight_newlang(self, line: str) -> str:
    # Add highlighting logic
    return result
```

3. Add tests in `tests/test_renderer.py`

4. Update documentation

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run `make check` to ensure quality
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

### PR Checklist

- [ ] Tests pass (`make test`)
- [ ] Linting passes (`make lint`)
- [ ] Type checking passes (`make type-check`)
- [ ] Documentation updated if needed
- [ ] CHANGELOG updated for notable changes

## Releasing

Releases are managed by maintainers:

```bash
# Commit and tag
git tag v1.0.1
git push --tags

## Questions?

Open an issue on GitHub or reach out to the maintainers.

Thank you for contributing! 🎉
