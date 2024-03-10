from pants.engine.fs import DigestContents, GlobMatchErrorBehavior, PathGlobs
from pants.engine.rules import Get, collect_rules, rule
from pants.engine.target import (
    COMMON_TARGET_FIELDS,
    Target
)
from pants.engine.unions import UnionRule
from pants.core.target_types import FileSourceField, StringField, MultipleSourcesField
from pants.util.strutil import help_text
from dataclasses import dataclass
from typing import Optional
import os

# class RegexFilterField(StringField):
#     alias = "regex"
#     required = False
#     help = help_text(
#         """
#         Regex pattern, used to extract the string from the file contents.
#         """
#     )

class ContentOfMultipleSourcesField(MultipleSourcesField):
    required = False
    help = help_text(
        """
        A list of files to read the contents from.
        All contents are concatenated together.
        """
    )


@dataclass(frozen=True)
class ReadFileContents(str):
    """read_file_contents() string provider"""

    alias = "read_file_contents"
    help = help_text(
        """
        A string read from a file.
        """
    )
    regex: Optional[str] = None
    static: Optional[str] = None
    sources: Optional[ContentOfMultipleSourcesField] = None

    def __new__(cls, value: str = "dummy-value-from-new", **kwargs):
        print(f"new() {value=} {kwargs=}", end="")
        return super().__new__(cls, value)

    def __init__(self, value: str = "dummy-value-from-init", **kwargs):
        print(f"init {value=} {kwargs=}", end="")
        super().__init__()
        # self.regex = kwarg.get("regex")
        # self.static = kwarg.get("static")
        # self.sources = kwarg.get("sources")

    def __hash__(self):
        return super().__hash__()


@dataclass(frozen=True)
class ReadFileContentsRequest:
    target: Target

    @classmethod
    def is_applicable(cls, _: Target) -> bool:
       return True


@rule
async def do_read_the_file(request: ReadFileContentsRequest) -> str:

    return ReadFileContents("winner")

def rules():
    return (
        do_read_the_file,
    )
