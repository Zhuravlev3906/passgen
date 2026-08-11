import argparse


def create_parser() -> argparse.ArgumentParser:
    """Create an argument parser for the password generator CLI."""

    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument(
        "--length", type=int, default=12, help="Length of the password", metavar="N"
    )
    parser.add_argument(
        "--uppercase", action="store_true", help="Include uppercase letters"
    )
    parser.add_argument(
        "--lowercase", action="store_true", help="Include lowercase letters"
    )
    parser.add_argument("--digits", action="store_true", help="Include digits")
    parser.add_argument(
        "--special", action="store_true", help="Include special characters"
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
    parser = create_parser()
    return parser.parse_args()
