import os
import random
import sys
import cv2
import datetime 
import imutils

res = 'pills'#input("\r\nPlease enter model name: ")

dirLst = os.listdir("data")
if res in dirLst:
    #print("\r\nError. Model directory already exists. Please choose some other name or delete the current directory\r\n")
    #sys.exit()
    pass
else:
    print("Making directory structure")
    os.makedirs("data/{}/Annotations".format(res))
    os.makedirs("data/{}/ImageSets/Main".format(res))
    os.makedirs("data/{}/JPEGImages".format(res)) 
    pass 




cap = cv2.VideoCapture("sample_movie/video.mp4")

total_img = 100
fCnt = 1
startTime = datetime.datetime.now()
while True:
    ret, frame = cap.read()
    if not ret:
        break 
    frame = imutils.resize(frame, width=800)
    
    
    cv2.imwrite("data/{}/JPEGImages/{}.png".format(res, fCnt), frame)
    fCnt = fCnt + 1
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if fCnt == total_img:
        break

endTime = datetime.datetime.now()
diff = endTime - startTime
sec = diff.seconds
fps = round(fCnt/sec, 30)
print("Total FPS {}".format(fps))
print("Total Img saved {}".format(fCnt))

allFiles = os.listdir("data/{}/JPEGImages".format(res))

testNum = int(fCnt * 0.10)
testFileLst = []
while True:
    ap = random.choice(allFiles)
    if ap not in testFileLst:
        testFileLst.append(ap)
        if len(testFileLst) == testNum:
            break

trainFileLst = list(set(testFileLst).symmetric_difference(set(allFiles)))

f = open("data/{}/ImageSets/Main/test.txt".format(res), 'w+')
for test in testFileLst:
    test = test.split(".")
    f.write(test[0] + "\n")
f.close()
f = open("data/{}/ImageSets/Main/val.txt".format(res), 'w+')
for test in testFileLst:
    test = test.split(".")
    f.write(test[0] + "\n")
f.close()

f = open("data/{}/ImageSets/Main/train.txt".format(res), 'w+')
for train in trainFileLst:
    train = train.split(".")
    f.write(train[0] + "\n")
f.close()
f = open("data/{}/ImageSets/Main/trainval.txt".format(res), 'w+')
for train in trainFileLst:
    train = train.split(".")
    f.write(train[0] + "\n")
f.close()








