import cv2
img=cv2.imread('island.jpeg',0)
print(img)
status=cv2.imwrite('island.jpeg',img)
print("Image written to file system:",status)
