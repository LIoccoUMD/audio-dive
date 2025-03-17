# Audio Waveform and Chromagram Analysis

This project contains a Python script for analyzing audio files by generating a waveform plot and a chromagram visualization. It uses libraries like `librosa`, `scipy`, and `matplotlib` to process and visualize audio data.

## Features
- Loads an audio file (`welcomeback.wav`) and extracts its waveform data.
- Computes and displays a chromagram, showing the distribution of energy across 12 pitch classes over time.
- Includes commented-out code for plotting the raw audio waveform.

## Prerequisites
Ensure you have Python installed along with the following dependencies:
- `librosa` - For audio processing and chromagram computation.
- `yt_dlp` - (Not used in the current script but included in imports).
- `matplotlib` - For plotting the waveform and chromagram.
- `numpy` - For numerical operations.
- `scipy` - For reading `.wav` files.

Install the required packages using pip:
```bash
pip install librosa yt_dlp matplotlib numpy scipy
