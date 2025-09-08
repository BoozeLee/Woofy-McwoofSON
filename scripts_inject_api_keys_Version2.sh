#!/bin/bash
# Securely injects GROQ and Perplexity API keys into local .env file

ENV_FILE=".env"

echo "🐾 Woofy Secure API Key Injector 🦴"

# Prompt user for keys (never echo to screen)
read -sp "Enter GROQ API Key: " GROQ_KEY && echo
read -sp "Enter Perplexity API Key: " PERPLEXITY_KEY && echo

# Backup existing .env
cp $ENV_FILE "${ENV_FILE}.bak.$(date +%s)"

# Remove any existing keys
grep -v 'GROQ_API_KEY' $ENV_FILE | grep -v 'PERPLEXITY_API_KEY' > "${ENV_FILE}.tmp" || true

# Write new keys
echo "GROQ_API_KEY=${GROQ_KEY}" >> "${ENV_FILE}.tmp"
echo "PERPLEXITY_API_KEY=${PERPLEXITY_KEY}" >> "${ENV_FILE}.tmp"

mv "${ENV_FILE}.tmp" $ENV_FILE

echo "✅ API keys safely added to .env (backup at ${ENV_FILE}.bak.*)"