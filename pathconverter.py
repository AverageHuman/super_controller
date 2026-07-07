from pathlib import Path
import os

BASE_DIRECTORY = Path(__file__).resolve().parent

AUDIO_DIRECTORY = Path(
    os.getenv("AUDIO_DIRECTORY", BASE_DIRECTORY / "audio")
).expanduser().resolve()

def audio_path(filename:str) -> str:
    return str(AUDIO_DIRECTORY / filename)

