import secrets
import string

from passgen.config import Config
from passgen.exception import PasswordGenerationException


class PasswordGenerator:
    def __init__(
        self,
        config: Config,
    ) -> None:
        self.length = config.length
        self.uppercase = config.include_uppercase
        self.lowercase = config.include_lowercase
        self.numbers = config.include_numbers
        self.special = config.include_special
        self.exclude = config.exclude_chars

    def generate(self) -> str:
        character_pool = ""

        if self.uppercase:
            character_pool += string.ascii_uppercase
        elif self.lowercase:
            character_pool += string.ascii_lowercase
        else:
            character_pool += string.ascii_letters

        if self.numbers:
            character_pool += string.digits
        if self.special:
            character_pool += string.punctuation

        for char in self.exclude:
            character_pool = character_pool.replace(char, "")

        if not character_pool:
            raise PasswordGenerationException(
                "Character pool is empty. Cannot generate password."
            )

        return "".join(secrets.choice(character_pool) for _ in range(self.length))
