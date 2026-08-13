from passgen.cli import get_args
from passgen.config import Config
from passgen.file_manager import FileManager
from passgen.password_generator import PasswordGenerator

if __name__ == "__main__":
    args = get_args()

    config = Config(
        length=args.length,
        include_uppercase=args.uppercase,
        include_lowercase=args.lowercase,
        include_numbers=args.digits,
        include_special=args.special,
        exclude_chars=args.exclude,
        output_file=args.output,
    )

    password_generator = PasswordGenerator(config)
    password = password_generator.generate()

    if config.output_file:
        file_manager = FileManager(config.output_file)
        file_manager.write_passwords(password)
        print(f"Password saved to {config.output_file}")
    else:
        print(f"Generated password: {password}")
