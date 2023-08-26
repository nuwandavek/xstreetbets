#!/bin/sh
gunicorn \
--bind 0.0.0.0:5000 \
--worker-class aiohttp.GunicornWebWorker \
--workers 4 \
--threads 2 \
--worker-connections 1000 \
--error-logfile /dev/stderr \
--access-logfile /dev/stdout \
--forwarded-allow-ips '*' \
--log-level debug \
--preload \
app:xsb