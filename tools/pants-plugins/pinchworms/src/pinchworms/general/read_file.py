from pants.engine.fs import DigestContents, GlobMatchErrorBehavior, PathGlobs
from pants.engine.rules import Get, collect_rules, rule
from pants.engine.target import (
    COMMON_TARGET_FIELDS,
    Target
)
from pants.engine.unions import UnionRule, union
from pants.core.target_types import FileSourceField, StringField, MultipleSourcesField
from pants.util.strutil import help_text
from dataclasses import dataclass
from typing import Optional
import os

@dataclass(frozen=True)
class ReadFileContents:
    alias = "read_file_contents"
    help = help_text(
        """
        Read a string from a file.
        """
    )
    sources: Optional[MultipleSourcesField] = None
    regex: Optional[str] = None

@rule
async def do_read_the_file(file_content_alias: ReadFileContents) -> str:

    return "read-the-file-contents"

def rules():
    return (do_read_the_file,)
