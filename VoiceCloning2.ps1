python -m venv ./venv
./venv/scripts/activate.ps1

# source ./venv/bin/activate

python.exe -m pip install --upgrade pip

#####
pip install jupyterlab
pip install torch torchaudio librosa
pip install SpeechRecognition
pip install pydub
pip install ffmpeg
