#!/bin/bash
# File: run_start.sh
# Purpose: Configure Git and set up the project environment and Jupyter kernel at SageMaker startup

echo "=== SageMaker startup script started ==="

# Stop on first error
set -e

# --- Helper Functions ---
log_success() {
    echo "✓ $1"
}

log_warning() {
    echo "⚠ $1"
}

# --- PARAMETERS ---
YOUR_USER_NAME="Mohit Sonkamble"
YOUR_EMAIL_ADDRESS="mohitseventeens@gmail.com"
ENV_FILE=".env"
PROJECT_FILE="pyproject.toml"
VENV_DIR=".venv"
KERNEL_NAME="green-agent-venv"
KERNEL_DISPLAY_NAME="Python (Green Agent)"

# --- Configure Git ---
echo "Configuring Git user for commits..."
git config --global user.name "$YOUR_USER_NAME"
git config --global user.email "$YOUR_EMAIL_ADDRESS"
log_success "Git config set to: $(git config --global user.name) <$(git config --global user.email)>"

# --- Configure Git credentials ---
echo "Setting up Git credentials..."
if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE"
    
    if [ -n "$AWS_SAGEMAKER_2_GITHUB_TOKEN" ]; then
        git config --global credential.helper 'store'
        echo "https://$YOUR_USER_NAME:$AWS_SAGEMAKER_2_GITHUB_TOKEN@github.com" > ~/.git-credentials
        log_success "Git credentials configured from $ENV_FILE."
    else
        log_warning "AWS_SAGEMAKER_2_GITHUB_TOKEN not found in $ENV_FILE. Skipping credential config."
    fi
else
    log_warning "$ENV_FILE not found. Skipping credential config."
fi

# --- Install uv ---
echo "Installing/updating uv..."
pip install --upgrade pip > /dev/null
pip install --upgrade uv > /dev/null
log_success "uv is installed."

# --- Setup Project Virtual Environment ---
if [ -f "$PROJECT_FILE" ]; then
    log_success "Found $PROJECT_FILE. Proceeding with environment setup."

    if [ ! -d "$VENV_DIR" ]; then
        echo "Virtual environment not found. Creating it..."
        uv venv > /dev/null
        log_success "Virtual environment created at $VENV_DIR."
    else
        log_success "Virtual environment already exists."
    fi

    echo "Installing/updating dependencies and kernel..."
    source "$VENV_DIR/bin/activate"
    
    uv sync > /dev/null
    uv pip install ipykernel > /dev/null
    log_success "Dependencies are up to date."
    
    # --- Register venv as a Jupyter Kernel ---
    KERNEL_PATH="$HOME/.local/share/jupyter/kernels/$KERNEL_NAME"
    if [ ! -d "$KERNEL_PATH" ]; then
        echo "Jupyter kernel '$KERNEL_DISPLAY_NAME' not found. Registering..."
        python -m ipykernel install --user --name="$KERNEL_NAME" --display-name="$KERNEL_DISPLAY_NAME" > /dev/null
        log_success "Kernel registered successfully."
    else
        log_success "Jupyter kernel '$KERNEL_DISPLAY_NAME' is already registered."
    fi
    
    deactivate
    log_success "Project environment is ready."
else
    log_warning "$PROJECT_FILE not found. Skipping project environment setup."
fi

echo "=== SageMaker startup script finished successfully ==="