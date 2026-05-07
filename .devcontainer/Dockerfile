FROM debian:bookworm-slim

# Evita prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instala o uv (binários oficiais)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Instala dependências essenciais de sistema e SSH (necessário para o DevPod)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    curl \
    build-essential \
    ssh \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Cria o usuário 'dev' para evitar rodar como root
RUN useradd -m -s /bin/bash dev
USER dev
WORKDIR /workspaces