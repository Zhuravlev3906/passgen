import pytest

from passgen.config import Config, validate_config
from passgen.exception import InvalidConfigException


def test_default_config_is_valid():
    cfg = Config()
    # should not raise
    validate_config(cfg)


def test_invalid_length_raises():
    cfg = Config(length=0)
    with pytest.raises(InvalidConfigException):
        validate_config(cfg)


def test_no_character_types_raises():
    cfg = Config(
        include_uppercase=False,
        include_lowercase=False,
        include_numbers=False,
        include_special=False,
    )
    with pytest.raises(InvalidConfigException):
        validate_config(cfg)


def test_config_is_frozen():
    cfg = Config()
    with pytest.raises(Exception):
        # frozen dataclass should prevent attribute assignment
        cfg.length = 8


if __name__ == "__main__":
    # allow running this file directly to execute tests
    raise SystemExit(pytest.main([__file__]))
