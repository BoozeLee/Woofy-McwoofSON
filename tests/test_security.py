def test_no_secrets_in_codebase():
    """Fails if hardcoded secrets are detected in code or markdown files.

    Expanded to scan markdown (.md) for accidental credential leakage.
    Placeholder values used in documentation (e.g. ``your_client_secret``)
    are ignored so example/template files do not produce false positives.
    """
    import os
    import re

    forbidden_patterns = [
        r'ghp_[A-Za-z0-9]{36,}',              # GitHub PAT
        r'sk_live_[A-Za-z0-9]{24,}',          # Stripe live key
        r'(?:AWS|aws)_?(?:SECRET|secret)?_?ACCESS_?KEY[=:\s]+[A-Za-z0-9/+=]{20,40}',  # AWS style
        r'(?i)(client_secret|api_key|token)[\'\"]?\s*[:=]\s*[\'\"][A-Za-z0-9_\-]{8,}[\'\"]',
    ]
    placeholder_marks = ('your', 'example', 'xxxx', 'changeme', '<redacted>', 'xxx', '1234', 'placeholder')
    code_exts = ('.py', '.js', '.env', '.json', '.yaml', '.yml', '.md')
    root = '.'
    skip_dirs = {'.git', '.github', '__pycache__', 'venv', '.venv', 'node_modules'}

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fname in filenames:
            if fname.endswith(code_exts):
                path = os.path.join(dirpath, fname)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        text = f.read()
                except Exception:
                    continue
                for pat in forbidden_patterns:
                    for m in re.finditer(pat, text):
                        value = m.group(0)
                        if any(mark in value.lower() for mark in placeholder_marks):
                            continue
                        raise AssertionError(f"Potential secret in {path} pattern {pat}")

def test_env_example_exists():
    import os
    assert os.path.exists('.env.example'), ".env.example should be present"
