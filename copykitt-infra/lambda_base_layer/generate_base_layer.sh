docker build -t base-layer .
docker run --name layer-container base-layer
docker cp layer-container:/var/task/layer.zip ./layer.zip
docker rm -f layer-container