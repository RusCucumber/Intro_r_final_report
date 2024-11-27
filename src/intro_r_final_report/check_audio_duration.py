from pathlib import Path
from typing import Generator

from pydub import AudioSegment

WORK_DIR = Path(__file__).parents[2]
DATA_DIR = WORK_DIR / "data/raw"

def audio_duration_generator() -> Generator[float, None, None]:
    for audio_path in DATA_DIR.glob("*.wav"):
        audio = AudioSegment.from_wav(audio_path)
        yield audio.duration_seconds

def main() -> None:
    total_duration_seconds = 0
    for audio_dur in audio_duration_generator():
        total_duration_seconds += audio_dur

    print(f"{total_duration_seconds / 60} mins")

if __name__ == "__main__":
    main()
