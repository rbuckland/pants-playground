# ref: https://www.pantsbuild.org/docs/plugins-setup-py
from pants.backend.python.util_rules.package_dists import (
    SetupKwargs,
    SetupKwargsRequest,
)
from pants.engine.fs import DigestContents, GlobMatchErrorBehavior, PathGlobs
from pants.engine.rules import Get, collect_rules, rule
from pants.engine.target import Target
from pants.engine.unions import UnionRule
import os


class CustomSetupKwargsRequest(SetupKwargsRequest):
    @classmethod
    def is_applicable(cls, _: Target) -> bool:
        return True


@rule
async def setup_kwargs_plugin(request: CustomSetupKwargsRequest) -> SetupKwargs:
    """Create the SetupKwargs parameters

    Args:
        request (CustomSetupKwargsRequest): _description_

    Returns:
        SetupKwargs: Returns an altered SetupKwargs with description and version populated
    """

    async def read_file(file_path: str) -> str:
        """returns the longdesc file contents file contents"""
        digest_contents = await Get(
            DigestContents,
            PathGlobs(
                [file_path],
                description_of_origin="`python_artifact()` plugin",
                glob_match_error_behavior=GlobMatchErrorBehavior.error,
            ),
        )
        c = digest_contents[0].content.decode()
        return c

    original_kwargs = request.explicit_kwargs.copy()
    build_file_path = request.target.address.spec_path

    version_file = original_kwargs.pop("version_file", None)
    version_file_full_path = os.path.join(build_file_path, version_file)
    version = await read_file(version_file_full_path)

    longdesc_file = original_kwargs.pop("long_description_file", None)
    longdesc_file_full_path = os.path.join(build_file_path, longdesc_file)
    longdesc = await read_file(longdesc_file_full_path)

    return SetupKwargs(
        {
            **request.explicit_kwargs,
            "version": version,
            "long_description": longdesc,
        },
        address=request.target.address,
    )


def rules():
    return (
        *collect_rules(),
        UnionRule(SetupKwargsRequest, CustomSetupKwargsRequest),
    )
