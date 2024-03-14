#
#  Summary
#
# the build-arg BASE_IMAGE can either be
#   - static, repository reachable, images inside the Dockerfile
#   - static, pants targets, (relative, absolute, and parametrized)
#   - "dynamic", passed in via the extra_build_args, ONLY if FROM image value is a : repository reachable, images inside the Dockerfile
#
# ------------------------------------------------

#
# This example uses a public docker image as a base image, passed in via the build-arg BASE_IMAGE
# Status: Works - is: "dynamic", passed in via the extra_build_args, is a : repository reachable, image
docker_image(
  name="sample-external-image-via-build_args",
  source="Dockerfile",
  extra_build_args=["BASE_IMAGE=python:3.11"],
  dependencies= [
    "lib/my-simple-lib:simple_lib_wheel",
  ],
)

#
# This example uses a pants, built, parametrized (other BUILD file) as a base image, passed in via the build-arg BASE_IMAGE
# Status: Does NOT work. image target parsing happens at the Dockerfile, not to arguments being passed in.
docker_image(
  name="sample-other-pants-tgt-parametrized-image-relative-via-build_args",
  source="Dockerfile",
  extra_build_args=["BASE_IMAGE=containers/common:images-python@parametrize=py311deb"],
  dependencies= [
    "lib/my-simple-lib:simple_lib_wheel",
    "containers/common:images-python@parametrize=py311deb",
  ],
)

#
# This example uses a full path (//...) pants, built, parametrized (other BUILD file) as a base image, passed in via the build-arg BASE_IMAGE
# Status: Does NOT work. image target parsing happens at the Dockerfile, not to arguments being passed in.
docker_image(
  name="sample-other-pants-tgt-parametrized-image-absolute-via-build_args",
  source="Dockerfile",
  extra_build_args=["BASE_IMAGE=//containers/common:images-python@parametrize=py311deb"],
  dependencies= [
    "lib/my-simple-lib:simple_lib_wheel",
    "containers/common:images-python@parametrize=py311deb",
  ],
)


#
# This example uses a pants, built, non-parametrize'd (other BUILD file) as a base image, passed in via the build-arg BASE_IMAGE
# Status: Does NOT work. image target parsing happens at the Dockerfile, not to arguments being passed in.
docker_image(
  name="sample-other-pants-tgt-basic-image-relative-via-build_args",
  source="Dockerfile",
  extra_build_args=["BASE_IMAGE=containers/common:python-3-11-basic"],
  dependencies= [
    "lib/my-simple-lib:simple_lib_wheel",
    "containers/common:python-3-11-basic",
  ],
)

#
# this example works
# This example uses a a different Dockerfile, which has a value for BASE_IMAGE
# which inside has a "static" BASE_IMAGE, which is a pants, built, parametrize'd (other BUILD file) as a base image
# Status: Works - is: "static", pants targets inside the Dockerfile
docker_image(
  name="sample-other-pants-tgt-parametrized-image-via-static_in_dockerfile",
  source="Dockerfile.non-arg-arg",
  dependencies= [
    "lib/my-simple-lib:simple_lib_wheel",
    "//containers/common:images-python@parametrize=py311deb",
  ],
)