from pydub import AudioSegment
import os

def convert_mp3_to_wav(directory):
    """
    Convert all MP3 files in the given directory to WAV format.

    Args:
      directory: The path to the directory containing MP3 files.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(directory, filename)
            wav_path = os.path.join(directory, filename.replace(".mp3", ".wav"))

            # Convert MP3 to WAV
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")
            print(f"Converted {filename} to WAV format")

# Example usage
convert_mp3_to_wav('recordings')  # Replace with your directory path
