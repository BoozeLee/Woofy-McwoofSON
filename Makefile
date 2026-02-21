# Makefile for Woofy-McwoofSON

.PHONY: help install test build run clean

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make test     - Run tests"
	@echo "  make build    - Build project"
	@echo "  make run      - Run project"
	@echo "  make clean    - Clean build artifacts"

install:
	@echo "Installing dependencies..."

test:
	@echo "Running tests..."

build:
	@echo "Building project..."

run:
	@echo "Running project..."

clean:
	@echo "Cleaning..."
