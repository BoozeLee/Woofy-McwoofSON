def test_no_secrets_in_codebase():
    """
    Fails if hardcoded secrets are detected in key source files.
    """
    import os, re

    forbidden_patterns = [
        r'ghp_[A-Za-z0-9]{36,}',  # GitHub PAT
        r'sk_live_[A-Za-z0-9]{24,}',  # Stripe live key
        r'(client_secret|api_key|token)[\'\"]?\s*[:=]\s*[\'\"][A-Za-z0-9_\-]+[\'\"]'
    ]
    root = '.'
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(('.py', '.js', '.env', '.json')):
                with open(os.path.join(dirpath, fname), 'r', encoding='utf-8') as f:
                    text = f.read()
                    for pat in forbidden_patterns:
                        assert not re.search(pat, text), f"Potential secret in {fname}"

def test_env_example_exists():
    import os
    assert os.path.exists('.env.example'), ".env.example should be present"
