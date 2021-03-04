#!/bin/bash

# Activate virtual environment
. /appenv/bin/activate

# Download requirements to the build cache
pip download -d /build -r requirements_test.txt --no-input

# Install application test requirements
pip install -r requirements_test.txt

# Run test.sh arguments
exec $@

