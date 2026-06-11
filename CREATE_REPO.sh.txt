#!/bin/bash

echo "Animate Pro - Repository Setup"
echo ""
read -p "Enter your GitHub username: " GITHUB_USERNAME
echo ""
echo "IMPORTANT: Create repository at https://github.com/new"
echo "1. Repository name: animate-pro"
echo "2. Do NOT initialize with README/gitignore"
echo ""
read -p "Press Enter once created..."

git init
git remote add origin https://github.com/$GITHUB_USERNAME/animate-pro.git
git add .
git commit -m "Initial commit - Animate Pro: AI Video Animation Studio"
git branch -M main
git push -u origin main

echo ""
echo "✅ Repository created and pushed!"
echo "📍 https://github.com/$GITHUB_USERNAME/animate-pro"