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
    files: Optional[ContentOfMultipleSourcesField] = None

    def __new__(cls, value: str = "ccc", regex: Optional[str] = None, files: Optional[ContentOfMultipleSourcesField] = None):
        return str.__new__(cls, value)

