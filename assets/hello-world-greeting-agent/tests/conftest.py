"""Test conftest — ensures app/ is on sys.path for all tests in this directory."""
import sys
from pathlib import Path

# Add app/ to sys.path so agent modules resolve as top-level imports
app_path = str(Path(__file__).parent.parent / "app")
if app_path not in sys.path:
    sys.path.insert(0, app_path)
