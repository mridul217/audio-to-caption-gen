import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print("this is the subtitles:\n",result["text"])

