import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from passgen.password_generator import Generator


class TestGenerator:
    def test_length_12_all_options(self):
        """Test password generation with length 12, all options enabled"""
        params = "length=12, uppercase=True, lowercase=True, numbers=True, special=True"
        gen = Generator(
            length=12, uppercase=True, lowercase=True, numbers=True, special=True
        )
        password = gen.generate()
        print(f"\n✓ Parameters: {params}")
        print(f"  Password: {password} (length={len(password)})")
        assert len(password) == 12
        assert isinstance(password, str)

    def test_length_8_no_special(self):
        """Test password generation with length 8, no special characters"""
        params = "length=8, uppercase=True, lowercase=True, numbers=True, special=False"
        gen = Generator(
            length=8, uppercase=True, lowercase=True, numbers=True, special=False
        )
        password = gen.generate()
        print(f"\n✓ Parameters: {params}")
        print(f"  Password: {password} (length={len(password)})")
        assert len(password) == 8
        assert not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

    def test_length_20_only_uppercase_and_numbers(self):
        """Test password generation with length 20, only uppercase and numbers"""
        params = (
            "length=20, uppercase=True, lowercase=False, numbers=True, special=False"
        )
        gen = Generator(
            length=20, uppercase=True, lowercase=False, numbers=True, special=False
        )
        password = gen.generate()
        print(f"\n✓ Parameters: {params}")
        print(f"  Password: {password} (length={len(password)})")
        assert len(password) == 20

    def test_length_6_only_lowercase(self):
        """Test password generation with length 6, only lowercase letters"""
        params = (
            "length=6, uppercase=False, lowercase=True, numbers=False, special=False"
        )
        gen = Generator(
            length=6, uppercase=False, lowercase=True, numbers=False, special=False
        )
        password = gen.generate()
        print(f"\n✓ Parameters: {params}")
        print(f"  Password: {password} (length={len(password)})")
        assert len(password) == 6
        assert password.islower()

    def test_length_15_uppercase_and_special(self):
        """Test password generation with length 15, uppercase and special characters"""
        params = (
            "length=15, uppercase=True, lowercase=False, numbers=False, special=True"
        )
        gen = Generator(
            length=15, uppercase=True, lowercase=False, numbers=False, special=True
        )
        password = gen.generate()
        print(f"\n✓ Parameters: {params}")
        print(f"  Password: {password} (length={len(password)})")
        assert len(password) == 15

    def test_length_30_all_enabled(self):
        """Test password generation with length 30, all options enabled"""
        params = "length=30, uppercase=True, lowercase=True, numbers=True, special=True"
        gen = Generator(
            length=30, uppercase=True, lowercase=True, numbers=True, special=True
        )
        password = gen.generate()
        print(f"\n✓ Parameters: {params}")
        print(f"  Password: {password} (length={len(password)})")
        assert len(password) == 30

    def test_multiple_generations_are_different(self):
        """Test that multiple generations produce different passwords"""
        params = "length=16, uppercase=True, lowercase=True, numbers=True, special=True"
        gen = Generator(
            length=16, uppercase=True, lowercase=True, numbers=True, special=True
        )
        password1 = gen.generate()
        password2 = gen.generate()
        print(f"\n✓ Parameters: {params}")
        print(f"  Password 1: {password1} (length={len(password1)})")
        print(f"  Password 2: {password2} (length={len(password2)})")
        print(f"  Different: {password1 != password2}")
        # Passwords should be different (extremely unlikely to be the same)
        assert password1 != password2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
