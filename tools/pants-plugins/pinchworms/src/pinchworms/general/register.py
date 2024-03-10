from pants.build_graph.build_file_aliases import BuildFileAliases

import pinchworms.general.read_file
from pinchworms.general.read_file import ReadFileContents


def build_file_aliases():
    return BuildFileAliases(objects={ReadFileContents.alias: ReadFileContents})

# def rules():
#     return [*pinchworms.general.read_file.rules()]
