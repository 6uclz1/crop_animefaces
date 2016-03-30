import cv2
import sys
import glob
import os

cascade_file = str(os.path.expanduser('~')) + "/.pyenv/versions/\
anaconda2-2.5.0/share/OpenCV/lbpcascades/lbpcascade_animeface.xml"

directory = sys.argv[1]

if not os.path.exists(directory):
    os.makedirs(directory)

def detect(image):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    cascade = cv2.CascadeClassifier(cascade_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    print faces
    return faces

for image_files in glob.glob('*.jpg'):
    face_num = 0
    image = cv2.imread(image_files)
    faces = detect(image)
    print image_files

    for (x, y, w, h) in faces:
        crop = image[y:y + h, x:x + w]
        savename = str(face_num).zfill(4) + str(image_files) + '.jpg'
        cv2.imwrite(os.path.join(directory, savename), crop)
        face_num += 1
