# How to Monitor GitHub Actions Publishing Workflow

This guide explains how to check if the GitHub Actions automation is working after you create a release.

## 🔍 Step-by-Step: Monitoring the Workflow

### Step 1: Navigate to GitHub Actions

After creating a release on GitHub:

1. Go to your repository: https://github.com/iaakashRoy/or-af
2. Click on the **"Actions"** tab at the top of the page
3. You should see the workflow runs listed

**Direct link**: https://github.com/iaakashRoy/or-af/actions

### Step 2: Find Your Workflow Run

Look for a workflow run named **"Publish to PyPI"** with:
- **Trigger**: The release tag you just created (e.g., `v0.1.0`)
- **Status**: One of the following:
  - 🟡 **Yellow dot** = In progress (workflow is running)
  - ✅ **Green checkmark** = Success (published to PyPI!)
  - ❌ **Red X** = Failed (needs troubleshooting)

### Step 3: View Workflow Details

Click on the workflow run to see:
- **Overall status** at the top
- **Job**: "deploy" - shows the publishing job status
- **Time taken**: How long the workflow took to run

### Step 4: Check Detailed Logs

To see what happened during the workflow:

1. Click on the **"deploy"** job
2. You'll see all the steps:
   - ✅ Set up job
   - ✅ Run actions/checkout@v4
   - ✅ Set up Python
   - ✅ Install dependencies
   - ✅ Build package
   - ✅ Publish to PyPI
   - ✅ Complete job

3. Click on any step to expand and see detailed logs

### Step 5: Verify PyPI Publication

Once the workflow shows ✅ **Success**:

#### Check PyPI Website

1. Go to: https://pypi.org/project/or-af/
2. You should see your package page with:
   - Package name: **or-af**
   - Version: **0.1.0** (or your version)
   - Description and metadata

#### Test Installation

```bash
# Install the package
pip install or-af

# Verify it works
python -c "import or_af; print('Success! Package installed from PyPI')"
```

## 📊 What Each Workflow Status Means

### 🟡 In Progress (Yellow Dot)
- **What it means**: The workflow is currently running
- **What to do**: Wait 2-5 minutes for it to complete
- **Expected duration**: Usually 2-5 minutes total

### ✅ Success (Green Checkmark)
- **What it means**: Package was successfully published to PyPI!
- **What to do**: 
  1. Wait ~5 minutes for PyPI to index the package
  2. Test with `pip install or-af`
  3. Visit https://pypi.org/project/or-af/

### ❌ Failed (Red X)
- **What it means**: Something went wrong during publishing
- **What to do**: See the troubleshooting section below

## 🔧 Troubleshooting Common Issues

### Issue 1: Workflow Doesn't Start

**Symptoms**: No workflow run appears after creating a release

**Possible causes**:
- Release wasn't published (saved as draft)
- Workflow file has syntax errors

**Solution**:
1. Check the release is **published** (not draft)
2. Verify `.github/workflows/publish.yml` exists and has correct syntax

### Issue 2: "PyPI Publishing Not Configured" Error

**Symptoms**: Workflow fails with authentication error

**Example log message**:
```
Error: Failed to publish to PyPI - Trusted publishing is not configured
```

**Solution**:
1. Go to https://pypi.org/manage/account/publishing/
2. Configure Trusted Publishing with values from `PYPI_PUBLISHING_DETAILS.md`:
   - PyPI Project Name: `or-af`
   - Owner: `iaakashRoy`
   - Repository name: `or-af`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`

### Issue 3: "Package Already Exists" Error

**Symptoms**: Workflow fails when trying to upload to PyPI

**Example log message**:
```
Error: File already exists on PyPI
```

**Solution**:
- You cannot republish the same version
- Update the version number in:
  - `pyproject.toml`
  - `setup.py`
- Create a new release with the new version tag (e.g., `v0.1.1`)

### Issue 4: Build Fails

**Symptoms**: "Build package" step fails with errors

**Solution**:
1. Test the build locally:
   ```bash
   cd /path/to/or-af
   python -m pip install --upgrade build
   python -m build
   ```
2. Fix any errors shown
3. Commit and push fixes
4. Create a new release

### Issue 5: Environment Not Configured

**Symptoms**: Workflow fails with "environment not found"

**Solution**:
1. Go to repository Settings → Environments
2. Create environment named `pypi` (if it doesn't exist)
3. Configure protection rules if desired

## 📱 Getting Notifications

### Enable Email Notifications

GitHub will automatically email you when:
- ✅ Workflow succeeds
- ❌ Workflow fails

To configure:
1. Go to GitHub Settings → Notifications
2. Ensure "Actions" notifications are enabled

### Watch the Workflow in Real-Time

1. Go to the Actions tab
2. Click on the running workflow
3. Click on the "deploy" job
4. Watch the logs stream in real-time

## ✅ Checklist: Confirming Successful Publication

Use this checklist to verify everything worked:

- [ ] GitHub Actions workflow shows ✅ green checkmark
- [ ] All workflow steps completed successfully
- [ ] Package appears on PyPI: https://pypi.org/project/or-af/
- [ ] `pip install or-af` works without errors
- [ ] Package imports successfully: `import or_af`
- [ ] GitHub release shows the workflow badge as ✅

## 🕐 Timeline Expectations

| Step | Duration | What's Happening |
|------|----------|------------------|
| Create release | Instant | You publish the release on GitHub |
| Workflow starts | 5-10 seconds | GitHub Actions picks up the release event |
| Checkout code | 5-10 seconds | Downloads repository code |
| Setup Python | 10-20 seconds | Installs Python 3.8 |
| Install deps | 20-30 seconds | Installs build tools |
| Build package | 30-60 seconds | Creates wheel and source distribution |
| Publish to PyPI | 10-30 seconds | Uploads to PyPI via Trusted Publishing |
| **Total** | **2-5 minutes** | **Complete workflow** |
| PyPI indexing | 5-10 minutes | PyPI makes package available |
| **Ready to install** | **~10 minutes** | **`pip install or-af` works!** |

## 📸 Visual Guide

### Where to Find Workflow Status

```
GitHub Repository
└── Actions tab (top navigation)
    └── Workflow runs (list)
        └── "Publish to PyPI" (click to view)
            └── "deploy" job (click to view logs)
                └── Individual steps (expand to see details)
```

### Reading the Workflow Page

```
┌─────────────────────────────────────────────────────────┐
│ Publish to PyPI                                    ✅   │
│ triggered by release v0.1.0                             │
│                                                          │
│ ┌──────────────────────────────────────────────────┐   │
│ │ deploy                                      ✅   │   │
│ │ ubuntu-latest                                     │   │
│ │                                                   │   │
│ │ ✅ Set up job                          2s        │   │
│ │ ✅ Run actions/checkout@v4            3s        │   │
│ │ ✅ Set up Python                      15s       │   │
│ │ ✅ Install dependencies               25s       │   │
│ │ ✅ Build package                      45s       │   │
│ │ ✅ Publish to PyPI                    12s       │   │
│ │ ✅ Complete job                        1s        │   │
│ └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## 🎯 Quick Reference: Workflow URLs

Replace `iaakashRoy/or-af` with your repository if needed:

- **All workflows**: https://github.com/iaakashRoy/or-af/actions
- **Workflow file**: https://github.com/iaakashRoy/or-af/blob/main/.github/workflows/publish.yml
- **Package on PyPI** (after publishing): https://pypi.org/project/or-af/
- **Repository releases**: https://github.com/iaakashRoy/or-af/releases

## 💡 Pro Tips

1. **Test first with TestPyPI**: Before publishing to PyPI, you can test with TestPyPI (requires modifying the workflow)

2. **Manual trigger**: You can manually run the workflow:
   - Go to Actions → Publish to PyPI
   - Click "Run workflow"
   - Select the branch
   - Click "Run workflow"

3. **Re-run failed workflows**: If a workflow fails due to a temporary issue:
   - Click "Re-run all jobs" on the workflow page

4. **Download build artifacts**: The built packages are available in the workflow logs

## 📚 Related Documentation

- `PYPI_PUBLISHING_DETAILS.md` - Values for PyPI Trusted Publishing setup
- `PUBLISHING_STATUS.md` - Current publishing status and steps
- `PUBLISHING.md` - General publishing guide
- GitHub Actions docs: https://docs.github.com/en/actions

---

**Remember**: After the workflow succeeds, wait 5-10 minutes for PyPI indexing before the package is installable with `pip install or-af`.
