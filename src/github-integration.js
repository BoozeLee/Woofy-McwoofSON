const AWS = require('aws-sdk');
const { Octokit } = require('@octokit/rest');

class GitHubIntegration {
    constructor() {
        this.secretsManager = new AWS.SecretsManager({ region: 'us-east-1' });
        this.octokit = null;
    }

    async initialize() {
        const credentials = await this.getGitHubCredentials();
        this.octokit = new Octokit({
            auth: credentials.client_secret
        });
        return this;
    }

    async getGitHubCredentials() {
        const result = await this.secretsManager.getSecretValue({
            SecretId: 'github-oauth-secret'
        }).promise();
        
        return JSON.parse(result.SecretString);
    }

    async createRepo(name, description = 'WOOFY McWOOFSON Enterprise AI Assistant') {
        return await this.octokit.rest.repos.createForAuthenticatedUser({
            name,
            description,
            private: false,
            auto_init: true
        });
    }

    async pushCode(owner, repo, files) {
        for (const file of files) {
            await this.octokit.rest.repos.createOrUpdateFileContents({
                owner,
                repo,
                path: file.path,
                message: `🐾 WOOFY: ${file.message}`,
                content: Buffer.from(file.content).toString('base64')
            });
        }
    }
}

module.exports = GitHubIntegration;