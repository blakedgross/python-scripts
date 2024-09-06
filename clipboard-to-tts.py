from elevenlabs import play
from elevenlabs.client import ElevenLabs
import time
import win32clipboard

prevClipboardData = None

client = ElevenLabs(
  api_key="3320d59da3cc4f8ba4fa35a67bdd330b" # Defaults to ELEVEN_API_KEY
)

# get voices
#response = client.voices.get_all()
#print(response)

#get data
while True: 
    win32clipboard.OpenClipboard()
    examineData = win32clipboard.GetClipboardData()
    if prevClipboardData != examineData:
        prevClipboardData = examineData
        print(prevClipboardData)
        audio = client.generate(text=prevClipboardData, voice="3JDquces8E8bkmvbh6Bc")
        play(audio)
    win32clipboard.CloseClipboard()
    time.sleep(.5)
