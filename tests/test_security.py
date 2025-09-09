
# WOOFY SECURITY GUARDRAILS - AUTO-APPLIED
import os
import sys
import logging

# Disable AWS credential logging
for logger_name in ['boto3', 'botocore', 'urllib3', 's3transfer']:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)

# Suppress credential discovery
os.environ['AWS_DEFAULT_OUTPUT'] = 'json'
os.environ['AWS_CLI_FILE_ENCODING'] = 'UTF-8'

# Import security guardrails
try:
    from security_guardrails import SecurityGuardrails
    SecurityGuardrails.secure_log("Security guardrails active")
except ImportError:
    pass

def test_no_secrets_in_codebase():
    """Fails if hardcoded secrets are detected in code or markdown files.

    Expanded to scan markdown (.md) for accidental credential leakage.
    """
    import os, re

    forbidden_patterns = [
        r"ghp_[A-Za-z0-9]{36,}",  # GitHub PAT
        r"sk_live_[A-Za-z0-9]{24,}",  # Stripe live key
        r"(?:AWS|aws)_?(?:SECRET|secret)?_?ACCESS_?KEY[=:\s]+[A-Za-z0-9/+=]{20,40}",  # AWS style
        r"(?i)(client_secret|api_key|token)[\'\"]?\s*[:=]\s*[\'\"][A-Za-z0-9_\-]{8,}[\'\"]",
    ]
    code_exts = (".py", ".js", ".env", ".json", ".yaml", ".yml", ".md")
    root = "."
    skip_dirs = {".git", ".github", "__pycache__", "venv", ".venv", "node_modules"}

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fname in filenames:
            if fname.endswith(code_exts):
                path = os.path.join(dirpath, fname)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                except Exception:
                    continue
                # Shallow allowlist to avoid flagging documentation placeholders
                placeholders = [
                    "your-key",
                    "YOUR_KEY",
                    "example_token",
                    "example-key",
                    "dummy",
                    "placeholder-key",
                    "PLACEHOLDER_KEY",
                    "placeholder_key",
                    "api_key\":\"your-key\"",
                    "your_client_secret",
                    "YOUR_CLIENT_SECRET",
                    "your-client-secret",
                    'client_secret": "your_client_secret"',
                    'client_secret":"your_client_secret"',
                    'client_secret: "your_client_secret"',
                    'your-grok-api-key-here',
                    'YOUR_GROK_API_KEY_HERE',
                    'your_grok_api_key_here',
                ]
                safe_text = text
                for ph in placeholders:
                    safe_text = safe_text.replace(ph, "<placeholder>")
                # Normalize generic doc placeholders like TOKEN="your_xxx" or key: 'your_xxx'
                import re as _re
                # 1) Replace any assignment of a quoted value starting with your_ (e.g., KEY="your_token")
                safe_text = _re.sub(r'([:=]\s*[\'\"])your_[A-Za-z0-9_\-]+([\'\"])', r'\1<placeholder>\2', safe_text, flags=_re.IGNORECASE)
                # 2) Specifically normalize common secret keys followed by a placeholder value (client_secret|api_key|token)
                #    Examples handled:
                #      client_secret: "your_client_secret"
                #      API_KEY="your-grok-api-key-here"
                #      token = "your_discord_token"
                safe_text = _re.sub(
                    r'(?i)\b(client_secret|api_key|token)[\'\"]?\s*[:=]\s*[\'\"]your[^\'\"]+[\'\"]',
                    r'\1: "<placeholder>"',
                    safe_text,
                )
                # 3) Replace any client_secret/api_key/token assignment whose value contains placeholder/example/dummy words
                safe_text = _re.sub(
                    r'(?i)\b(client_secret|api_key|token)[\'\"]?\s*[:=]\s*[\'\"][^\'\"]*(placeholder|example|dummy)[^\'\"]*[\'\"]',
                    r'\1: "<placeholder>"',
                    safe_text,
                )
                # 4) Replace any quoted literal placeholder-key/token values anywhere
                safe_text = _re.sub(r'[\'\"]placeholder[-_]?key[\'\"]', '"<placeholder>"', safe_text, flags=_re.IGNORECASE)
                safe_text = _re.sub(r'[\'\"]placeholder[-_]?token[\'\"]', '"<placeholder>"', safe_text, flags=_re.IGNORECASE)
                # 5) Normalize keys that include token or api_key (e.g., "github_token", "grok_api_key") when value is placeholder/example/your_
                #    Allow optional quotes around the key name (JSON style) and around separators
                safe_text = _re.sub(
                    r'(?i)([\'\"]?\b[a-z0-9_]*(?:api[_-]?key|token)\b[\'\"]?\s*[:=]\s*[\'\"])([^\'\"]*(?:your[_-]|placeholder|example|dummy)[^\'\"]*)([\'\"])',
                    r'\1<placeholder>\3',
                    safe_text,
                )
                for pat in forbidden_patterns:
                    assert not re.search(
                        pat, safe_text
                    ), f"Potential secret in {path} pattern {pat}"


def test_env_example_exists():
    import os

    assert os.path.exists(".env.example"), ".env.example should be present"
