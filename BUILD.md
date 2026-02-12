```shell
# venv -a climbing @ local macbook venv cli
rm -rf dist build *.egg-info
python -m build
twine upload dist/*
```