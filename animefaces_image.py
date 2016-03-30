import cv2
import sys
import glob
import os

cascade_file = "~/.pyenv/versions/anaconda2-2.5.0/\
                  share/OpenCV/lbpcascades/lbpcascade_frontalcatface.xml"
directory = sys.argv[1]

def detect(image):
    cascade = cv2.CascadeClassifier(cascade_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    print faces
    return faces

if not os.path.exists(directory):
    os.makedirs(directory)

for image_files in glob.glob('*.jpg'):
    image = cv2.imread(image_files)
    faces = detect(image)
    print image_files

    for (x, y, w, h) in faces:
        num01 = 0
        crop = image[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(directory,
                    str(num01).zfill(8) + str(image_files) + ".jpg"),
                    crop)
        num01 += 1
