# SPDX-FileCopyrightText: 2025-present jd-35656 <jitesh.sahani@outlook.com>
#
# SPDX-License-Identifier: MIT

from click.testing import CliRunner

from lbx.cli import lbx


def test_lbx_command():
    """Test basic lbx command execution."""
    runner = CliRunner()
    result = runner.invoke(lbx)

    assert result.exit_code == 0
    assert "Hello Dreamers!" in result.output


def test_lbx_version():
    """Test lbx version option."""
    runner = CliRunner()
    result = runner.invoke(lbx, ["--version"])

    assert result.exit_code == 0
    assert "lbx" in result.output


def test_lbx_help():
    """Test lbx help option."""
    runner = CliRunner()
    result = runner.invoke(lbx, ["--help"])

    assert result.exit_code == 0
    assert "Usage:" in result.output
