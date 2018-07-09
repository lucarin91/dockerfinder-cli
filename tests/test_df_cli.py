#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `df_cli` package."""


import unittest
from click.testing import CliRunner

from df_cli import cli


class TestDf_cli(unittest.TestCase):
    """Tests for `df_cli` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        self.assertIn('Show this message and exit.', help_result.output)
