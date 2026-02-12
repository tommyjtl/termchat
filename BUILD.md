# Building and Publishing TermQ to PyPI

## Development Installation

Install in development mode (editable):
```bash
pip install -e .
```

This allows you to make changes to the code and test them immediately without reinstalling.

## Building the Package

1. Install build tools:
```bash
pip install build twine
```

2. Build the distribution packages:
```bash
rm -rf dist/* && python -m build
```

This creates:
- `dist/termq-0.1.0-py3-none-any.whl` (wheel)
- `dist/termq-0.1.0.tar.gz` (source distribution)

## Testing the Package Locally

Before publishing, test installation:
```bash
pip install dist/termq-0.1.0-py3-none-any.whl
```

Test the commands:
```bash
termq --help
termq --pdf --help
```

## Publishing to PyPI

### Test PyPI (recommended first)

1. Create account at https://test.pypi.org/
2. Upload to Test PyPI:
```bash
python -m twine upload --repository termq dist/*
```

3. Install from Test PyPI to verify:
```bash
pip install --index-url https://test.pypi.org/simple/ termq
```

### Production PyPI

1. Create account at https://pypi.org/
2. Upload to PyPI:
```bash
python -m twine upload dist/*
```

3. Install from PyPI:
```bash
pip install termq
```

## Usage After Installation

Once installed via pip, users can run:

```bash
# Chat mode (default)
termq
termq -c characters/hal9000.json
termq --stream
termq -q  # direct question mode

# PDF mode
termq --pdf -f document.pdf
termq --pdf -f document.pdf --ocr
```

## Version Updates

1. Update version in `pyproject.toml`
2. Update version in `termq/__init__.py`
3. Rebuild and republish

## Environment Variables

Users still need to set:
```bash
export OPENAI_API_KEY=<your key>
```
