```shell
# venv -a climbing @ local macbook venv cli
rm -rf dist build *.egg-info
pipx run build
pipx run twine upload dist/*
```