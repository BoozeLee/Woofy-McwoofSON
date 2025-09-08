#!/bin/bash

# Add all new and changed files in the current repository
git add .

# Commit with a descriptive message
git commit -m "Add all WOOFY McWOOFSON enterprise templates, docs, scripts, compliance, and assets"

# Push to the main branch (or change 'main' to your branch name)
git push origin main

echo "All files added, committed, and pushed!"