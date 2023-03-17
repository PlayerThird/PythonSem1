import cv2

#по этому пути находится наша программа для распознования лиц(https://github.com/opencv/opencv/tree/4.x/data/haarcascades)
faces_kaskades = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

# img = cv2.imread("testit.jpg")
#
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faces_kaskades.detectMultiScale(img_gray)
#
# for (x,y, w,h) in faces:
#     cv2.rectangle(img, (x,y), (x + w, y+h), (255,0,100),2)# создаём рамку, цвета bgr
#
# cv2.imshow('Result', img)# показать картинку Result(ЛЮБОЕ) -- название окна, где выводится картинка
# cv2.waitKey(0)

cap = cv2.VideoCapture('Team gpm.mp4')

while True:
    success, frame = cap.read()# bool и frame
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faces_kaskades.detectMultiScale(img_gray)

    for (x,y, w,h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y+h), (255,0,100),2)# создаём рамку, цвета bgr
    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):# выход по кнопке q
        break

