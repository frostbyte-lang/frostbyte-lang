"""
    Reference implementation for the Frostbyte smart contract protocol.
"""

import argparse

# # https://rich.readthedocs.io/en/latest/
# from rich import box
# from rich.console import Console
# from rich.panel import Panel

def frostbyte() -> None:
    """
        Script for the `frostbyte` command.
    """
    # Parse commandline arguments:
    description = "Frostbyte smart contract protocol."
    commands = ["daemon"]
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("command", choices=commands, nargs="?", default="daemon")
    args = parser.parse_args()
    print(args)
