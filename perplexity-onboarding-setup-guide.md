# 🛡️ Secure Perplexity API Key Setup Guide with Onboarding

*Agent Instructions for Robust Security and Cross-Platform Compatibility*

## 🎯 Executive Summary

This guide provides secure, step-by-step instructions for setting up your Perplexity API key using Onboarding (the popular IDE assistant) in VSCode. Designed for cases where keyboard shortcuts like Ctrl+Shift+P may not work, ensuring your API key remains encrypted and secure.

## 🧠 Security Framework Overview

The setup follows a secure architecture:
- **Access Layer**: IDE integration and settings panel navigation
- **Input Layer**: Secure API key entry without exposure
- **Storage Layer**: Encrypted secret storage in Onboarding's vault
- **Verification Layer**: Connection testing and confirmation
- **Audit Layer**: Security finalization and access review

## 🚀 Quick Start Instructions

### For VSCode with Onboarding Extension:

1. **Open Onboarding Panel**: Locate the Onboarding icon in the VSCode sidebar or top menu
2. **Access Settings**: Navigate to Settings → Integrations or Configure Connections
3. **Add API Key**: Search for "Perplexity" or "AI API Keys" and click 'Add API Key'
4. **Secure Entry**: Use the password-style input field to enter your Perplexity API key
5. **Store Securely**: Name the key "PPLX_API_KEY" and save in Onboarding's secret storage
6. **Test Connection**: Issue a test query to verify the setup
7. **Confirm Security**: Ensure the key is only visible in secure settings

## 📋 Detailed Setup Steps

### 1. Use Onboarding's Settings Command Directly

**Instruction for Setup:**
1. Open Onboarding's command or home panel (usually available in the IDE sidebar or top menu).
2. Locate the 'Settings', 'Integrations', or 'Configure Connections' option.
   - If available, use the search or filtering function to find "Perplexity" or "AI API Keys".
3. Click 'Add API Key' or 'Configure Perplexity'.

*Tip: If there's an Onboarding quick command menu (often activated by clicking the robot/assistant icon), use that to locate integrations.*

### 2. Prompt User for API Key Entry (Secure)

**Command for Setup:**
4. Prompt for API key as secure input (never display or echo the entered value).
   - Use a password-style field for entry.
   - If possible, store key in secure workspace/secret vault, not in plain config files.
5. Name the key "PPLX_API_KEY" and set its value to the user's input.

*Security Note: Ask the user to paste their Perplexity API key for secure onboarding. This key will be encrypted and only used for Perplexity plugin access.*

### 3. Verify and Save Configuration

**Follow-Up Instructions:**
6. Test the API key by issuing a simple Perplexity query (e.g. "Summarize this text: [your text]").
   - Confirm a valid response.
7. Confirm to the user: "API key securely set. You are ready to use Perplexity!"

*Agent logs: Only record success/failure, not the key value.*

### 4. Security Finalization

**Final Setup Command:**
8. Confirm the API key is only visible in Onboarding's secure secrets/settings—not in public files or logs.
9. Advise the user to change/revoke the key immediately if it's ever exposed.
10. Review plugin access and permissions for safety.

## 🔑 Summary Command (for Automated Setup)

```plaintext
Onboarding, please:
- Open integrations/settings panel.
- Add Perplexity API key using a secure input field.
- Store the key as "PPLX_API_KEY" in Onboarding's secret storage.
- Test connection with a sample query to Perplexity.
- Confirm secure setup and notify me when ready.
```

## 🛠️ Troubleshooting

### Common Issues and Solutions

**Issue: Can't access Onboarding settings**
- Ensure Onboarding extension is installed and enabled
- Try restarting VSCode
- Check for extension updates

**Issue: API key entry not secure**
- Verify you're using Onboarding's built-in key management
- Avoid storing in plain text files
- Use VSCode's secure storage when available

**Issue: Test query fails**
- Verify API key is valid and active
- Check network connectivity
- Ensure Perplexity service is accessible

**Issue: Key appears in logs**
- Review Onboarding's logging settings
- Disable verbose logging if enabled
- Clear any temporary logs

## 🔒 Security Best Practices

### Key Management
- **Never expose API keys** in code, logs, or shared files
- **Use secure storage** provided by Onboarding
- **Regular rotation** of API keys for enhanced security
- **Monitor access** and revoke if compromised

### Privacy Settings
- **Review Onboarding permissions** regularly
- **Enable encryption** for stored secrets
- **Configure access controls** for team environments
- **Audit usage logs** without exposing sensitive data

### Corporate Environment
- **Comply with security policies** for API key usage
- **Use enterprise-grade storage** when available
- **Implement access controls** and monitoring
- **Document security procedures** for team members

## 📊 Verification Checklist

### Successful Setup Checklist
- [ ] Onboarding extension installed and accessible
- [ ] Settings panel opened successfully
- [ ] API key entered securely without exposure
- [ ] Key stored as "PPLX_API_KEY" in secure vault
- [ ] Test query executed and responded correctly
- [ ] Security confirmation received
- [ ] Access permissions reviewed

### Testing Commands
```bash
# Example test query (replace with actual text)
Test query: "Summarize this guide's security features"
```

## 💡 Advanced Features

### Integration Options
- **Multiple AI providers** configuration
- **Workspace-specific keys** for different projects
- **Automated key rotation** scheduling
- **Backup and recovery** procedures

### Monitoring and Alerts
- **Usage tracking** without exposing keys
- **Security alerts** for potential breaches
- **Audit trails** for compliance
- **Performance monitoring** of API calls

---

*This guide ensures your Perplexity API key is set up securely with Onboarding, keeping your credentials safe and your development environment protected.*