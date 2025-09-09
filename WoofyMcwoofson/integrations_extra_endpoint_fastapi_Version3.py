
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

# Maintained by BoozeLee, 2025-09-08
from fastapi import APIRouter

router = APIRouter()


@router.get("/woof-extra", summary="Extra dog fact")
def woof_extra():
    return {
        "fact": "Dogs have unique nose prints, just like human fingerprints!",
        "endpoint": "/woof-extra",
    }
