#!/bin/bash
# File: run_start.sh
# Purpose: Configure Git and install uv at SageMaker startup

echo "=== SageMaker startup script started ==="

# Stop on first error
set -e

# PARAMETERS
YOUR_USER_NAME="Mohit Sonkamble"
YOUR_EMAIL_ADDRESS="mohitseventeens@gmail.com"

# --- Configure Git ---
echo "Configuring Git user..."
git config --global user.name "$YOUR_USER_NAME"
git config --global user.email "$YOUR_EMAIL_ADDRESS"
echo "Git config set to: $(git config --global user.name) <$(git config --global user.email)>"

# --- Install uv ---
echo "Installing uv via pip..."
pip install --upgrade pip
pip install --upgrade uv

echo "uv installation complete."
echo "=== SageMaker startup script finished successfully ==="