#!/bin/bash

# This script executes the test suite to validate the functionality of the project.

# Exit immediately if a command exits with a non-zero status.
set -e

# Run the tests using pytest
pytest tests/ --maxfail=1 --disable-warnings -q

# Print a success message
echo "All tests passed successfully!"