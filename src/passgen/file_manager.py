from pathlib import Path

from passgen.exception import FileOutputException


class FileManager:
    def __init__(self, output_file: str):
        self.output_file = Path(output_file)

    def save_password(self, password: str) -> None:
        """Write the generated password to the specified output file."""
        try:
            self.output_file.write_text(password + "\n", encoding="utf-8")
        except OSError as e:
            raise FileOutputException(
                f"Failed to write to file {self.output_file}: {e}"
            ) from e
