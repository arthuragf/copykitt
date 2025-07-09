#!/bin/bash

# Generates a base layer for the Lambda function

# Remove the container first (if it exists)
docker rm -f layer-container 2>/dev/null || true

# Build the base layer
docker build -t base-layer .

# rename it to base-layer
docker run --name layer-container base-layer

# Copy the generated zip artifact so our CDK can use it
docker cp layer-container:layer.zip . && echo "Created layer.zip with updated base layer."
