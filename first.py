import cv2
img=cv2.imread(r'island.jpeg',0)
print(img)
cv2.imshow('color-image',img)

cv2.waitKey(100)
cv2.destroyAllWindows()
