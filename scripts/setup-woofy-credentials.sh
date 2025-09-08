#!/bin/bash

# 🐕‍🦺 WOOFY McWOOFSON Secure Credential Setup Script
# Enterprise-Grade Git Authentication Setup
# NEVER share your tokens - this script helps you set them up securely

set -e

# Configuration
SCRIPT_VERSION="1.0"
WOOFY_REPO="https://github.com/Bakery-street-projct/Woofy-McwoofSON.git"
WOOFY_EMAIL="${WOOFY_EMAIL:-dev@woofymcwoofson.com}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_security() {
    echo -e "${PURPLE}[SECURITY]${NC} $1"
}

log_step() {
    echo -e "${CYAN}[STEP]${NC} $1"
}

# Security disclaimer
security_disclaimer() {
    echo
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                    🔐 SECURITY NOTICE                        ║"
    echo "╠════════════════════════════════════════════════════════════════╣"
    echo "║  This script helps you set up YOUR OWN credentials.         ║"
    echo "║  NEVER share tokens, passwords, or private keys!            ║"
    echo "║                                                              ║"
    echo "║  🔴 DANGER: Sharing credentials can compromise:             ║"
    echo "║     • Your GitHub account                                    ║"
    echo "║     • Repository access                                      ║"
    echo "║     • Organization permissions                               ║"
    echo "║     • Enterprise security                                    ║"
    echo "║                                                              ║"
    echo "║  ✅ SAFE: Generate your own tokens and keys                  ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo
}

# Check system requirements
check_requirements() {
    log_step "Checking system requirements..."

    # Check for required commands
    local missing_commands=()

    for cmd in git curl wget; do
        if ! command -v "$cmd" &> /dev/null; then
            missing_commands+=("$cmd")
        fi
    done

    if [[ ${#missing_commands[@]} -gt 0 ]]; then
        log_error "Missing required commands: ${missing_commands[*]}"
        log_info "Please install missing commands and try again."
        exit 1
    fi

    # Check Git version
    local git_version=$(git --version | sed 's/git version //')
    log_info "Git version: $git_version"

    log_success "System requirements check passed"
}

# Setup Git configuration
setup_git_config() {
    log_step "Setting up Git configuration..."

    # Get user information
    read -p "Enter your full name: " user_name
    read -p "Enter your email address: " user_email

    # Configure Git
    git config --global user.name "$user_name"
    git config --global user.email "$user_email"
    git config --global init.defaultBranch main
    git config --global core.editor "code --wait"
    git config --global pull.rebase true

    log_success "Git configuration completed"
    echo "  Name: $user_name"
    echo "  Email: $user_email"
}

# Setup credential helper
setup_credential_helper() {
    log_step "Setting up credential helper..."

    echo
    echo "Choose your credential storage method:"
    echo "1) Store (persistent - saves to file)"
    echo "2) Cache (temporary - memory only)"
    echo "3) Manager (OS-specific keychain)"
    read -p "Enter choice (1-3): " choice

    case $choice in
        1)
            git config --global credential.helper store
            log_success "Credential helper set to 'store'"
            log_security "Credentials will be saved to ~/.git-credentials"
            ;;
        2)
            git config --global credential.helper 'cache --timeout=28800'
            log_success "Credential helper set to 'cache' (8 hours)"
            log_security "Credentials stored in memory only"
            ;;
        3)
            if [[ "$OSTYPE" == "darwin"* ]]; then
                git config --global credential.helper osxkeychain
                log_success "Credential helper set to 'osxkeychain'"
            elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
                git config --global credential.helper manager
                log_success "Credential helper set to 'manager'"
            else
                git config --global credential.helper libsecret
                log_success "Credential helper set to 'libsecret'"
            fi
            ;;
        *)
            log_warning "Invalid choice. Using default 'store' helper."
            git config --global credential.helper store
            ;;
    esac
}

# Generate GitHub PAT instructions
generate_github_pat() {
    log_step "GitHub Personal Access Token Setup"

    echo
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                🐙 GITHUB PAT GENERATION                       ║"
    echo "╠════════════════════════════════════════════════════════════════╣"
    echo "║  Follow these steps to generate your PAT:                   ║"
    echo "║                                                              ║"
    echo "║  1. Open: https://github.com/settings/tokens                ║"
    echo "║  2. Click: 'Generate new token (classic)'                   ║"
    echo "║  3. Name: 'WOOFY-McWOOFSON-DEV-$(date +%Y%m%d)'             ║"
    echo "║  4. Expiration: 90 days                                     ║"
    echo "║  5. Scopes: Select these permissions:                       ║"
    echo "║     ✅ repo (full repository access)                        ║"
    echo "║     ✅ workflow (GitHub Actions)                            ║"
    echo "║     ✅ read:org (organization read)                         ║"
    echo "║     ✅ read:packages (package read)                         ║"
    echo "║  6. Click: 'Generate token'                                 ║"
    echo "║  7. COPY the token immediately (it disappears!)            ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo

    # Wait for user confirmation
    read -p "Have you generated your PAT and copied it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_warning "Please generate your PAT first, then run this script again."
        exit 0
    fi

    log_success "Great! Now let's test your PAT..."
}

# Test GitHub authentication
test_github_auth() {
    log_step "Testing GitHub authentication..."

    echo
    echo "🔑 Testing your GitHub PAT..."
    echo "You'll be prompted for:"
    echo "  Username: your-github-username"
    echo "  Password: paste-your-PAT-here"
    echo

    # Test with a simple operation
    if git ls-remote "$WOOFY_REPO" &> /dev/null; then
        log_success "GitHub authentication successful!"
        log_info "Your PAT is working correctly."
    else
        log_error "GitHub authentication failed."
        log_info "Please check:"
        log_info "  • Your PAT is correct and not expired"
        log_info "  • Your GitHub username is correct"
        log_info "  • You have access to the WOOFY repository"
        log_info "  • Your PAT has the required scopes"
        exit 1
    fi
}

# Clone WOOFY repository
clone_woofy_repo() {
    log_step "Cloning WOOFY McWOOFSON repository..."

    if [[ -d "Woofy-Mcwoofson" ]]; then
        log_warning "WOOFY directory already exists. Skipping clone."
        cd Woofy-Mcwoofson
    else
        log_info "Cloning repository..."
        if git clone "$WOOFY_REPO"; then
            log_success "Repository cloned successfully!"
            cd Woofy-Mcwoofson
        else
            log_error "Failed to clone repository."
            log_info "Please check your authentication and try again."
            exit 1
        fi
    fi

    # Set up remotes
    git remote add upstream "$WOOFY_REPO" 2>/dev/null || true
    log_success "Repository setup completed"
}

# Setup development environment
setup_dev_environment() {
    log_step "Setting up development environment..."

    # Create .env file if it doesn't exist
    if [[ ! -f ".env" ]]; then
        cat > .env << 'EOF'
# WOOFY McWOOFSON Environment Configuration
# Add your API keys and configuration here
# NEVER commit this file to version control

# GitHub Configuration
GITHUB_TOKEN=your-github-pat-here

# AI Service API Keys (get from respective services)
PERPLEXITY_API_KEY=your-perplexity-key-here
OPENROUTER_API_KEY=your-openrouter-key-here
GEMINI_API_KEY=your-gemini-key-here

# AWS Configuration (if using AWS services)
AWS_REGION=us-east-1
AWS_PROFILE=default

# Development Settings
NODE_ENV=development
LOG_LEVEL=INFO
EOF
        log_success "Created .env template file"
        log_security "Remember to add your actual API keys to .env"
    fi

    # Install dependencies if requirements.txt exists
    if [[ -f "requirements.txt" ]]; then
        log_info "Installing Python dependencies..."
        pip install -r requirements.txt
        log_success "Python dependencies installed"
    fi

    # Setup pre-commit hooks if configured
    if [[ -f ".pre-commit-config.yaml" ]]; then
        log_info "Setting up pre-commit hooks..."
        pip install pre-commit
        pre-commit install
        log_success "Pre-commit hooks configured"
    fi
}

# Setup SSH keys (optional)
setup_ssh_keys() {
    log_step "SSH Key Setup (Optional but Recommended)"

    echo
    echo "SSH keys provide passwordless authentication and are more secure than tokens."
    read -p "Would you like to set up SSH keys for GitHub? (y/N): " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        local key_name="woofy-github-key"
        local key_path="$HOME/.ssh/$key_name"

        # Generate SSH key
        log_info "Generating SSH key..."
        ssh-keygen -t ed25519 -C "$(git config user.email)" -f "$key_path" -N ""

        # Start SSH agent
        eval "$(ssh-agent -s)"

        # Add key to agent
        ssh-add "$key_path"

        echo
        echo "╔════════════════════════════════════════════════════════════════╗"
        echo "║                     🔑 SSH PUBLIC KEY                         ║"
        echo "╠════════════════════════════════════════════════════════════════╣"
        echo "║  Copy this key and add it to GitHub:                         ║"
        echo "║  https://github.com/settings/ssh/new                         ║"
        echo "║                                                              ║"
        echo "║  Title: WOOFY-McWOOFSON-DEV-$(hostname)                      ║"
        echo "║                                                              ║"
        echo "╚════════════════════════════════════════════════════════════════╝"
        echo
        cat "${key_path}.pub"
        echo
        echo "══════════════════════════════════════════════════════════════════"
        echo

        log_success "SSH key generated and displayed above"
        log_info "Add the key to GitHub, then test with: ssh -T git@github.com"

        # Test SSH connection
        read -p "Have you added the SSH key to GitHub? Test connection now? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
                log_success "SSH authentication successful!"

                # Configure Git to use SSH
                git remote set-url origin "git@github.com:Bakery-street-projct/Woofy-McwoofSON.git"
                log_success "Repository remote updated to use SSH"
            else
                log_warning "SSH test failed. Please check your key was added correctly."
            fi
        fi
    else
        log_info "Skipping SSH setup. You can set it up later if needed."
    fi
}

# Final setup and verification
final_setup() {
    log_step "Final setup and verification..."

    # Verify Git configuration
    echo
    log_info "Git Configuration Summary:"
    echo "  User Name: $(git config user.name)"
    echo "  User Email: $(git config user.email)"
    echo "  Credential Helper: $(git config credential.helper)"
    echo "  Default Branch: $(git config init.defaultBranch)"
    echo "  Remote Origin: $(git remote get-url origin 2>/dev/null || echo 'Not set')"

    # Check repository status
    if [[ -d ".git" ]]; then
        echo "  Current Branch: $(git branch --show-current)"
        echo "  Repository Status: $(git status --porcelain | wc -l) changes"
    fi

    echo
    log_success "WOOFY McWOOFSON credential setup completed!"
    echo
    echo "🎯 Next Steps:"
    echo "  1. Add your API keys to the .env file"
    echo "  2. Run: git status (to see repository status)"
    echo "  3. Run: git pull (to get latest changes)"
    echo "  4. Start developing! 🚀"
    echo
    echo "📚 Useful Commands:"
    echo "  • git status          - Check repository status"
    echo "  • git log --oneline   - View commit history"
    echo "  • git branch -a       - List all branches"
    echo "  • git checkout <branch> - Switch branches"
    echo
    echo "🆘 Need Help?"
    echo "  • Docs: docs/git-credential-setup-guide.md"
    echo "  • Email: dev@woofymcwoofson.com"
    echo "  • Issues: https://github.com/Bakery-street-projct/Woofy-McwoofSON/issues"
}

# Main execution
main() {
    echo "🐕‍🦺 WOOFY McWOOFSON Secure Credential Setup Script v$SCRIPT_VERSION"
    echo "════════════════════════════════════════════════════════════════════"
    echo

    security_disclaimer
    check_requirements
    setup_git_config
    setup_credential_helper
    generate_github_pat
    test_github_auth
    clone_woofy_repo
    setup_dev_environment
    setup_ssh_keys
    final_setup

    echo
    echo "🎉 Setup complete! Welcome to the WOOFY McWOOFSON development pack!"
    echo "   Remember: 🔐 Security first - never share your credentials!"
}

# Run main function
main "$@"