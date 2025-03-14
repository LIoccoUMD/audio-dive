import librosa
import yt_dlp
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

sample_rate, data = wavfile.read("welcomeback.wav")
time = np.arange(len(data)) / sample_rate # Create time axis in seconds
# plt.plot(time, data)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.title('Waveform of Audio')
# plt.grid(True)
# plt.show()




# Each column is a "snapshot" of the harmonic content at a specific moment. 
# With the default hop length of 512 samples and a sampling rate of 22050 Hz, 
# each frame is about 23 milliseconds apart (512 / 22050 ≈ 0.023 seconds). 
# For 15 seconds of audio, you’d get roughly 647 columns (15 / 0.023).
y, sr = librosa.load("welcomeback.wav", duration=15)
# A chromagram represents the distribution of energy across the 12 distinct pitch classes
# (or "chroma") of the musical octave (C, C#, D, D#, E, F, F#, G, G#, A, A#, B).
# It’s commonly used in music information retrieval to analyze the harmonic content of audio.
print(librosa.feature.chroma_stft(y=y, sr=sr).shape)
chromagram = librosa.feature.chroma_stft(y=y,sr=sr)

librosa.display.specshow(data=chromagram,sr=sr, y_axis="chroma", x_axis="time")
plt.colorbar()
plt.show()