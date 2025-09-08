# 🐶 Woofy Demo Script: Gmail & Google Drive Automation

## 1. Prerequisites
- OAuth setup complete (see knowledge-vault/GMAIL_OAUTH_SETUP.md)
- Credentials stored in GitHub Secrets

## 2. Demo: Send Email via Gmail API

```python
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SERVICE_ACCOUNT_FILE = os.environ["GOOGLE_OAUTH_JSON"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('gmail', 'v1', credentials=credentials)

def send_message():
    message = {
        'raw': 'BASE64_ENCODED_EMAIL'
    }
    result = service.users().messages().send(userId='me', body=message).execute()
    print(f"Message sent: {result['id']}")

send_message()
```

## 3. Demo: Upload File to Google Drive

```python
SCOPES = ['https://www.googleapis.com/auth/drive.file']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive = build('drive', 'v3', credentials=credentials)

def upload_file(filename, mime_type):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filename, mimetype=mime_type)
    file = drive.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File uploaded: {file['id']}")

upload_file('demo.txt', 'text/plain')
```

---

**For full setup, see knowledge-vault/GMAIL_OAUTH_SETUP.md.**