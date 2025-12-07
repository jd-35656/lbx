# SPDX-FileCopyrightText: 2025-present jd-35656 <jitesh.sahani@outlook.com>
#
# SPDX-License-Identifier: MIT

import click

from lbx.__version__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="lbx")
def lbx() -> None:
    click.echo("Hello Dreamers!")
