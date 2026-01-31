# How to Publish or-af to PyPI

## Current Status

✅ **Package is ready for publication!**

- Package configuration is correct
- Build process works successfully  
- Trusted publisher is configured on PyPI
- GitHub Actions workflow is set up correctly

## Why the Package is Not Available Yet

The `or-af` package has not been published to PyPI yet. This is why you're seeing:
```
ERROR: Could not find a version that satisfies the requirement or-af (from versions: none)
ERROR: No matching distribution found for or-af
```

## Solution: Create a GitHub Release

You have already configured the **trusted publisher** on PyPI (pending publisher). Now you need to create a GitHub release to trigger the automated publishing workflow.

### Steps to Publish:

1. **Go to your GitHub repository**: https://github.com/iaakashRoy/or-af

2. **Navigate to Releases**:
   - Click on "Releases" in the right sidebar
   - Or go directly to: https://github.com/iaakashRoy/or-af/releases

3. **Create a new release**:
   - Click "Draft a new release" or "Create a new release"
   
4. **Configure the release**:
   - **Choose a tag**: Create a new tag `v0.1.0`
   - **Release title**: `v0.1.0 - Initial Release`
   - **Description**: Add release notes from CHANGELOG.md or write:
     ```
     First release of OR-AF (Operations Research Agentic Framework)
     
     Features:
     - Lightweight framework for creating AI agents
     - Tool-calling capabilities
     - Streaming support
     - Comprehensive observability
     ```
   
5. **Publish the release**:
   - Click "Publish release"
   - This will automatically trigger the GitHub Actions workflow

6. **Monitor the workflow**:
   - Go to the "Actions" tab in your repository
   - You should see "Publish to PyPI" workflow running
   - Wait for it to complete (usually takes 1-2 minutes)

7. **Verify publication**:
   - Once the workflow completes successfully, your package will be on PyPI!
   - Visit: https://pypi.org/project/or-af/
   - Install with: `pip install or-af`

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

## Troubleshooting

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
