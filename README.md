# pants-playground

This repository showcases, and is used for debugging various pants repo plugin setups etc.

## 1. Setup Kwargs Override

A custom plugin to read in a file for the version, and a file for the description of a wheel.

* [tools/pants-plugins/pinchworms/src/pinchworms/](tools/pants-plugins/pinchworms/src/pinchworms/)

```
python_distribution(
    name = "simple_lib_wheel",
    dependencies = [
        "./src:sources",
        ":reqs"
    ],
    generate_setup = True,
    provides = python_artifact(
        name = "my_simple_lib",
        version_file = "VERSION",                   # <---- HERE
        long_description_file = "README.md",        # <---- HERE
    ),
)
```

**Usage**
The `VERSION` file, is used as the version for the wheel.
```
❯  pants package lib/my-simple-lib::
08:05:46.75 [INFO] Wrote dist/my_simple_lib-4.3.1-py3-none-any.whl
08:05:46.75 [INFO] Wrote dist/my_simple_lib-4.3.1.tar.gz
```

The plugin, [tools/pants-plugins/pinchworms/src/pinchworms/packaging/setup_kwargs.py](tools/pants-plugins/pinchworms/src/pinchworms/packaging/setup_kwargs.py) reads the `VERSION` file and the `README.md`, into the wheel.

```
❯ unzip -p dist/my_simple_lib-4.3.1-py3-none-any.whl my_simple_lib-4.3.1.dist-info/METADATA
Metadata-Version: 2.1
Name: my-simple-lib
Version: 4.3.1
Requires-Python: <3.12,>=3.10

# my-simple-lib

bunch of fibonacci fns
```

## 2. Exploring pants target docker inference

```
❯ pants list containers/sample:: | xargs -Ixx sh -c "echo ======= xx; pants package xx 2>&1 | sed 's#^#  #'"
======= containers/sample:sample-external-image-via-build_args
  08:10:44.95 [INFO] Starting: Building docker image sample-external-image-via-build_args:latest
  08:10:53.83 [INFO] Completed: Building docker image sample-external-image-via-build_args:latest
  08:10:53.84 [INFO] Wrote dist/containers.sample/sample-external-image-via-build_args.docker-info.json
  Built docker image: sample-external-image-via-build_args:latest
  Docker image ID: sha256:fed834eb510decd18e8cdc0e4abf9b1d8ecb293f58941cd616f7725ce0e00479
======= containers/sample:sample-other-pants-tgt-basic-image-relative-via-build_args
  08:11:00.68 [INFO] Starting: Building docker image python:3.11-slim
  08:11:03.16 [INFO] Completed: Building docker image python:3.11-slim
  08:11:03.16 [INFO] Starting: Building docker image sample-other-pants-tgt-basic-image-relative-via-build_args:latest
  08:11:05.01 [INFO] Completed: Building docker image sample-other-pants-tgt-basic-image-relative-via-build_args:latest
  08:11:05.01 [WARN] Docker build failed for `docker_image` containers/sample:sample-other-pants-tgt-basic-image-relative-via-build_args. There are files in the Docker build context that were not referenced by any `COPY` instruction (this is not an error):

    * containers.common/python-3-11-basic.docker-info.json
    * my_simple_lib-4.3.1-py3-none-any.whl
    * my_simple_lib-4.3.1.tar.gz


  08:11:05.01 [ERROR] 1 Exception encountered:

  Engine traceback:
    in `package` goal

  ProcessExecutionFailure: Process 'Building docker image sample-other-pants-tgt-basic-image-relative-via-build_args:latest' failed with exit code 1.
  stdout:

  stderr:
  #0 building with "default" instance using docker driver

  #1 [internal] load .dockerignore
  #1 transferring context: 2B done
  #1 DONE 0.0s

  #2 [internal] load build definition from Dockerfile
  #2 transferring dockerfile: 115B done
  #2 DONE 0.0s

  #3 [internal] load metadata for docker.io/containers/common:python-3-11-basic
  #3 ERROR: pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
  ------
   > [internal] load metadata for docker.io/containers/common:python-3-11-basic:
  ------
  Dockerfile:2
  --------------------
     1 |     ARG BASE_IMAGE
     2 | >>> FROM $BASE_IMAGE
     3 |
     4 |     RUN apt update && apt install -y \
  --------------------
  ERROR: failed to solve: containers/common:python-3-11-basic: pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed



  Use `--keep-sandboxes=on_failure` to preserve the process chroot for inspection.

======= containers/sample:sample-other-pants-tgt-parametrized-image-absolute-via-build_args
  08:11:12.22 [INFO] Starting: Building docker image python:3.11-slim
  08:11:13.82 [INFO] Completed: Building docker image python:3.11-slim
  08:11:13.83 [INFO] Starting: Building docker image sample-other-pants-tgt-parametrized-image-absolute-via-build_args:latest
  08:11:13.93 [INFO] Completed: Building docker image sample-other-pants-tgt-parametrized-image-absolute-via-build_args:latest
  08:11:13.94 [WARN] Docker build failed for `docker_image` containers/sample:sample-other-pants-tgt-parametrized-image-absolute-via-build_args. There are files in the Docker build context that were not referenced by any `COPY` instruction (this is not an error):

    * containers.common/images-python@parametrize=py311deb.docker-info.json
    * my_simple_lib-4.3.1-py3-none-any.whl
    * my_simple_lib-4.3.1.tar.gz


  08:11:13.94 [ERROR] 1 Exception encountered:

  Engine traceback:
    in `package` goal

  ProcessExecutionFailure: Process 'Building docker image sample-other-pants-tgt-parametrized-image-absolute-via-build_args:latest' failed with exit code 1.
  stdout:

  stderr:
  #0 building with "default" instance using docker driver

  #1 [internal] load .dockerignore
  #1 transferring context: 2B done
  #1 DONE 0.0s

  #2 [internal] load build definition from Dockerfile
  #2 transferring dockerfile: 115B done
  #2 DONE 0.0s
  Dockerfile:2
  --------------------
     1 |     ARG BASE_IMAGE
     2 | >>> FROM $BASE_IMAGE
     3 |
     4 |     RUN apt update && apt install -y \
  --------------------
  ERROR: failed to solve: failed to parse stage name "//containers/common:images-python@parametrize=py311deb": invalid reference format



  Use `--keep-sandboxes=on_failure` to preserve the process chroot for inspection.

======= containers/sample:sample-other-pants-tgt-parametrized-image-relative-via-build_args
  08:11:20.97 [INFO] Starting: Building docker image python:3.11-slim
  08:11:22.59 [INFO] Completed: Building docker image python:3.11-slim
  08:11:22.59 [INFO] Starting: Building docker image sample-other-pants-tgt-parametrized-image-relative-via-build_args:latest
  08:11:22.70 [INFO] Completed: Building docker image sample-other-pants-tgt-parametrized-image-relative-via-build_args:latest
  08:11:22.70 [WARN] Docker build failed for `docker_image` containers/sample:sample-other-pants-tgt-parametrized-image-relative-via-build_args. There are files in the Docker build context that were not referenced by any `COPY` instruction (this is not an error):

    * containers.common/images-python@parametrize=py311deb.docker-info.json
    * my_simple_lib-4.3.1-py3-none-any.whl
    * my_simple_lib-4.3.1.tar.gz


  08:11:22.70 [ERROR] 1 Exception encountered:

  Engine traceback:
    in `package` goal

  ProcessExecutionFailure: Process 'Building docker image sample-other-pants-tgt-parametrized-image-relative-via-build_args:latest' failed with exit code 1.
  stdout:

  stderr:
  #0 building with "default" instance using docker driver

  #1 [internal] load .dockerignore
  #1 transferring context: 2B done
  #1 DONE 0.0s

  #2 [internal] load build definition from Dockerfile
  #2 transferring dockerfile: 115B done
  #2 DONE 0.0s
  Dockerfile:2
  --------------------
     1 |     ARG BASE_IMAGE
     2 | >>> FROM $BASE_IMAGE
     3 |
     4 |     RUN apt update && apt install -y \
  --------------------
  ERROR: failed to solve: failed to parse stage name "containers/common:images-python@parametrize=py311deb": invalid reference format



  Use `--keep-sandboxes=on_failure` to preserve the process chroot for inspection.

======= containers/sample:sample-other-pants-tgt-parametrized-image-via-static_in_dockerfile
  08:11:29.59 [INFO] Starting: Building docker image python:3.11-slim
  08:11:31.23 [INFO] Completed: Building docker image python:3.11-slim
  08:11:31.24 [INFO] Starting: Building docker image sample-other-pants-tgt-parametrized-image-via-static_in_dockerfile:latest
  08:11:35.83 [INFO] Completed: Building docker image sample-other-pants-tgt-parametrized-image-via-static_in_dockerfile:latest
  08:11:35.83 [INFO] Wrote dist/containers.sample/sample-other-pants-tgt-parametrized-image-via-static_in_dockerfile.docker-info.json
  Built docker image: sample-other-pants-tgt-parametrized-image-via-static_in_dockerfile:latest
  Docker image ID: sha256:a0c60e6f2e41b60d445837ee76b5cc993f90d7097b302b517d3632d834f06aad
```