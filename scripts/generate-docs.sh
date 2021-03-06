#!/bin/sh

# pdoc --html margo_parser -o docs --force
sphinx-apidoc-3.8 -o sphinx/source/ margo_parser && \
rm -rf docs && \
cd sphinx && \
make clean && \
make html && \
mv build/html ../docs && \
cd .. &&
touch docs/.nojekyll