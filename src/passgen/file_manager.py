class FileManager:
    def __init__(self, output_file: str):
        self.output_file = output_file

    def write_passwords(self, password: str) -> None:
        """Write the generated passwords to the specified output file."""
        with open(self.output_file, "w") as f:
            f.write(password + "\n")
