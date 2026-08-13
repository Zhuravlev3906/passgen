from passgen.cli import get_args
from passgen.config import Config, validate_config
from passgen.file_manager import FileManager
from passgen.password_generator import PasswordGenerator


def main():
    args = get_args()

    config = Config(
        length=args.length,
        include_uppercase=args.include_uppercase,
        include_lowercase=args.include_lowercase,
        include_numbers=args.include_numbers,
        include_special=args.include_special,
        exclude_chars=args.exclude,
        output_file=args.output,
    )

    validate_config(config)

    password_generator = PasswordGenerator(config)
    password = password_generator.generate()

    if config.output_file:
        file_manager = FileManager(config.output_file)
        file_manager.save_password(password)
        print(f"Password saved to {config.output_file}")
    else:
        print(f"Generated password: {password}")
