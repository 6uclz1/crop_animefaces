import cv2
import glob

image_types = ('*.jpg', '*.png')

def detect(image):
    cascade = cv2.CascadeClassifier(cascade_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    return faces

for image_files in image_types:
    image = cv2.imread(glob.glob(image_files))

    for (x, y, w, h) in faces:
        num = 0
        crop = image[y:y + h, x:x + w]
        cv2.imwrite(str(image_files) + str(num) + ".jpg"),
                    crop)
        num += 1
