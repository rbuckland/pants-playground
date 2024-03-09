# pants-playground

This repository showcases, and is used for debugging various pants repo plugin setups etc.

## Setup Kwargs Override

**Usage**
```
pants package lib/my-simple-lib::
```

This is using a plugin, reo read the VERSION file and the README.txt, into the wheel.

```
❯ unzip -p dist/my_simple_lib-4.3.1-py3-none-any.whl my_simple_lib-4.3.1.dist-info/METADATA
Metadata-Version: 2.1
Name: my-simple-lib
Version: 4.3.1
Requires-Python: <3.12,>=3.10

# my-simple-lib

bunch of fibonacci fns
```
