#!/bin/bash
cd "/Users/richard/src/github.com/64bitAI/agents"

# Check if it's a market day (Monday-Friday)
if [ $(date +%u) -le 5 ]; then
    claude code --directory '/Users/richard/src/github.com/64bitAI/agents' --message '/statusline && /alerts'
else
    echo "Skipping market_open - not a market day"
fi
