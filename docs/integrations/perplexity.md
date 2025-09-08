# 🧠 Perplexity Bot Integration

## Overview

This document describes the integration of Perplexity AI into the WOOFY McWOOFSON project. Perplexity provides advanced AI-powered search and question-answering capabilities with real-time web access.

## Features

- **Real-time Web Search**: Access to current information and web content
- **Advanced AI Models**: Powered by state-of-the-art language models
- **Credit-based Usage**: Pay-per-use model with user-managed credits
- **Secure Integration**: Environment-based credential management

## Setup Instructions

### 1. Prerequisites

- Perplexity API account with active credits
- Python environment with required dependencies

### 2. Environment Configuration

Create or update your `.env` file with the following variables:

```bash
# Perplexity API Configuration
PERPLEXITY_API_KEY=your_perplexity_api_key_here
```

**Security Note**: Never commit the `.env` file to version control. It should be added to `.gitignore`.

### 3. Installation

Install the required Python package:

```bash
pip install python-dotenv
```

### 4. Usage

#### Basic Query Example

```python
from integrations.perplexity.perplexity_client import PerplexityClient

# Initialize client (loads API key from environment)
client = PerplexityClient()

# Execute a query
response = client.query("What is the latest news about AI development?")

# Process the response
print(response)

# Clean up
client.close()
```

#### Advanced Usage

```python
# Specify model and parameters
response = client.query(
    prompt="Explain quantum computing in simple terms",
    model="pplx-7b-online",
    temperature=0.7,
    max_tokens=500
)
```

## API Reference

### PerplexityClient Class

#### Methods

- `__init__(api_key=None)`: Initialize client with optional API key
- `query(prompt, model="pplx-7b-online", **kwargs)`: Execute AI query
- `get_credit_usage()`: Get current credit usage (placeholder)
- `close()`: Close HTTP session

#### Parameters

- `prompt`: The question or query text
- `model`: AI model to use (default: "pplx-7b-online")
- `temperature`: Creativity control (0.0-1.0)
- `max_tokens`: Maximum response length

## Security Considerations

- API keys are loaded from environment variables only
- No credentials are hardcoded or logged
- HTTPS encryption for all API communications
- Response sanitization to prevent sensitive data exposure

## Credit Management

- Monitor your Perplexity account for credit usage
- The `get_credit_usage()` method is a placeholder for future implementation
- Set up billing alerts in your Perplexity account

## Error Handling

The client includes comprehensive error handling for:
- Invalid API keys
- Network connectivity issues
- API rate limits
- Malformed requests

## Testing

Run the included test script:

```bash
python integrations/perplexity/perplexity_client.py
```

## Troubleshooting

### Common Issues

1. **API Key Not Found**: Ensure `PERPLEXITY_API_KEY` is set in your `.env` file
2. **Network Errors**: Check internet connectivity and API status
3. **Rate Limits**: Implement retry logic with exponential backoff

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Integration with WOOFY McWOOFSON

This integration enhances WOOFY McWOOFSON's capabilities by providing:
- Real-time information access
- Advanced question-answering
- Research assistance
- Content generation

## Support

For issues related to:
- Perplexity API: Contact Perplexity support
- Integration code: Create an issue in the project repository
- Security concerns: Follow the project's security reporting process

---

**Last Updated**: 2025-09-07
**Version**: 1.0
**Author**: Kilo Code