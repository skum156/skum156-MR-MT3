import librosa
import soundfile as sf

input_path = "/scratch/gilbreth/kumar809/MR-MT3/evaluation_mp3_1._0_40_70.wav"
output_path = "/scratch/gilbreth/kumar809/MR-MT3/evaluation_mp3_1._0_40_70_16k.wav"

audio, sr = librosa.load(input_path, sr=None)
print(f"Loaded audio sample rate: {sr}")

if sr != 16000:
    print("Resampling audio to 16kHz...")
    audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
    sf.write(output_path, audio, 16000)
    print(f"Saved resampled audio to: {output_path}")
else:
    print("Audio already 16kHz, no resampling needed.")