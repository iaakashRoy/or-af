# Publishing OR-AF to PyPI

This guide walks you through publishing the OR-AF package to PyPI.

## Prerequisites

1. **PyPI Account**: Create accounts on:
   - [PyPI](https://pypi.org/account/register/) (production)
   - [TestPyPI](https://test.pypi.org/account/register/) (testing)

2. **Install Build Tools**:
   ```bash
   pip install --upgrade build twine
   ```

## Step 1: Prepare Your Package

1. **Update Version Number**: Edit version in both `setup.py` and `pyproject.toml`

2. **Update CHANGELOG.md**: Document all changes

3. **Test Locally**:
   ```bash
   pip install -e .
   python -c "import or_af; print(or_af.__version__)"
   ```

## Step 2: Build the Package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build distribution packages
python -m build
```

This creates:
- `dist/or-af-0.1.0.tar.gz` (source distribution)
- `dist/or_af-0.1.0-py3-none-any.whl` (wheel distribution)

## Step 3: Test on TestPyPI (Optional but Recommended)

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ --no-deps or-af
```

## Step 4: Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*
```

You'll be prompted for your PyPI credentials.

## Step 5: Verify Installation

```bash
pip install or-af
python -c "import or_af; print(or_af.__version__)"
```

## Using API Tokens (Recommended)

1. Generate API token on PyPI:
   - Go to Account Settings → API tokens
   - Create a token for the project

2. Configure `.pypirc` in your home directory:
   ```ini
   [pypi]
   username = __token__
   password = pypi-your-api-token-here
   ```

3. Upload:
   ```bash
   twine upload dist/*
   ```

## GitHub Actions Automation

The repository includes GitHub Actions workflows:

1. **Automated Publishing**: `.github/workflows/publish.yml`
   - Triggers on GitHub releases
   - Automatically builds and publishes to PyPI
   - Requires `PYPI_API_TOKEN` secret in GitHub

2. **Set up GitHub Secret**:
   - Go to Repository Settings → Secrets → Actions
   - Add new secret: `PYPI_API_TOKEN`
   - Paste your PyPI API token

3. **Create a Release**:
   - Go to GitHub → Releases → Create new release
   - Tag version: `v0.1.0`
   - The workflow automatically publishes to PyPI

## Troubleshooting

### Version Already Exists
You cannot overwrite a published version. Increment the version number.

### Authentication Failed
- Check your credentials
- Use API tokens instead of password
- Verify token has correct permissions

### Missing Files in Package
- Check `MANIFEST.in`
- Ensure all necessary files are included
- Rebuild package after changes

## Checklist Before Publishing

- [ ] All tests pass
- [ ] Version number updated
- [ ] CHANGELOG.md updated
- [ ] README.md is accurate
- [ ] License file included
- [ ] Tested on TestPyPI
- [ ] Git repository is clean
- [ ] Tagged release in git

## Resources

- [PyPI Help](https://pypi.org/help/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
