#!/bin/sh

# pdoc --html margo_parser -o docs --force
sphinx-apidoc-3.8 -o docs/source/ margo_parser && \
cd docs && \
make clean && \
make html && \
cd ..