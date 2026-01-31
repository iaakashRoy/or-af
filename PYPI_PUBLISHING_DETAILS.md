# PyPI Publishing Details for OR-AF

This document contains the exact details you need to fill in when setting up Trusted Publishing on PyPI.

## 🔐 Trusted Publishing Configuration

Go to https://pypi.org/manage/account/publishing/ and add a new pending publisher with these details:

### Required Fields

#### PyPI Project Name (required)
```
or-af
```
**Note**: This is the project name that will be created on PyPI when the publisher is first used.

#### Owner (required)
```
iaakashRoy
```
**Note**: This is the GitHub username that owns the repository.

#### Repository name (required)
```
or-af
```
**Note**: This is the name of the GitHub repository containing the publishing workflow.

#### Workflow name (required)
```
publish.yml
```
**Note**: This is the filename of the publishing workflow located in `.github/workflows/` directory.

#### Environment name (optional but recommended)
```
pypi
```
**Note**: This is the GitHub Actions environment configured in the workflow (line 11 of `publish.yml`). Using a dedicated publishing environment is strongly recommended for security as it allows you to control which maintainers have publishing access.

---

## 📋 Additional Information

### Package Details
- **Package Name**: or-af
- **Current Version**: 0.1.0
- **Description**: Operations Research Agentic Framework - A lightweight framework for creating AI agents with tool-calling capabilities
- **License**: MIT
- **Python Requirements**: >=3.8

### Repository Information
- **GitHub Repository**: https://github.com/iaakashRoy/or-af
- **Workflow File Path**: `.github/workflows/publish.yml`
- **Workflow Type**: Trusted Publishing (uses OpenID Connect)

### Workflow Configuration
The workflow is configured to:
- Trigger on GitHub releases (when a release is published)
- Support manual triggers via workflow_dispatch
- Use trusted publishing (OIDC) - no API tokens needed
- Use the `pypi` environment for deployment
- Build the package using Python 3.8
- Publish using `pypa/gh-action-pypi-publish@release/v1`

---

## ✅ Setup Steps

### Step 1: Configure PyPI Trusted Publishing
1. Go to https://pypi.org/manage/account/publishing/
2. Click "Add a new pending publisher"
3. Fill in the fields with the values above
4. Click "Add"

### Step 2: Configure GitHub Environment (Already Done)
The workflow already uses the `pypi` environment. To configure access:
1. Go to your GitHub repository settings
2. Navigate to Environments → pypi
3. Configure environment protection rules as needed
4. Add required reviewers if desired

### Step 3: Publish Your First Release
1. Go to your GitHub repository
2. Click on "Releases" → "Draft a new release"
3. Create a new tag: `v0.1.0`
4. Title: `v0.1.0 - Initial Release`
5. Add release notes
6. Click "Publish release"
7. The GitHub Actions workflow will automatically build and publish to PyPI

---

## 🔑 Why Trusted Publishing?

Trusted Publishing (OpenID Connect) is the recommended method because:
- ✅ More secure - no API tokens to manage
- ✅ No secrets stored in GitHub
- ✅ PyPI verifies the workflow identity
- ✅ Automatic authentication
- ✅ Recommended by PyPI as of 2023+

---

## 📞 Support

If you encounter issues:
- Check GitHub Actions logs for the workflow run
- Verify the PyPI Trusted Publishing configuration matches exactly
- Ensure the environment name in PyPI matches the workflow
- Confirm you have necessary permissions on the GitHub repository

For more information:
- [PyPI Trusted Publishers Documentation](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions for PyPI Publishing](https://github.com/marketplace/actions/pypi-publish)
