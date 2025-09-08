# 🔐 Guide: Using Secret Manager with Cloud Code

**Date:** 2025-09-08
**Purpose:** Provide a standardized guide for securely managing API keys and other secrets using Google Secret Manager and the Cloud Code extension in VS Code.
**Author:** Kilo Code

---

## 1. Why Use Secret Manager?

Hardcoding secrets (like API keys, database passwords, or tokens) into source code is a major security risk. Secret Manager provides a secure, centralized place to store and manage these secrets. The Cloud Code extension integrates directly with it, making it easy to use secrets in your applications without exposing them.

---

## 2. Creating a Secret in VS Code

You can manage secrets directly from the VS Code interface.

1.  **Open Cloud Code Explorer:** Click the Google Cloud icon in the VS Code Activity Bar.
2.  **Navigate to Secret Manager:** Expand the **Secret Manager** section.
3.  **Create Secret:** Right-click the **Secret Manager** header and select **`Create Secret`**.
4.  **Enter ID and Value:**
    -   **Secret ID:** A unique name for your secret (e.g., `my-api-key`).
    -   **Secret Value:** The actual secret value you want to store.

---

## 3. Using Secrets in Cloud Run (Recommended Method)

The most secure and efficient way to use secrets in Cloud Run is to mount them as environment variables.

### A. Grant IAM Permissions

The service account running your Cloud Run service needs permission to access the secret.
1.  Go to the **Google Cloud Console > IAM & Admin**.
2.  Find the service account used by your Cloud Run service (e.g., the Default Compute Service Account).
3.  Grant it the **`Secret Manager Secret Accessor`** role.

### B. Mount the Secret During Deployment

1.  Start the deployment process with `Cloud Code: Deploy to Cloud Run`.
2.  In the deployment configuration window, click the **`Secrets`** tab.
3.  Click **`Add Secret`** and configure it:
    -   **Type:** `Environment Variable`
    -   **Secret:** Select the secret you created (e.g., `my-api-key`).
    -   **Version:** `latest`
    -   **Variable Name:** The name your code will use (e.g., `API_KEY`).
4.  Click **`Deploy`**.

### C. Access the Secret in Code

Your application can now read the secret from the environment.

**Example `app.py`:**
```python
import os
from flask import Flask

app = Flask(__name__)

# Cloud Run securely injects the secret as this environment variable
API_KEY = os.environ.get('API_KEY', 'default-key-not-found')

@app.route('/')
def use_the_key():
    if API_KEY != 'default-key-not-found':
        return f'Success! The API Key is configured.'
    else:
        return 'Error: API Key environment variable not found.'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```

---

## 4. Accessing Secrets via Code (Alternative Method)

For other environments (like local development or virtual machines), you can fetch secrets directly using the client library.

### A. Install Client Library

Add the library to your `requirements.txt`:
```
google-cloud-secret-manager
```
Then run `pip install -r requirements.txt`.

### B. Code to Fetch a Secret

```python
from google.cloud import secretmanager

def access_secret_version(project_id: str, secret_id: str, version_id: str = "latest") -> str:
    """
    Access the payload for the given secret version and return it as a string.
    """
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})

    # Return the decoded payload.
    payload = response.payload.data.decode("UTF-8")
    return payload

# Example usage:
# project_id = "your-gcp-project-id"
# api_key = access_secret_version(project_id, "my-api-key")
# print(f"Successfully accessed secret: {api_key[:4]}...")
```

---

## 5. Security Best Practices

-   **Least Privilege:** Always grant the `Secret Manager Secret Accessor` role to the specific service account that needs it, not to broader groups.
-   **Versioning:** Use secret versions to manage key rotation. You can pin a service to a specific version for stability.
-   **Audit Logs:** Enable Secret Manager audit logs to track when secrets are accessed.

---
