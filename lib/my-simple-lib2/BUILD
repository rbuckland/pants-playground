poetry_requirements(
    name = "reqs",
    resolve = "python-default",
    source = "pyproject.toml",
)

python_distribution(
    name = "simple_lib_wheel2",
    dependencies = [
        "./src:sources",
        ":reqs"
    ],
    generate_setup = True,
    provides = python_artifact(
        name = "my_simple_lib2",
        version_file = "VERSION",
        long_description_file = "README.md",
    ),
)
