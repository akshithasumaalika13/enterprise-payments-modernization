#!/usr/bin/env bash
set -euo pipefail
curl -fsS http://localhost:8000/health | jq .
curl -fsS http://localhost:9090/-/healthy
echo "Health checks passed"
