import cv2
import sys
import os.path

dirname = 'output'
cascade_file = "lbpcascade_animeface.xml"

def detect(image):
    cascade = cv2.CascadeClassifier(cascade_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    return faces

video_path = sys.argv[1]
cptr = cv2.VideoCapture(video_path)
frame_num = 0

while(1):
    frame_num += 1
    ret, image = cptr.read()
    if not ret:
        break

    if frame_num % 16 == 0:
        faces = detect(image)
        if len(faces) == 0:
            continue

        for (x, y, w, h) in faces:
            crop = image[y:y + h, x:x + w]
            cv2.imwrite(os.path.join(dirname,
                                     "frame_"\
                                     + str(frame_num).zfill(8)\
                                     + ".jpg"),
                        crop)
            print str(frame_num).zfill(8)

cptr.release()
