#!/usr/bin/env python

"""Tests for `contactform` package."""

import pytest
from click.testing import CliRunner

from contactform import __version__, cli, contactform


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_version():
    """Test reading version and module name"""
    assert contactform.__name__ == "contactform.contactform"
    assert __version__
    assert isinstance(__version__, str)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code != 0, result
    assert "contactform" in result.output

    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0, result
    assert "Show this message and exit." in result.output
