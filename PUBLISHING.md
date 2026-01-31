# Publishing to PyPI

This guide explains how to publish the `or-af` package to PyPI.

## Prerequisites

1. Create accounts on:
   - [PyPI](https://pypi.org/account/register/) (for production releases)
   - [TestPyPI](https://test.pypi.org/account/register/) (for testing)

2. Install required tools:
   ```bash
   pip install build twine
   ```

## Step 1: Build the Package

Build both source distribution and wheel:

```bash
python -m build
```

This creates:
- `dist/or_af-0.1.0-py3-none-any.whl` (wheel distribution)
- `dist/or_af-0.1.0.tar.gz` (source distribution)

## Step 2: Test on TestPyPI (Recommended)

Before publishing to the main PyPI, test on TestPyPI:

```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Install from TestPyPI to verify
pip install --index-url https://test.pypi.org/simple/ or-af
```

## Step 3: Publish to PyPI

Once testing is successful, publish to PyPI:

```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI username and password.

## Alternative: Using API Tokens

For better security, use API tokens instead of passwords:

1. Generate an API token from PyPI:
   - Go to Account Settings → API tokens
   - Create a new token with scope for this project

2. Create a `~/.pypirc` file:
   ```ini
   [pypi]
   username = __token__
   password = pypi-AgEIcHlwaS5vcmc...your-token-here
   
   [testpypi]
   username = __token__
   password = pypi-AgEIcHlwaS5vcmc...your-token-here
   ```

3. Upload using the config:
   ```bash
   python -m twine upload dist/*
   ```

## Updating the Package

To publish a new version:

1. Update the version in `pyproject.toml` and `or_af/__init__.py`
2. Update the CHANGELOG (if you have one)
3. Clean old build artifacts:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```
4. Build the new version:
   ```bash
   python -m build
   ```
5. Upload to PyPI:
   ```bash
   python -m twine upload dist/*
   ```

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- MAJOR version: incompatible API changes
- MINOR version: new functionality (backward-compatible)
- PATCH version: bug fixes (backward-compatible)

Example: `0.1.0` → `0.1.1` (patch) → `0.2.0` (minor) → `1.0.0` (major)

## Verifying the Upload

After publishing, verify the package:

1. Check the PyPI page: https://pypi.org/project/or-af/
2. Install from PyPI: `pip install or-af`
3. Test the installation:
   ```python
   from or_af import Agent, ORFramework
   print(Agent.__doc__)
   ```

## Common Issues

### Package name already taken
If `or-af` is taken, you'll need to choose a different name. Update:
- `pyproject.toml`: `name = "your-new-name"`
- Package imports in examples and docs

### Upload fails
- Ensure version number is higher than existing versions
- Check credentials are correct
- Verify `~/.pypirc` format if using tokens

### Build errors
- Ensure all required files are included in MANIFEST.in
- Check pyproject.toml syntax
- Verify all dependencies are listed

## Resources

- [PyPI Help](https://pypi.org/help/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Twine Documentation](https://twine.readthedocs.io/)
