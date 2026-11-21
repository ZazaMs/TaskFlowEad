import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import create_app

@pytest.fixture
def client(tmp_path):
    database = tmp_path / "test.db"
    app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test-key",
        "DATABASE": str(database),
    })
    with app.test_client() as client:
        yield client
