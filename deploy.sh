#!/bin/sh
set -eu

IMAGE="ghcr.io/dbremont/tecnica:latest"
CONTAINER="tecnica"
PORT="${TECNICA_PORT:-8000}"

cd "$(dirname "$0")"

# Mount the repo's .env into the container; bin/envutil.py reads it from
# /srv/.env (repo root next to bin/). Real env vars still win (setdefault).
ENV_MOUNT=""
if [ -f .env ]; then
  ENV_MOUNT="-v ${PWD}/.env:/srv/.env:ro"
fi

docker pull "$IMAGE"
docker rm -f "$CONTAINER" 2>/dev/null || true
# shellcheck disable=SC2086
exec docker run -d --name "$CONTAINER" --restart unless-stopped \
  --network host \
  $ENV_MOUNT \
  "$IMAGE" \
  python bin/sync.py --root app --port "$PORT"
