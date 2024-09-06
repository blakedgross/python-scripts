from os import listdir
from os.path import isfile, join, basename
from datetime import timedelta
import whisper
import torch

torch.cuda.init()
device = "cuda"

path = "F:\\workspace\\transcriptions\\to_process\\"
outpath = "F:\\workspace\\transcriptions\\to_process\\out\\"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

model = whisper.load_model("medium").to(device)
for x in onlyfiles:
    combinedpath = path + x
    print("combined path: " + combinedpath)
    with torch.cuda.device(device):
        result = model.transcribe(combinedpath, language="japanese", fp16=False)
    segments = result['segments']

    fileName = x.rsplit(".", 1)[0] + '.txt'
    combinedOutpath = outpath + fileName
    
    for segment in segments:
        startTime = str(timedelta(seconds=int(segment['start'])))
        endTime = str(timedelta(seconds=int(segment['end'])))
        text = segment['text']
        outSegment = startTime + " - " + endTime + "\r\n" + text + "\r\n"

        try: 
            with open(combinedOutpath, 'a', encoding='utf8') as writeFile:
                writeFile.write(outSegment)
        except:
            print("error generating segment") 
    
#print("processed: " + fileName)