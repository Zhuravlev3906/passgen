import argparse


def _create_parser() -> argparse.ArgumentParser:
    """Create an argument parser for the password generator CLI."""

    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument(
        "--length", type=int, default=12, help="Length of the password", metavar="N"
    )
    parser.add_argument(
        "--no-uppercase",
        action="store_false",
        dest="include_uppercase",
        help="Include uppercase letters",
    )
    parser.add_argument(
        "--no-lowercase",
        action="store_false",
        dest="include_lowercase",
        help="Include lowercase letters",
    )
    parser.add_argument(
        "--no-digits",
        action="store_false",
        dest="include_numbers",
        help="Include digits",
    )
    parser.add_argument(
        "--no-special",
        action="store_false",
        dest="include_special",
        help="Include special characters",
    )
    parser.add_argument(
        "--exclude",
        type=str,
        default="",
        help="Characters to exclude from the password",
        metavar="CHARS",
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Output file to save the generated password",
        metavar="FILE",
    )

    return parser


def get_args() -> argparse.Namespace:
    parser = _create_parser()
    return parser.parse_args()
