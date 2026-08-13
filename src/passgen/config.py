from dataclasses import dataclass

from passgen.exception import InvalidConfigException


@dataclass(frozen=True)
class Config:
    """Configuration for the password generator."""

    length: int = 12
    include_uppercase: bool = True
    include_lowercase: bool = True
    include_numbers: bool = True
    include_special: bool = True
    exclude_chars: str = ""
    output_file: str = ""


def validate_config(config: Config) -> None:
    """Validate the configuration for the password generator."""
    if config.length <= 0:
        raise InvalidConfigException("Password length must be greater than 0.")
    if not (
        config.include_uppercase
        or config.include_lowercase
        or config.include_numbers
        or config.include_special
    ):
        raise InvalidConfigException("At least one character type must be included.")
