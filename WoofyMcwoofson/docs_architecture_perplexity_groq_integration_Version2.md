# 🤖 Perplexity + Groq Integration Flow

```mermaid
flowchart TD
    subgraph User/Agent
      A1(Client/Integration)
    end
    subgraph MCP Server
      B1[API Gateway]
      B2[Secure Context Provider]
      B3[AWS Secrets Manager]
      B4[Audit Logging]
    end
    subgraph AI Providers
      C1(Perplexity API)
      C2(Groq API)
    end

    A1 --> B1
    B1 --> B2
    B2 --> B3
    B2 -->|Fetch API Key| B3
    B2 -->|Call| C1
    B2 -->|Call| C2
    B2 --> B4
```

**Summary:**  
- All secret/API calls are handled by MCP Server, which fetches keys securely from AWS Secrets Manager, routes to Perplexity/Groq, and logs all access for compliance.