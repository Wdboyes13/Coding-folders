import aubio
import pyaudio
import numpy as np

# Audio settings
BUFFER_SIZE = 1024
CHANNELS = 1
RATE = 44100

# Setup audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=BUFFER_SIZE)

# Setup tempo detector
tempo_detector = aubio.tempo("default", BUFFER_SIZE, BUFFER_SIZE//2, RATE)
bpm_values = []

print("Listening... Tap your table with the beat if testing!")

while True:
    try:
        # Read audio data
        data = np.frombuffer(stream.read(BUFFER_SIZE), dtype=np.float32)

        # Feed data to tempo detector
        if tempo_detector(data):
            bpm = tempo_detector.get_bpm()
            bpm_values.append(bpm)

            # Moving average for smoother BPM output
            if len(bpm_values) > 5:
                avg_bpm = sum(bpm_values[-5:]) / 5  # Last 5 detections
                print(f"Estimated BPM: {round(avg_bpm, 2)}")
            else:
                print(f"Estimated BPM: {round(bpm, 2)}")
    
    except KeyboardInterrupt:
        print("\nStopping...")
        break

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()