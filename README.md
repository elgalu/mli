# mli

Fail and tell user to install from GHE or Nexus instead

## Build and publish the package

```bash
# Install build tools
pip install --upgrade build twine

# Build the package
python -m build

# Upload to PyPI (you'll need your PyPI credentials)
python -m twine upload dist/*

# To generate an `API token` go to `API tokens` in https://pypi.org/manage/account/
```

### Error

```log
PyPi.org public ERROR: The name 'mli' is too similar to an existing project.
```
