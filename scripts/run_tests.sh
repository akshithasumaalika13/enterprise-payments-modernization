#!/usr/bin/env bash
set -euo pipefail
python -m pytest -q api/tests tests
python -m compileall api streaming data_quality synthetic_data
