# Contributing

If you notice an error, please don't hesitate to open an issue.

## Development setup (Ubuntu)

```sh
# update
sudo apt update
# install Python for ensuring that tests can be run
sudo apt install python3-pip \
  python3.8 python3.8-dev python3.8-distutils python3.8-venv \
  python3.9 python3.9-dev python3.9-distutils python3.9-venv \
  python3.10 python3.10-dev python3.10-distutils python3.10-venv \
  python3.11 python3.11-dev python3.11-distutils python3.11-venv
  python3.12 python3.12-dev python3.12-distutils python3.12-venv
  python3.13 python3.13-dev python3.13-venv
# install pipenv for creation of virtual environments

# check out repo
git clone https://github.com/stefantaubert/mel-cepstral-distance.git
cd mel_cepstral_distance
# create virtual environment
python3.13 -m venv .venv-py13
source .venv-py13/bin/activate
pip install -e .[dev]
```

## Running the tests

```sh
coverage erase
tox
coverage combine
coverage html -d coverage
coverage report -m
```

## Calculating test coverage

```sh
mkdir coverage
pytest \
  --cov=src/mel_cepstral_distance \
  --cov-report=html:coverage \
  src/mel_cepstral_distance_tests > coverage/output.log 2>&1
```

## Running the linter

```sh
ruff check --fix
```

## Running mypy

```sh
mypy

# run on tests
mypy src/mel_cepstral_distance_tests/ \
  --check-untyped-defs \
  --disable-error-code "arg-type"
```

## Upload to PyPI
```sh
rm -rf dist/; python3.13 -m build -o dist/

# upload to testpypi 
pipenv run twine upload --repository testpypi dist/*

# upload to pypi
pipenv run twine upload --repository pypi dist/*
```
