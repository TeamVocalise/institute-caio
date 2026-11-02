#!/bin/bash
cd "$(dirname "$0")"
echo "ICAIO draft: http://localhost:8080  (Ctrl+C to stop)"
(sleep 1; open http://localhost:8080) &
python3 -m http.server 8080
