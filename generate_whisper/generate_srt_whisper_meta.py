from os import listdir
from os.path import isfile, join, basename
from datetime import timedelta
import whisper
import torch

torch.cuda.init()
device = "cuda"

path = "C:\\Users\\Kater\\Downloads\\meta-charles-capture-8-12-24.mp4"
outpath = "C:\\Users\\Kater\\Downloads\\meta-charles-capture-8-12-24.srt"
#onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#print(onlyfiles)

model = whisper.load_model("medium").to(device)
#for x in onlyfiles:
with torch.cuda.device(device):
    result = model.transcribe(path, language="english", fp16=False)

segments = result['segments']

#fileName = path.rsplit(".", 1)[0] + '.srt'
for segment in segments:
    startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
    endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
    text = segment['text']
    segmentId = segment['id']+1
    try: 
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
        with open(outpath, 'a', encoding='utf8') as writeFile:
            writeFile.write(segment)
    except:
        print("error generating segment") 
    
#print("processed: " + fileName)