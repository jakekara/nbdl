#!/usr/bin/env sh

pdoc --html src/margo_parser -o docs/apidocs/html --force

pdoc src/margo_parser -o docs/apidocs/markdown --force