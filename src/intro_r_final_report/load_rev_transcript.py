import json
from pathlib import Path
from traceback import format_exc

from rev_asr import RevAsr, transcript_2_df
from tqdm import tqdm

WORK_DIR = Path(__file__).parents[2]
DATA_DIR = WORK_DIR / "data/raw"

with open(WORK_DIR / "src/intro_r_final_report/rev_access_token.json", "r") as f:
    access_token = json.load(f)

ACCESS_TOKEN = access_token["token"]

def main():
    asr = RevAsr(ACCESS_TOKEN)

    incompleted_job = []

    n_job = len(list(DATA_DIR.glob("*.json")))
    for job_path in tqdm(DATA_DIR.glob("*.json"), desc="Request transcript", total=n_job):
        save_path = DATA_DIR / f"{job_path.stem}.csv"
        if save_path.exists():
            continue

        with open(job_path, "r") as f:
            response = json.load(f)
            job_id = response["id"]

        try:
            if asr.is_job_completed(job_id):
                rev_transcript = asr.load_transcription(job_id, df=False)
                df_transcript = transcript_2_df(rev_transcript)
                df_transcript.to_csv(save_path, index=False)
        except RuntimeError:
            print(f"job {job_id} failed: {response['failure']}")
            print(format_exc())
            incompleted_job.append(job_path.stem)

    print(incompleted_job)

if __name__ == "__main__":
    main()
