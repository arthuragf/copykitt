set -e
docker rm -f layer-container 2>/dev/null || true
docker build -t base-layer .
docker run --name layer-container base-layer
docker cp base-layer:layer.zip ./layer.zip
docker rm -f layer-container