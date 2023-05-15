import cv2

img = cv2.imread('boy.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)
print(faces)

cv2.rectangle(img, (236,134), (236+175, 134+175), (0,255,0), 3)

cv2.imshow('Imagem final', img)
cv2.waitKey(0)