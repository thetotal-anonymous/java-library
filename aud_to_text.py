import speech_recognition as sr
from moviepy.editor import *

def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    mp3_file_path = r"C:\Users\44ved\Desktop\My Tools\Cloud+computing_out.mp3"

    audio_clip = AudioFileClip(mp3_file_path)
    temp_wav_path = "temp.wav"
    audio_clip.write_audiofile(temp_wav_path)

    result = audio_to_text(temp_wav_path)
    print("Transcription:", result)

    # Clean up temporary WAV file
    audio_clip.close()
    if os.path.exists(temp_wav_path):
        os.remove(temp_wav_path)



