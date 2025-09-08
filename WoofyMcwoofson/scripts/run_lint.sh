#!/bin/bash

# Run linting checks on the codebase
echo "Running lint checks..."

# Install flake8 if not already installed
if ! command -v flake8 &> /dev/null
then
    echo "flake8 not found, installing..."
    pip install flake8
fi

# Run flake8 on the integrations and tests directories
flake8 integrations/ tests/

# Check if flake8 succeeded
if [ $? -eq 0 ]; then
    echo "Lint checks passed!"
else
    echo "Lint checks failed. Please fix the issues above."
    exit 1
fi