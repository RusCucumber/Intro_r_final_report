import json
from pathlib import Path

from rev_asr import RevAsr, save_job
from tqdm import tqdm

WORK_DIR = Path(__file__).parents[2]
DATA_DIR = WORK_DIR / "data/raw"

with open(WORK_DIR / "src/intro_r_final_report/rev_access_token.json", "r") as f:
    access_token = json.load(f)

ACCESS_TOKEN = access_token["token"]

def main():
    asr = RevAsr(ACCESS_TOKEN)

    tqdm_desc = "POST audio data"
    n_speech = len(list(DATA_DIR.glob("*.wav")))
    for audio_path in tqdm(DATA_DIR.glob("*.wav"), desc=tqdm_desc, total=n_speech):
        save_path = DATA_DIR / f"{audio_path.stem}.json"
        if save_path.exists():
            continue

        job = asr.submit(audio_path)
        save_job(job, save_path)

if __name__ == "__main__":
    main()
