#!/bin/bash
# 🐾 License Compliance Checker Script

echo "Checking dependency licenses..."

if [ -f package.json ]; then
  npx license-checker --summary
elif [ -f requirements.txt ]; then
  pip-licenses
else
  echo "No recognized dependency file found."
fi