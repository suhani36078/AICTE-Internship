import cv2
img=cv2.imread('ganpati.jpg',1)
print('Original demensions :',img.shape)

widht = 350
height = 450
dim = (widht,height)
# resize image
resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)
ov2.imshow("original image",img)
cv2.imshow("Resized image",resized)
cv2.waitkey(0)
cv2.destroyAllWindows()
