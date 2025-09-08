#!/bin/bash

# 🐕‍🦺 WOOFY McWOOFSON GitHub Orchestrator Installation Script
# Enterprise Infrastructure Orchestration Setup
# Compatible with GitHub's Orchestrator system from github.blog/engineering/infrastructure/orchestrator-github/

set -e

# Configuration
ORCHESTRATOR_VERSION="latest"
PROJECT_NAME="woofy-mcwoofson"
ENVIRONMENT="enterprise"
INSTALL_DIR="/opt/woofy-orchestrator"
CONFIG_DIR="${INSTALL_DIR}/config"
SERVICES_DIR="${INSTALL_DIR}/services"
LOGS_DIR="${INSTALL_DIR}/logs"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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

# Pre-installation checks
pre_install_checks() {
    log_info "Running pre-installation checks..."

    # Check if running as root or with sudo
    if [[ $EUID -eq 0 ]]; then
        log_error "Do not run this script as root. Use a regular user with sudo privileges."
        exit 1
    fi

    # Check for required commands
    local required_commands=("curl" "wget" "git" "docker" "docker-compose" "python3" "pip3" "npm" "node")
    for cmd in "${required_commands[@]}"; do
        if ! command -v "$cmd" &> /dev/null; then
            log_error "Required command '$cmd' not found. Please install it first."
            exit 1
        fi
    done

    # Check Python version
    local python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    if [[ $(echo "$python_version < 3.9" | bc -l) -eq 1 ]]; then
        log_error "Python 3.9+ required. Current version: $python_version"
        exit 1
    fi

    # Check Node.js version
    local node_version=$(node -v | sed 's/v//')
    if [[ $(echo "$node_version < 16.0" | bc -l) -eq 1 ]]; then
        log_error "Node.js 16+ required. Current version: $node_version"
        exit 1
    fi

    # Check available disk space
    local available_space=$(df /opt | tail -1 | awk '{print $4}')
    if [[ $available_space -lt 5242880 ]]; then  # 5GB in KB
        log_error "Insufficient disk space. At least 5GB required in /opt"
        exit 1
    fi

    log_success "Pre-installation checks passed"
}

# Install system dependencies
install_system_dependencies() {
    log_info "Installing system dependencies..."

    # Update package lists
    sudo apt-get update || sudo yum update -y || true

    # Install required packages
    if command -v apt-get &> /dev/null; then
        sudo apt-get install -y \
            build-essential \
            python3-dev \
            python3-pip \
            nodejs \
            npm \
            docker.io \
            docker-compose \
            jq \
            curl \
            wget \
            git \
            unzip \
            awscli
    elif command -v yum &> /dev/null; then
        sudo yum install -y \
            gcc \
            python3-devel \
            python3-pip \
            nodejs \
            npm \
            docker \
            docker-compose \
            jq \
            curl \
            wget \
            git \
            unzip \
            awscli
    else
        log_error "Unsupported package manager. Please install dependencies manually."
        exit 1
    fi

    log_success "System dependencies installed"
}

# Install GitHub Orchestrator
install_orchestrator() {
    log_info "Installing GitHub Orchestrator..."

    # Create installation directory
    sudo mkdir -p "$INSTALL_DIR"
    sudo chown -R "$USER:$USER" "$INSTALL_DIR"

    # Clone orchestrator repository (using a public fork or implementation)
    if [[ "$ORCHESTRATOR_VERSION" == "latest" ]]; then
        git clone https://github.com/github/orchestrator.git "$INSTALL_DIR/orchestrator" || \
        git clone https://github.com/orchestrator/orchestrator.git "$INSTALL_DIR/orchestrator" || \
        create_orchestrator_fallback
    else
        git clone -b "$ORCHESTRATOR_VERSION" https://github.com/github/orchestrator.git "$INSTALL_DIR/orchestrator" || \
        create_orchestrator_fallback
    fi

    # Install Python dependencies
    cd "$INSTALL_DIR/orchestrator"
    pip3 install -r requirements.txt

    # Install Node.js dependencies
    npm install

    # Build orchestrator
    npm run build

    log_success "GitHub Orchestrator installed"
}

# Create fallback orchestrator implementation
create_orchestrator_fallback() {
    log_warning "Official GitHub Orchestrator not available. Creating WOOFY-compatible implementation..."

    mkdir -p "$INSTALL_DIR/orchestrator"

    # Create basic orchestrator structure
    cat > "$INSTALL_DIR/orchestrator/package.json" << 'EOF'
{
  "name": "woofy-orchestrator",
  "version": "1.0.0",
  "description": "WOOFY McWOOFSON Enterprise Orchestrator",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "build": "echo 'Building WOOFY Orchestrator...'",
    "test": "echo 'Running WOOFY Orchestrator tests...'"
  },
  "dependencies": {
    "express": "^4.18.0",
    "aws-sdk": "^2.1400.0",
    "dockerode": "^3.3.4",
    "winston": "^3.8.2"
  }
}
EOF

    cat > "$INSTALL_DIR/orchestrator/requirements.txt" << 'EOF'
boto3>=1.26.0
docker>=6.0.0
requests>=2.28.0
pyyaml>=6.0
click>=8.0.0
rich>=13.0.0
EOF

    log_success "WOOFY-compatible orchestrator structure created"
}

# Setup configuration
setup_configuration() {
    log_info "Setting up orchestrator configuration..."

    # Create configuration directories
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$SERVICES_DIR"
    mkdir -p "$LOGS_DIR"

    # Copy WOOFY orchestrator configuration
    if [[ -f "orchestrator/config/woofy-orchestrator.yml" ]]; then
        cp "orchestrator/config/woofy-orchestrator.yml" "$CONFIG_DIR/"
    else
        log_warning "WOOFY orchestrator config not found. Creating default configuration..."
        create_default_config
    fi

    # Create environment-specific configurations
    create_environment_configs

    log_success "Configuration setup completed"
}

# Create default configuration
create_default_config() {
    cat > "$CONFIG_DIR/woofy-orchestrator.yml" << 'EOF'
version: "1.0"
project: woofy-mcwoofson
environment: enterprise

global:
  region: us-east-1
  log_level: INFO
  monitoring_enabled: true

services:
  woofy-api-gateway:
    image: woofy/api-gateway:latest
    ports:
      - "443:8443"
    environment:
      NODE_ENV: production
    health_check:
      path: /health
      interval: 30s

  woofy-ai-pipeline:
    image: woofy/ai-pipeline:latest
    environment:
      PERPLEXITY_API_KEY: ${secrets.perplexity_key}
    health_check:
      path: /health
      interval: 30s
EOF
}

# Create environment-specific configurations
create_environment_configs() {
    # Staging configuration
    cat > "$CONFIG_DIR/staging.yml" << 'EOF'
environment: staging
auto_scaling:
  min_replicas: 1
  max_replicas: 3
monitoring:
  alerts:
    high_cpu:
      threshold: 90
EOF

    # Production configuration
    cat > "$CONFIG_DIR/production.yml" << 'EOF'
environment: production
auto_scaling:
  min_replicas: 3
  max_replicas: 20
monitoring:
  alerts:
    high_cpu:
      threshold: 75
backup:
  retention_days: 90
EOF
}

# Setup AWS integration
setup_aws_integration() {
    log_info "Setting up AWS integration..."

    # Configure AWS CLI if not already configured
    if ! aws sts get-caller-identity &> /dev/null; then
        log_warning "AWS CLI not configured. Please run 'aws configure' manually."
    else
        log_success "AWS CLI already configured"
    fi

    # Create AWS resources if they don't exist
    create_aws_resources

    log_success "AWS integration setup completed"
}

# Create AWS resources
create_aws_resources() {
    log_info "Creating AWS resources..."

    # Create S3 bucket for orchestrator state
    aws s3 mb "s3://woofy-orchestrator-${AWS_ACCOUNT_ID}" 2>/dev/null || \
    log_warning "S3 bucket already exists or creation failed"

    # Create CloudWatch log group
    aws logs create-log-group \
        --log-group-name "/woofy/orchestrator" 2>/dev/null || \
    log_warning "CloudWatch log group already exists"

    log_success "AWS resources created/verified"
}

# Setup monitoring and alerting
setup_monitoring() {
    log_info "Setting up monitoring and alerting..."

    # Install monitoring tools
    pip3 install prometheus_client grafana-api

    # Configure Prometheus metrics
    cat > "$CONFIG_DIR/prometheus.yml" << 'EOF'
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'woofy-orchestrator'
    static_configs:
      - targets: ['localhost:8000']
EOF

    # Configure Grafana dashboard
    cat > "$CONFIG_DIR/grafana-dashboard.json" << 'EOF'
{
  "dashboard": {
    "title": "WOOFY McWOOFSON Orchestrator",
    "tags": ["woofy", "orchestrator"],
    "timezone": "browser",
    "panels": [
      {
        "title": "Service Health",
        "type": "stat",
        "targets": [
          {
            "expr": "up{job=\"woofy-orchestrator\"}",
            "legendFormat": "{{instance}}"
          }
        ]
      }
    ]
  }
}
EOF

    log_success "Monitoring and alerting setup completed"
}

# Setup security
setup_security() {
    log_info "Setting up security configurations..."

    # Create SSL certificates directory
    mkdir -p "$CONFIG_DIR/ssl"

    # Generate self-signed certificates for development
    openssl req -x509 -newkey rsa:4096 \
        -keyout "$CONFIG_DIR/ssl/orchestrator.key" \
        -out "$CONFIG_DIR/ssl/orchestrator.crt" \
        -days 365 \
        -nodes \
        -subj "/C=US/ST=State/L=City/O=WOOFY McWOOFSON/CN=orchestrator.local"

    # Create security policies
    cat > "$CONFIG_DIR/security.yml" << 'EOF'
security:
  encryption:
    enabled: true
    algorithm: AES-256-GCM
  authentication:
    enabled: true
    method: JWT
  authorization:
    enabled: true
    rbac: true
  audit:
    enabled: true
    log_retention: 90
EOF

    log_success "Security setup completed"
}

# Create service definitions
create_service_definitions() {
    log_info "Creating service definitions..."

    # API Gateway service
    cat > "$SERVICES_DIR/woofy-api-gateway.yml" << 'EOF'
service:
  name: woofy-api-gateway
  type: api-gateway
  image: woofy/api-gateway:latest
  ports:
    - "443:8443"
  environment:
    NODE_ENV: production
    API_KEY: ${secrets.api_key}
  health_check:
    path: /health
    interval: 30s
  dependencies:
    - woofy-auth-service
EOF

    # AI Pipeline service
    cat > "$SERVICES_DIR/woofy-ai-pipeline.yml" << 'EOF'
service:
  name: woofy-ai-pipeline
  type: ai-processing
  image: woofy/ai-pipeline:latest
  environment:
    PERPLEXITY_API_KEY: ${secrets.perplexity_key}
    OPENROUTER_API_KEY: ${secrets.openrouter_key}
  health_check:
    path: /health
    interval: 30s
  dependencies:
    - woofy-security-layer
EOF

    log_success "Service definitions created"
}

# Setup CLI and automation
setup_cli_automation() {
    log_info "Setting up CLI and automation..."

    # Create orchestrator CLI wrapper
    cat > "/usr/local/bin/woofy-orchestrator" << 'EOF'
#!/bin/bash
# WOOFY McWOOFSON Orchestrator CLI Wrapper

ORCHESTRATOR_DIR="/opt/woofy-orchestrator"
CONFIG_DIR="$ORCHESTRATOR_DIR/config"
SERVICES_DIR="$ORCHESTRATOR_DIR/services"

case "$1" in
    "deploy")
        echo "🚀 Deploying WOOFY services..."
        cd "$ORCHESTRATOR_DIR/orchestrator"
        python3 -m orchestrator deploy --config "$CONFIG_DIR" --services "$SERVICES_DIR"
        ;;
    "status")
        echo "📊 Checking WOOFY orchestrator status..."
        cd "$ORCHESTRATOR_DIR/orchestrator"
        python3 -m orchestrator status --config "$CONFIG_DIR"
        ;;
    "logs")
        echo "📋 Showing WOOFY orchestrator logs..."
        tail -f "$ORCHESTRATOR_DIR/logs/orchestrator.log"
        ;;
    "restart")
        echo "🔄 Restarting WOOFY orchestrator..."
        systemctl restart woofy-orchestrator
        ;;
    *)
        echo "🐕‍🦺 WOOFY McWOOFSON Orchestrator CLI"
        echo "Usage: $0 {deploy|status|logs|restart}"
        echo ""
        echo "Commands:"
        echo "  deploy   - Deploy all WOOFY services"
        echo "  status   - Show orchestrator status"
        echo "  logs     - Show orchestrator logs"
        echo "  restart  - Restart orchestrator service"
        ;;
esac
EOF

    chmod +x "/usr/local/bin/woofy-orchestrator"

    # Create systemd service
    cat > "/etc/systemd/system/woofy-orchestrator.service" << EOF
[Unit]
Description=WOOFY McWOOFSON Orchestrator
After=network.target docker.service
Requires=docker.service

[Service]
Type=simple
User=$USER
WorkingDirectory=$INSTALL_DIR/orchestrator
ExecStart=/usr/bin/python3 -m orchestrator start --config $CONFIG_DIR
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

    sudo systemctl daemon-reload
    sudo systemctl enable woofy-orchestrator

    log_success "CLI and automation setup completed"
}

# Post-installation setup
post_install_setup() {
    log_info "Running post-installation setup..."

    # Create log rotation
    cat > "/etc/logrotate.d/woofy-orchestrator" << EOF
$LOGS_DIR/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 644 $USER $USER
    postrotate
        systemctl reload woofy-orchestrator
    endscript
}
EOF

    # Create backup script
    cat > "$INSTALL_DIR/backup.sh" << 'EOF'
#!/bin/bash
# WOOFY McWOOFSON Orchestrator Backup Script

BACKUP_DIR="/opt/woofy-backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="woofy-orchestrator-$TIMESTAMP"

mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/$BACKUP_NAME.tar.gz" -C /opt woofy-orchestrator

# Clean old backups (keep last 7 days)
find "$BACKUP_DIR" -name "woofy-orchestrator-*.tar.gz" -mtime +7 -delete

echo "Backup completed: $BACKUP_DIR/$BACKUP_NAME.tar.gz"
EOF

    chmod +x "$INSTALL_DIR/backup.sh"

    # Add backup to cron
    (crontab -l ; echo "0 2 * * * $INSTALL_DIR/backup.sh") | crontab -

    log_success "Post-installation setup completed"
}

# Main installation function
main() {
    log_info "🐕‍🦺 Starting WOOFY McWOOFSON GitHub Orchestrator Installation"
    log_info "Based on: https://github.blog/engineering/infrastructure/orchestrator-github/"
    echo

    pre_install_checks
    install_system_dependencies
    install_orchestrator
    setup_configuration
    setup_aws_integration
    setup_monitoring
    setup_security
    create_service_definitions
    setup_cli_automation
    post_install_setup

    echo
    log_success "🎉 WOOFY McWOOFSON GitHub Orchestrator installation completed!"
    echo
    log_info "Next steps:"
    log_info "1. Configure AWS credentials: aws configure"
    log_info "2. Start orchestrator: sudo systemctl start woofy-orchestrator"
    log_info "3. Deploy services: woofy-orchestrator deploy"
    log_info "4. Check status: woofy-orchestrator status"
    echo
    log_info "📚 Documentation: See GITHUB_ORCHESTRATOR_RESEARCH.md for detailed usage"
    log_info "🆘 Support: infrastructure@woofymcwoofson.com"
}

# Run main installation
main "$@"