# -*- coding: utf-8 -*-
"""Tests for lta.parser."""
from _pytest import capture

from lta.commands.run import run
from lta.parser import lta_parser

expected = """usage: lta [-h] [-c CONFIG] [-t {[0, 1]}] [-b BOOT_REPS] [-n N_ROWS_METADATA]
           [--group GROUP] [--control CONTROL] [--compartment COMPARTMENT]
           [--mode MODE] [--sample-id SAMPLE_ID] [-V] [-v] [-l LOGFILE]
           [--savealignfiles]
           file output
"""


def test_correct_usage(capsys: capture.CaptureFixture) -> None:
    """It has the correct usage (ie. structure)."""
    lta_parser.print_usage()
    usage = capsys.readouterr()
    assert usage.out == expected, "LTA's usage is incorrect."


def test_default_func() -> None:
    """It has the correct default function."""
    assert (
        lta_parser.get_default("func") == run
    ), "The default function is not lta.commands.run."
