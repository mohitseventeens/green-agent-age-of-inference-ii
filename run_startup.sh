#!/bin/bash
# File: run_start.sh
# Purpose: Configure Git and install uv at SageMaker startup

echo "=== SageMaker startup script started ==="

# Stop on first error
set -e

# PARAMETERS
YOUR_USER_NAME="Mohit Sonkamble"
YOUR_EMAIL_ADDRESS="mohitseventeens@gmail.com"
ENV_FILE=".env"

# --- Configure Git ---
echo "Configuring Git user..."
git config --global user.name "$YOUR_USER_NAME"
git config --global user.email "$YOUR_EMAIL_ADDRESS"
echo "Git config set to: $(git config --global user.name) <$(git config --global user.email)>"

# --- Configure Git credentials ---
echo "Setting up Git credentials..."

# Check if .env file exists
if [ -f "$ENV_FILE" ]; then
    echo "Loading GitHub token from $ENV_FILE..."
    # Source the .env file to load environment variables
    source "$ENV_FILE"
    
    # Check if token variable exists
    if [ -n "$AWS_SAGEMAKER_2_GITHUB_TOKEN" ]; then
        echo "Configuring Git credential store..."
        
        # Configure Git to store credentials
        git config --global credential.helper 'store'
        
        # Create a temporary file to trigger credential storage
        # The first git operation will store the credentials
        echo "https://$YOUR_USER_NAME:$AWS_SAGEMAKER_2_GITHUB_TOKEN@github.com" > ~/.git-credentials
        
        echo "Git credentials configured successfully."
    else
        echo "Warning: AWS_SAGEMAKER_2_GITHUB_TOKEN not found in $ENV_FILE"
        echo "Git credential configuration skipped."
    fi
else
    echo "Warning: $ENV_FILE not found. Git credential configuration skipped."
fi

# --- Install uv ---
echo "Installing uv via pip..."
pip install --upgrade pip
pip install --upgrade uv

echo "uv installation complete."
echo "=== SageMaker startup script finished successfully ==="