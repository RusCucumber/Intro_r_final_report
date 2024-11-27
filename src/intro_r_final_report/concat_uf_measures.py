from pathlib import Path
from typing import Generator

import pandas as pd

WORK_DIR = Path(__file__).parents[2]
DATA_DIR = WORK_DIR / "data/processed"

def transcript_path_generator() -> Generator[Path, None, None]:
    for csv_path in DATA_DIR.glob("*.csv"):
        yield csv_path

def main() -> None:
    uf_measure_df = []
    for csv_path in transcript_path_generator():
        df_uf = pd.read_csv(csv_path)
        uf_measure_df.append(df_uf)

    df_uf = pd.concat(uf_measure_df)
    df_uf = df_uf.sort_values("filename")
    df_uf.to_csv(DATA_DIR / "uf_measures.csv", index=False)

if __name__ == "__main__":
    main()
