# margo-parser developer documentation

## Setting up your environment

Set up a virtual environment. I like to use `mkvirtualenv`.

Then install the developer requirements:

```bash
pip install -r requirements-dev.txt
```

Then install the package in an editable form:

```bash
pip install -e .
```

## Using tox

This project uses tox to automate linting, formatting and testing.

To run tox, use:

```bash
tox
```

You should see something like:

```
flake8: recreate env because python changed version_info=[3, 11, 2, 'final', 0]->[3, 9, 16, 'final', 0] | executable='/usr/local/bin/python3.11'->'/usr/local/bin/python3.9'
flake8: remove tox env folder /app/.tox/flake8
flake8: install_deps> python -I -m pip install -r requirements-dev.txt
.pkg: recreate env because python changed version_info=[3, 11, 2, 'final', 0]->[3, 9, 16, 'final', 0] | executable='/usr/local/bin/python3.11'->'/usr/local/bin/python3.9'
.pkg: remove tox env folder /app/.tox/.pkg
.pkg: install_requires> python -I -m pip install hatch-requirements-txt hatchling
.pkg: _optional_hooks> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
.pkg: get_requires_for_build_sdist> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
.pkg: prepare_metadata_for_build_wheel> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
.pkg: build_sdist> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
flake8: install_package_deps> python -I -m pip install 'lark-parser[regex]==0.10.0' pyyaml==5.3.1
flake8: install_package> python -I -m pip install --force-reinstall --no-deps /app/.tox/.tmp/package/31/margo_parser-1.0.0.tar.gz
flake8: commands[0]> flake8 .
flake8: OK ✔ in 1 minute 13.72 seconds
black: recreate env because python changed version_info=[3, 11, 2, 'final', 0]->[3, 9, 16, 'final', 0] | executable='/usr/local/bin/python3.11'->'/usr/local/bin/python3.9'
black: remove tox env folder /app/.tox/black
black: install_deps> python -I -m pip install -r requirements-dev.txt
black: install_package_deps> python -I -m pip install 'lark-parser[regex]==0.10.0' pyyaml==5.3.1
black: install_package> python -I -m pip install --force-reinstall --no-deps /app/.tox/.tmp/package/32/margo_parser-1.0.0.tar.gz
black: commands[0]> black .
All done! ✨ 🍰 ✨
25 files left unchanged.
black: OK ✔ in 45.67 seconds
tests: recreate env because python changed version_info=[3, 11, 2, 'final', 0]->[3, 9, 16, 'final', 0] | executable='/usr/local/bin/python3.11'->'/usr/local/bin/python3.9'
tests: remove tox env folder /app/.tox/tests
tests: install_deps> python -I -m pip install -r requirements-dev.txt
tests: install_package_deps> python -I -m pip install 'lark-parser[regex]==0.10.0' pyyaml==5.3.1
tests: install_package> python -I -m pip install --force-reinstall --no-deps /app/.tox/.tmp/package/33/margo_parser-1.0.0.tar.gz
tests: commands[0]> python -m pytest
============================================= test session starts =============================================
platform linux -- Python 3.9.16, pytest-7.2.2, pluggy-1.0.0
cachedir: .tox/tests/.pytest_cache
rootdir: /app
collected 27 items                                                                                            

tests/test_MargoAssignment.py ..                                                                        [  7%]
tests/test_MargoBlock.py .......                                                                        [ 33%]
tests/test_MargoDirective.py ...                                                                        [ 44%]
tests/test_MargoMarkdownCellPreambleBlock.py .                                                          [ 48%]
tests/test_MargoPythonCellPreambleBlock.py .                                                            [ 51%]
tests/test_get_preamble_block.py ..                                                                     [ 59%]
tests/test_get_preamble_source.py ....                                                                  [ 74%]
tests/test_parser.py .......                                                                            [100%]

============================================= 27 passed in 1.12s ==============================================
.pkg: _exit> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
  flake8: OK (73.72=setup[73.24]+cmd[0.48] seconds)
  black: OK (45.67=setup[44.98]+cmd[0.68] seconds)
  tests: OK (45.88=setup[43.94]+cmd[1.93] seconds)
  congratulations :) (165.41 seconds)
```

## Running tests with docker-compose

To run tox in docker-compose, use:

```bash
docker-compose run py39
```

Replace py39 with any of: `py38`, `py39`, `py310`, `py311` to run
tests in different versions of python.

Note that as of version 1.0.0 this library does not support python
versions older than 3.8, so that's why there are no docker-compose
services for those python versions.
