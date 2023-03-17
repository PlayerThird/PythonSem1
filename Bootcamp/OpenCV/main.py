import cv2

img = cv2.imread("test.png")
print(img.shape)#размер картинки
# img = cv2.resize(img,(200,200))

cv2.imshow('Result', img)# показать картинку Result -- название окна, где выводится картинка

cv2.waitKey(0)

