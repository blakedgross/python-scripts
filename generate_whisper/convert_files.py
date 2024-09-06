from os import listdir
from os.path import isfile, join, basename

outpath = "G:\\workspace\\transcriptions\\scratch\\podcasts\\Japanese_for_Beginners_Nihongo_con_Teppei\\to_process\\output"
onlyfiles = [f for f in listdir(outpath)]
#print(onlyfiles)

for x in onlyfiles:
    f = open(outpath + "\\" + x, 'r')
    l = open(outpath + "\\new\\" + x, 'w', encoding='utf8')
    fileData = f.read()
    l.write(fileData)
    # try:
    #     for segment in result["segments"]:
    #         f.write(segment["text"] + '\r\n')
    # except:
    #     print("error writing data")

    print("processed: " + x)
    f.close()
