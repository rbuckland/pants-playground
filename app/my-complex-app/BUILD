
resource(
    name = "version",
    source = "VERSION",
)


docker_image(
  name="my-complex-app",
  dependencies=[
    "lib/my-simple-lib:simple_lib_wheel",
  ],
  image_tags=[
       "abc",
       "123",
       read_file_contents("xxxx"),
  ]
)
