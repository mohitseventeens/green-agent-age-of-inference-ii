#!/bin/bash
# File: run_start.sh
# Purpose: Configure Git and set up the project environment and Jupyter kernel at SageMaker startup

echo "=== SageMaker startup script started ==="

# Stop on first error
set -e

# --- PARAMETERS ---
YOUR_GITHUB_USERNAME="mohitseventeens"
YOUR_USER_NAME="Mohit Sonkamble" # This is for commit author name
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
echo "Git config set to: $(git config --global user.name) <$(git config --global user.email)>"

# --- Configure Git credentials ---
echo "Setting up Git credentials..."
if [ -f "$ENV_FILE" ]; then
    echo "Loading GitHub token from $ENV_FILE..."
    source "$ENV_FILE"
    
    if [ -n "$AWS_SAGEMAKER_2_GITHUB_TOKEN" ]; then
        echo "Configuring Git credential store..."
        git config --global credential.helper 'store'
        
        # CHANGE #2: Use the correct GitHub username for the credential URL
        echo "https://$YOUR_GITHUB_USERNAME:$AWS_SAGEMAKER_2_GITHUB_TOKEN@github.com" > ~/.git-credentials
        
        echo "Git credentials configured successfully."
    else
        echo "Warning: AWS_SAGEMAKER_2_GITHUB_TOKEN not found in $ENV_FILE. Git credential configuration skipped."
    fi
else
    echo "Warning: $ENV_FILE not found. Git credential configuration skipped."
fi

# --- Install/Update uv ---
echo "Installing/updating uv via pip..."
pip install --upgrade pip
pip install --upgrade uv
echo "uv installation complete."

# --- Setup Project Virtual Environment and Jupyter Kernel ---
if [ -f "$PROJECT_FILE" ]; then
    echo "Found $PROJECT_FILE. Setting up project environment..."

    if [ ! -d "$VENV_DIR" ]; then
        echo "Virtual environment not found. Creating it now..."
        uv venv
    else
        echo "Virtual environment already exists."
    fi

    source "$VENV_DIR/bin/activate"

    echo "Installing/updating dependencies from $PROJECT_FILE..."
    uv pip install .
    
    echo "Ensuring ipykernel is installed..."
    uv pip install ipykernel

    KERNEL_PATH="$HOME/.local/share/jupyter/kernels/$KERNEL_NAME"
    if [ ! -d "$KERNEL_PATH" ]; then
        echo "Jupyter kernel '$KERNEL_DISPLAY_NAME' not found. Registering it now..."
        python -m ipykernel install --user --name="$KERNEL_NAME" --display-name="$KERNEL_DISPLAY_NAME"
        echo "Kernel registered."
    else
        echo "Jupyter kernel '$KERNEL_DISPLAY_NAME' is already registered."
    fi
    
    deactivate
    
    echo "Project environment is ready and registered with Jupyter."
else
    echo "Warning: $PROJECT_FILE not found. Skipping project environment setup."
fi

echo "=== SageMaker startup script finished successfully ==="