import secrets
import string
import random

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
        character_pool = []

        if self.uppercase:
            character_pool.append(string.ascii_uppercase)
        if self.lowercase:
            character_pool.append(string.ascii_lowercase)

        if self.numbers:
            character_pool.append(string.digits)
        if self.special:
            character_pool.append(string.punctuation)

        for char in self.exclude:
            for i, pool in enumerate(character_pool):
                character_pool[i] = pool.replace(char, "")

        # Remove any empty strings from the list
        character_pool = [pool for pool in character_pool if pool]

        if not character_pool:
            raise PasswordGenerationException(
                "Character pool is empty. Cannot generate password."
            )

        # Ensure at least one character from each selected category
        if self.length < len(character_pool):
            raise PasswordGenerationException(
                "Password length is less than number of selected character categories."
            )

        # Pick one mandatory character from each category
        password_chars = [secrets.choice(pool) for pool in character_pool]

        # Build combined pool for remaining characters
        combined_pool = "".join(character_pool)
        if not combined_pool:
            raise PasswordGenerationException(
                "Combined character pool is empty. Cannot generate password."
            )

        remaining = self.length - len(password_chars)
        for _ in range(remaining):
            password_chars.append(secrets.choice(combined_pool))

        # Shuffle using a cryptographically secure RNG
        random.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)
