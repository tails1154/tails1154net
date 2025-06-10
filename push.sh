#!/bin/bash

# Stage all changes
git add .

# Prompt for commit message
read -p "Enter commit message: " commitmsg

# Prevent empty commits
if [ -z "$commitmsg" ]; then
  echo "Commit message cannot be empty."
  exit 1
fi

# Commit and push
git commit -m "$commitmsg" && git push

# Check if main.py exists before running
if [ -f main.py ]; then
  python3 main.py
else
  echo "main.py not found."
fi
