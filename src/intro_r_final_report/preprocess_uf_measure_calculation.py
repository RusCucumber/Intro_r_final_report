from pathlib import Path
from typing import Generator

import pandas as pd

WORK_DIR = Path(__file__).parents[2]
DATA_DIR = WORK_DIR / "data/raw"

def transcript_path_generator() -> Generator[Path, None, None]:
    for csv_path in DATA_DIR.glob("*.csv"):
        yield csv_path

def df_2_str(df_transcript: pd.DataFrame) -> str:
    text = "".join(df_transcript["text"])
    return text

def main() -> None:
    for csv_path in transcript_path_generator():
        df_transcript = pd.read_csv(csv_path)
        text = df_2_str(df_transcript)

        save_path = DATA_DIR / f"{csv_path.stem}.txt"
        with open(save_path, "w") as f:
            f.write(text)

if __name__ == "__main__":
    main()
