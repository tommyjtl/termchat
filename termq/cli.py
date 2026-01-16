#!/usr/bin/env python3
"""
CLI entry point for termq
"""

import sys
from argparse import ArgumentParser


def main():
    """Main CLI entry point that routes to chat.py or pdf.py"""
    # Parse initial args to check for --pdf flag
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "--pdf", dest="use_pdf", action="store_true", help="Use PDF mode"
    )

    # Parse known args to check for pdf flag
    args, remaining = parser.parse_known_args()

    if args.use_pdf:
        # Import and run pdf mode
        from termq.pdf_mode import main as pdf_main

        # Re-inject remaining args for pdf_mode to parse
        sys.argv = [sys.argv[0]] + remaining
        pdf_main()
    else:
        # Import and run chat mode
        from termq.chat_mode import main as chat_main

        # Re-inject all args except the script name for chat_mode to parse
        sys.argv = [sys.argv[0]] + sys.argv[1:]
        chat_main()


if __name__ == "__main__":
    main()
