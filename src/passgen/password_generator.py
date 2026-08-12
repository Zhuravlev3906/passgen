import secrets
import string


class Generator:
    def __init__(
        self,
        length: int,
        uppercase: bool,
        lowercase: bool,
        numbers: bool,
        special: bool,
    ) -> None:
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special = special

    def generate(self) -> str:
        character_pool = ""
        if self.uppercase and self.lowercase:
            character_pool += string.ascii_letters
        elif self.uppercase:
            character_pool += string.ascii_uppercase
        else:
            character_pool += string.ascii_lowercase

        if self.numbers:
            character_pool += string.digits
        if self.special:
            character_pool += string.punctuation

        return "".join(secrets.choice(character_pool) for _ in range(self.length))
