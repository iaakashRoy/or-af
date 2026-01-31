# PyPI Publishing Checklist

## ✅ Package Configuration (COMPLETED)
- [x] Correct GitHub repository URLs in pyproject.toml and setup.py
- [x] Valid license configuration (MIT)
- [x] Author information with email
- [x] Proper classifiers for Python versions
- [x] Dependencies correctly specified
- [x] MANIFEST.in configured
- [x] .gitignore excludes build artifacts
- [x] Package builds successfully
- [x] Package installs correctly

## 📋 Before First Publication

### 1. Create PyPI Account
- Create account at https://pypi.org/account/register/
- Verify email address

### 2. Set Up Trusted Publishing (Recommended)
This is the most secure method and doesn't require API tokens.

1. Go to https://pypi.org/manage/account/publishing/
2. Add a new publisher with these details:
   - **PyPI Project Name**: `or-af`
   - **Owner**: `iaakashRoy`
   - **Repository name**: `or-af`
   - **Workflow name**: `publish.yml`
   - **Environment name**: (leave blank)

### Alternative: API Token Method
If not using trusted publishing:

1. Generate API token at https://pypi.org/manage/account/token/
2. Add as GitHub secret: `PYPI_API_TOKEN`
3. Update workflow to use token authentication

## 🚀 Publishing Steps

### Option 1: GitHub Release (Automated - Recommended)
1. Go to GitHub repository → Releases → Draft a new release
2. Create new tag: `v0.1.0`
3. Release title: `v0.1.0 - Initial Release`
4. Add release notes from CHANGELOG.md
5. Click "Publish release"
6. GitHub Actions will automatically build and publish to PyPI

### Option 2: Manual Publishing
```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build

# Check the distribution
twine check dist/*

# Upload to Test PyPI (optional but recommended)
twine upload --repository testpypi dist/*

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ or-af

# Upload to PyPI
twine upload dist/*
```

## 🧪 Testing After Publication

```bash
# Install from PyPI
pip install or-af

# Verify installation
python -c "import or_af; print(or_af.__version__)"

# Test basic functionality
python examples/simple_example.py
```

## 📊 Package Status

**Current Version**: 0.1.0
**Package Name**: or-af
**Repository**: https://github.com/iaakashRoy/or-af
**PyPI URL (after publishing)**: https://pypi.org/project/or-af/

## ⚠️ Important Notes

1. **Version Numbers**: Once a version is published to PyPI, it cannot be changed. Always increment version for updates.
2. **Package Name**: `or-af` is unique on PyPI and available for registration.
3. **Testing**: Always test on TestPyPI before publishing to production PyPI.
4. **Trusted Publishing**: This is the recommended method as of 2024+ for security.

## 🔄 For Future Updates

1. Update version in:
   - `pyproject.toml`
   - `setup.py`
   - `or_af/__init__.py`
2. Update CHANGELOG.md
3. Commit changes
4. Create new release on GitHub with new version tag
5. GitHub Actions will automatically publish

## 📚 Resources

- [PyPI Documentation](https://pypi.org/help/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Trusted Publishing Guide](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions for PyPI](https://github.com/marketplace/actions/pypi-publish)
