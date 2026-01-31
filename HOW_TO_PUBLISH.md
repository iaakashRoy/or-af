# 🚀 How to Publish or-af to PyPI

## Current Status

✅ **Package is ready for publication!**

- ✅ Package configuration is correct
- ✅ Build process works successfully (verified locally)
- ✅ Package installs correctly (tested)
- ✅ Trusted publisher is configured on PyPI (pending)
- ✅ GitHub Actions workflow is set up correctly
- ✅ All Python code is properly structured

## Why the Package is Not Available Yet

The `or-af` package has **not been published to PyPI yet**. This is why you're seeing:
```bash
pip install or-af
ERROR: Could not find a version that satisfies the requirement or-af (from versions: none)
ERROR: No matching distribution found for or-af
```

**The package doesn't exist on PyPI yet because no release has been created.**

## ✨ Solution: Create a GitHub Release

You have already configured the **trusted publisher** on PyPI (pending publisher status). Now you just need to **create a GitHub release** to trigger the automated publishing workflow.

### 📝 Step-by-Step Instructions:

#### Step 1: Navigate to Releases
1. Go to your repository: https://github.com/iaakashRoy/or-af
2. Click on "**Releases**" in the right sidebar
   - Or go directly to: https://github.com/iaakashRoy/or-af/releases

#### Step 2: Create New Release
1. Click "**Draft a new release**" (or "**Create a new release**")

#### Step 3: Configure Release Details
Fill in the following:

- **Choose a tag**: 
  - Click on "Choose a tag" dropdown
  - Type `v0.1.0` (this creates a new tag)
  - Click "**+ Create new tag: v0.1.0 on publish**"

- **Release title**: 
  ```
  v0.1.0 - Initial Release
  ```

- **Description**: Copy and paste this:
  ```markdown
  ## 🎉 First Release of OR-AF
  
  Operations Research Agentic Framework - A lightweight framework for creating AI agents with tool-calling capabilities.
  
  ### Features
  - 🔧 Easy tool registration with automatic schema generation
  - 📊 Full observability with custom callbacks
  - 🌊 Real-time streaming of agent responses
  - 📝 Comprehensive logging (console and file)
  - ✅ Type safety with Pydantic
  - ⚡ Minimal dependencies, maximum performance
  - 🎯 Simple, intuitive API
  
  ### Installation
  ```bash
  pip install or-af
  ```
  
  ### Requirements
  - Python 3.8+
  - openai >= 1.0.0
  - python-dotenv >= 1.0.0
  - pydantic >= 2.0.0
  
  See the [README](https://github.com/iaakashRoy/or-af#readme) for quick start guide and examples.
  ```

- **Set as the latest release**: ✅ (checked)
- **Set as a pre-release**: ⬜ (unchecked)

#### Step 4: Publish! 🚀
1. Click the green "**Publish release**" button
2. This automatically triggers the GitHub Actions workflow

#### Step 5: Monitor Progress
1. Go to the "**Actions**" tab: https://github.com/iaakashRoy/or-af/actions
2. You'll see "**Publish to PyPI**" workflow running
3. Click on it to see real-time logs
4. Wait 1-2 minutes for it to complete ⏱️

#### Step 6: Verify Success! 🎊
Once the workflow shows a green checkmark:

1. Visit your package: https://pypi.org/project/or-af/
2. Test installation:
   ```bash
   pip install or-af
   ```
3. Verify it works:
   ```bash
   python -c "import or_af; print(or_af.__version__)"
   # Should print: 0.1.0
   ```

**Congratulations! Your package is now live on PyPI!** 🎉

## How It Works

Your setup uses **PyPI Trusted Publishing**:

1. ✅ You created a **pending publisher** on PyPI with these settings:
   - Project name: `or-af`
   - Owner: `iaakashRoy`
   - Repository: `or-af`
   - Workflow: `publish.yml`

2. ✅ The GitHub Actions workflow (`.github/workflows/publish.yml`) is configured with:
   - Trigger: Runs when a release is published
   - Permissions: `id-token: write` for OIDC authentication
   - Action: Uses `pypa/gh-action-pypi-publish@release/v1`

3. When you create a release:
   - GitHub Actions workflow runs automatically
   - Builds the package
   - Authenticates to PyPI using OpenID Connect (no API tokens needed!)
   - Publishes to PyPI
   - The "pending publisher" becomes a regular trusted publisher

## Alternative: Manual Workflow Trigger

If you prefer not to create a release, you can manually trigger the workflow:

1. Go to: https://github.com/iaakashRoy/or-af/actions/workflows/publish.yml
2. Click "Run workflow"
3. Select the branch (usually `main`)
4. Click "Run workflow"

**Note**: This requires that you merge your changes to the main branch first.

## 🔧 Troubleshooting

### "ERROR: No matching distribution found for or-af"

**This is the error you're currently seeing.** It's normal and expected because:
- The package hasn't been published yet
- Once you create the release (see above), this error will go away
- After publication, `pip install or-af` will work perfectly

### Workflow Fails with Authentication Error
- Verify the pending publisher is still configured on PyPI
- Check that the repository name, owner, and workflow name match exactly

### Package Already Exists Error
- Once published, you cannot republish the same version
- Increment the version number in:
  - `pyproject.toml`
  - `setup.py`
  - `or_af/__init__.py`

### Build Fails
- Check the Actions logs for specific errors
- Ensure all dependencies are correctly specified

## After First Publication

Once the package is published:

1. The pending publisher becomes a permanent trusted publisher
2. Future releases will automatically publish to PyPI
3. You can verify at: https://pypi.org/manage/account/publishing/

## For Future Updates

1. Update version numbers in all three files
2. Update CHANGELOG.md
3. Commit and push changes
4. Create a new release with the new version tag (e.g., `v0.1.1`)
5. GitHub Actions handles the rest!

---

**Ready to publish?** Create that release and your package will be live on PyPI in minutes! 🚀
