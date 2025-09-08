const GitHubIntegration = require('./src/github-integration');

async function setupGitHub() {
    try {
        const github = await new GitHubIntegration().initialize();
        
        // Create repository
        const repo = await github.createRepo('woofy-mcwoofson-enterprise');
        console.log('✅ Repository created:', repo.data.html_url);
        
        // Push your project files
        const files = [
            {
                path: 'README.md',
                content: require('fs').readFileSync('./README.md', 'utf8'),
                message: 'Initial README'
            }
        ];
        
        await github.pushCode(repo.data.owner.login, repo.data.name, files);
        console.log('🐾 WOOFY project pushed to GitHub!');
        
    } catch (error) {
        console.error('❌ Setup failed:', error.message);
    }
}

setupGitHub();