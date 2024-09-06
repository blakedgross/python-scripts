from os import listdir
from os.path import isfile, join, basename
from datetime import timedelta
import whisper
import torch
from typing import Iterator, TextIO

def srt_format_timestamp(seconds: float):
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    return (f"{hours}:") + f"{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def write_srt(transcript: Iterator[dict], file: TextIO):
    count = 0
    for segment in transcript:
        count +=1
        print(
            f"{count}\n"
            f"{srt_format_timestamp(segment['start'])} --> {srt_format_timestamp(segment['end'])}\n"
            f"{segment['text'].replace('-->', '->').strip()}\n",
            file=file,
            flush=True,
        )  

torch.cuda.init()
device = "cuda"

path = "D:\\Movies\\ラヂオの時間\[LonelyChaser] Welcome Back, Mr. McDonald [22FB5C77].mkv"
outpath = "D:\\Movies\\ラヂオの時間\[LonelyChaser] Welcome Back, Mr. McDonald [22FB5C77].srt"
#onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#print(onlyfiles)

model = whisper.load_model("medium").to(device)
#for x in onlyfiles:
with torch.cuda.device(device):
    result = model.transcribe(path, language="japanese", fp16=False)

segments = result['segments']

with open(outpath, "w", encoding='utf8') as srt:
    write_srt(segments, file=srt)

#fileName = path.rsplit(".", 1)[0] + '.srt'
# for segment in segments:
#     startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
#     endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
#     text = segment['text']
#     segmentId = segment['id']+1
#     try: 
#         segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
#         with open(outpath, 'a', encoding='utf8') as writeFile:
#             writeFile.write(segment)
#     except:
#         print("error generating segment") 
    


#print("processed: " + fileName)