#!/bin/bash

set -e

# Remove container antigo (se existir)
docker rm -f layer-container 2>/dev/null || true

# Build da imagem
docker build -t base-layer .

# Cria container
docker run --name layer-container base-layer

# Copia o zip gerado
docker cp layer-container:/opt/layer.zip . && echo "✅ layer.zip gerado com sucesso!"
