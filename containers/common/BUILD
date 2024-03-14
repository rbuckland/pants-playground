# Python base containers with TLS internal CA certs
docker_image(
  name="images-python",
  source="Dockerfile.python",
  **parametrize("py310deb", repository="python", image_tags=["3.10-slim"],   extra_build_args=["BASE_IMAGE=python:3.10-slim","DIST_TYPE=debian:12"]),
  **parametrize("py311deb", repository="python", image_tags=["3.11-slim"],   extra_build_args=["BASE_IMAGE=python:3.11-slim","DIST_TYPE=debian:12"]),
  **parametrize("py312deb", repository="python", image_tags=["3.12-slim"],   extra_build_args=["BASE_IMAGE=python:3.12-slim","DIST_TYPE=debian:12"]),
  **parametrize("py310alpine", repository="python", image_tags=["3.10-alpine"], extra_build_args=["BASE_IMAGE=python:3.10-alpine", "DIST_TYPE=alpine:3"]),
  **parametrize("py311alpine", repository="python", image_tags=["3.11-alpine"], extra_build_args=["BASE_IMAGE=python:3.11-alpine", "DIST_TYPE=alpine:3"]),
  **parametrize("py312alpine", repository="python", image_tags=["3.12-alpine"], extra_build_args=["BASE_IMAGE=python:3.12-alpine", "DIST_TYPE=alpine:3"]),
)

docker_image(
  name="python-3-11-basic",
  source="Dockerfile.python",
  repository="python",
  image_tags=["3.11-slim"],
  extra_build_args=["BASE_IMAGE=python:3.11-slim","DIST_TYPE=debian:12"],
)

