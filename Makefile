
sample.wav: sample.mp3
	ffmpeg -f mp3 -i sample.mp3 -f wav sample.wav
