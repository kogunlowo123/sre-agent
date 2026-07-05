#!/bin/bash
set -euo pipefail
echo "Setting up SRE Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
