import cv2
img=cv2.imread('ganpati.jpg',1)
dimensions=img.shape
height=img.shape[0]
channels=img.shape[2]
width=img.shape[1]
size1=img.size
print('Image dimension:',dimensions)
print('Image height:',height)
print('Image width:',width)
print('number of cannels:',channels)
print('Image size:',size1)
b,g,r=cv2.split(img)
merged_img_bgr=cv2.merge((b,g,r))
merged_img_rgb=cv2.merge((r,g,b))
cv2.imshow('original image',img)
cv2.imshow('color_b_image',b)
cv2.imshow('color_g_image',g)
cv2.imshow('color_r_image',r)
cv2.imshow('merged_bgr',merged_img_bgr)
cv2.imshow('merged_rgb',merged_img_rgb)
cv2.waitkey(0)
cv2.destroyAllWindows()


