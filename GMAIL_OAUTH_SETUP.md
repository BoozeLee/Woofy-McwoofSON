# 🔐 Gmail OAuth Setup Guide

**Maintained by:** BoozeLee, 2025-09-08  
**Security Level:** ENTERPRISE CRITICAL  
**Status:** CONFIGURATION REQUIRED  

---

## 🚨 SECURITY NOTICE

**OAuth configuration is REQUIRED before production deployment.**  
**All steps must be completed and validated by Amazon Q.**

---

## 📋 Google Cloud Console Setup

### Step 1: Create OAuth 2.0 Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project or create new one
3. Navigate to **APIs & Services** → **Credentials**
4. Click **Create Credentials** → **OAuth 2.0 Client IDs**

### Step 2: Configure Application Type
- **Application Type:** Web application
- **Name:** Woofy McWoofson Gmail Integration

### Step 3: Authorized JavaScript Origins
**⚠️ SECURITY NOTE:** Only add if browser-based (SPA) OAuth required

**Production:**
```
https://woofymcwoofson.com
```

**Development:**
```
http://localhost:5000
http://localhost:8080
```

### Step 4: Authorized Redirect URIs
**CRITICAL:** Must match actual endpoints exactly

**Production:**
```
https://woofymcwoofson.com/oauth2callback
https://woofymcwoofson.com/auth/gmail/callback
```

**Development:**
```
http://localhost:5000/oauth2callback
http://localhost:5000/auth/gmail/callback
```

**Staging:**
```
https://staging.woofymcwoofson.com/oauth2callback
```

---

## ⏰ PROPAGATION DELAY WARNING

**IMPORTANT:** Google OAuth settings may take **5 minutes to several hours** to propagate.

**During this period:**
- OAuth requests may fail with "redirect_uri_mismatch" errors
- Authentication flows will not work
- Testing must wait for propagation completion

**Recommendation:** Configure OAuth settings 24 hours before deployment.

---

## 🔐 Credential Storage

### Environment Variables
```bash
# Gmail OAuth Credentials
GMAIL_CLIENT_ID=your_client_id_here
GMAIL_CLIENT_SECRET=your_client_secret_here
GMAIL_REDIRECT_URI=https://woofymcwoofson.com/oauth2callback

# OAuth Scopes
GMAIL_SCOPES=https://www.googleapis.com/auth/gmail.readonly,https://www.googleapis.com/auth/gmail.send
```

### GitHub Secrets (Production)
- `GMAIL_CLIENT_ID`
- `GMAIL_CLIENT_SECRET`
- `GMAIL_REDIRECT_URI`

### AWS Secrets Manager
```json
{
  "gmail_oauth": {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "redirect_uri": "https://woofymcwoofson.com/oauth2callback"
  }
}
```

---

## 🛡️ Security Requirements

### OAuth Flow Security
- **HTTPS Only:** All redirect URIs must use HTTPS in production
- **State Parameter:** Required for CSRF protection
- **PKCE:** Recommended for additional security
- **Token Rotation:** Implement refresh token rotation

### Validation Checklist
- [ ] Client ID and Secret stored securely
- [ ] Redirect URIs match exactly
- [ ] HTTPS enforced in production
- [ ] State parameter implemented
- [ ] Error handling implemented
- [ ] Token expiration handled
- [ ] Refresh token rotation configured

---

## 🧪 Testing Procedure

### Pre-Production Testing
1. **Development Environment:**
   - Test OAuth flow with localhost URIs
   - Verify token acquisition and refresh
   - Test error scenarios

2. **Staging Environment:**
   - Test with staging URIs
   - Verify production-like configuration
   - Load test OAuth endpoints

3. **Production Validation:**
   - Verify all URIs are accessible
   - Test OAuth flow end-to-end
   - Monitor for propagation delays

---

## 📞 Support & Troubleshooting

### Common Issues
- **redirect_uri_mismatch:** Check URI configuration and propagation
- **invalid_client:** Verify client ID and secret
- **access_denied:** Check OAuth scopes and permissions

### Emergency Contacts
- **OAuth Issues:** oauth-support@bakery-street-projct.com
- **Security Incidents:** security@bakery-street-projct.com
- **Technical Support:** BoozeLee

---

## 📋 Compliance Requirements

### Documentation
- [ ] OAuth configuration documented
- [ ] Security review completed
- [ ] Penetration testing performed
- [ ] Compliance audit passed

### Monitoring
- [ ] OAuth success/failure rates monitored
- [ ] Token usage tracked
- [ ] Security events logged
- [ ] Anomaly detection configured

---

**🚨 DEPLOYMENT BLOCKED until OAuth configuration complete and validated by Amazon Q**