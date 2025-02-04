import requests
import os
from rich import print
from glob import glob
from pydub import AudioSegment
import urllib.request


VOICE_SAMPLE_URLS = [
    "https://archive.org/download/anne_greengables_librivox/anne_of_green_gables_01_montgomery.mp3",
    "https://dn720006.ca.archive.org/0/items/sense_sensibility_1104_librivox/sense-sensibility_01_austen_64kb.mp3",
    # "https://movie-sounds.org/quotes/308/once-again-i-must-protest!.mp3",
    # "https://movie-sounds.org/quotes/308/you-call-yourself-a-free-spirit-a-wild-thing-and-you're-terrified-somebody's-going-to-stick-you-in-a-cage-well-baby-you're-already-in-that-cage-you-built-it-yourself.mp3",
    # "https://movie-sounds.org/quotes/308/if-we're-going-to-be-friends-let's-just-get-one-thing-straight-right-now-i-hate-snoops.mp3",
    # "https://movie-sounds.org/quotes/308/people-do-fall-in-love-people-do-belong-to-each-other-because-that's-the-only-chance-anybody's-got-for-real-happiness.mp3",
    # "https://movie-sounds.org/quotes/308/all-right-so-he's-not-a-regular-rat-or-even-a-super-rat-he's-just-a-scared-little-mouse-that's-all.mp3",
    # "https://movie-sounds.org/quotes/308/and-i-always-heard-people-in-new-york-never-get-to-know-their-neighbours.mp3",
    # "https://movie-sounds.org/quotes/308/anyway-that's-why-he-decided-to-marry-the-queen-of-the-pig-people.mp3",
    # "https://movie-sounds.org/quotes/308/because-no-matter-where-you-run-you-just-end-up-running-into-yourself.mp3",
    # "https://movie-sounds.org/quotes/308/but-on-the-other-hand-you're-right-because-she's-a-real-phoney-you-know-why-because-she-honestly-believes-all-this-phoney-junk-that-she-believes-in-i-mean-it.mp3",
]


class DownloadVoiceFiles:

    def __init__(
        self,
        voice_file_urls: list[str],
        data_dir: str = "voice_data",
    ) -> None:
        os.makedirs(data_dir, exist_ok=True)
        self.voice_file_urls = voice_file_urls

        for voice_url in self.voice_file_urls:
            filename = voice_url.split("/")[-1]
            filename = filename.replace("'", "_")
            filepath = f"{data_dir}/{filename}"

            if os.path.exists(filepath):
                print(f"File '{filepath}' already exists, skipping download")
                continue

            self.download_mp3(voice_url, filepath)

    def download_mp3(self, url, save_path):
        response = requests.get(
            url,
            stream=True,
        )  # Stream mode prevents memory overload

        content_type = response.headers.get("Content-Type", "")
        print(content_type)

        # Check if the response is actually an MP3
        if "audio/mpeg" not in content_type:
            print(f"[red]Warning: {url} did not return an MP3. Skipping...[/red]")
            return False

        # Save file as binary
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):  # Download in chunks
                f.write(chunk)

        print(f"Downloaded: {save_path}")
        return True


class MP3Utils:

    @staticmethod
    def clip(
        filepath: str,
        length_milliseconds: int = 10_000,
        output_filepath: str = "voice_sample.mp3",
    ) -> None:
        this_clip = AudioSegment.from_mp3(filepath)
        sound = this_clip[:length_milliseconds]

        sound.export(output_filepath, format="mp3")

    @staticmethod
    def stich(self, input_dir: str, length_milliseconds: 10_000) -> None:
        mp3_filepaths = glob(f"{input_dir}/*.mp3", recursive=True)

        sound = None
        for mp3_path in mp3_filepaths:
            this_clip = AudioSegment.from_mp3(mp3_path)

            # if not sound:
            #     sound = this_clip
            #     continue

            # len() and slicing are in milliseconds
            # halfway_point = len(sound) / 2
            sound = this_clip[:length_milliseconds]

            # Concatenation is just adding
            # sound = sound + this_clip

        sound.export("voice_sample.mp3", format="mp3")
