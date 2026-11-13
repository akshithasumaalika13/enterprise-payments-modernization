#!/usr/bin/env bash
set -euo pipefail
cp -n .env.example .env || true
python synthetic_data/generate.py
echo "Environment prepared. Next: docker compose up --build"
