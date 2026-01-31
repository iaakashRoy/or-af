# Quick Start: Check Workflow Status

## 🚀 After Creating a Release

### 1️⃣ Go to Actions Tab
👉 https://github.com/iaakashRoy/or-af/actions

### 2️⃣ Look for Status Icons

| Icon | Status | What to Do |
|------|--------|------------|
| 🟡 | **In Progress** | Wait 2-5 minutes |
| ✅ | **Success** | Test: `pip install or-af` |
| ❌ | **Failed** | Click to view logs & troubleshoot |

### 3️⃣ Verify Publication

```bash
# After workflow succeeds (wait 5-10 min for PyPI indexing):
pip install or-af
python -c "import or_af; print('Success!')"
```

### 4️⃣ Check PyPI
📦 https://pypi.org/project/or-af/

---

## 🔧 Common Issues

**No workflow appears?**
- Check release is **published** (not draft)

**Authentication error?**
- Configure PyPI Trusted Publishing (see `PYPI_PUBLISHING_DETAILS.md`)

**"Package already exists"?**
- Update version number in `pyproject.toml` and `setup.py`
- Create new release with new version tag

---

## 📚 Full Guide
See `MONITORING_WORKFLOW.md` for complete instructions.

## ⏱️ Expected Timeline
- Workflow runs: **2-5 minutes**
- PyPI indexing: **5-10 minutes**
- **Total: ~10 minutes** until `pip install or-af` works
