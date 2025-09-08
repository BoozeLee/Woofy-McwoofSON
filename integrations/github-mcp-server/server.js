const express = require('express');
const { SecureAPIManager } = require('../secure_api_client');
const app = express();

class GitHubMCPServer {
    constructor() {
        this.apiManager = new SecureAPIManager();
        this.setupMiddleware();
        this.setupRoutes();
    }

    setupMiddleware() {
        app.use(express.json());
        app.use((req, res, next) => {
            console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
            next();
        });
    }

    setupRoutes() {
        app.get('/health', (req, res) => {
            res.json({ status: 'healthy', timestamp: new Date().toISOString() });
        });

        app.post('/github/webhook', async (req, res) => {
            try {
                const credentials = await this.apiManager.getCredentials('github');
                // Process GitHub webhook with secure credentials
                res.json({ received: true });
            } catch (error) {
                console.error('GitHub webhook error:', error);
                res.status(500).json({ error: 'Internal server error' });
            }
        });

        app.get('/context/:repo', async (req, res) => {
            try {
                const credentials = await this.apiManager.getCredentials('github');
                // Fetch repository context securely
                res.json({ context: 'secure_context_data' });
            } catch (error) {
                console.error('Context fetch error:', error);
                res.status(500).json({ error: 'Context unavailable' });
            }
        });
    }

    start(port = 8080) {
        app.listen(port, () => {
            console.log(`🐾 WOOFY MCP Server running on port ${port}`);
        });
    }
}

const server = new GitHubMCPServer();
server.start();