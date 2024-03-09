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

The plugin, `tools/pants-plugins/pinchworms/src/pinchworms/packaging/{register.py, setup_kwargs.py} read the `VERSION` file and the `README.md`, into the wheel.

```
❯ unzip -p dist/my_simple_lib-4.3.1-py3-none-any.whl my_simple_lib-4.3.1.dist-info/METADATA
Metadata-Version: 2.1
Name: my-simple-lib
Version: 4.3.1
Requires-Python: <3.12,>=3.10

# my-simple-lib

bunch of fibonacci fns
```
