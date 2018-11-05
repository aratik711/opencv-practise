import cv2, os

images_arr = os.listdir("sample-images/")
print(images_arr)
i=0
for image in images_arr:
    i += 1
    img = cv2.imread("sample-images/" + image, 0)
    print(image)
    print(img.shape)
    resized_img = cv2.resize(img, (100,100))
    cv2.imwrite(str(i)+".jpg", resized_img)
    cv2.imshow("image", resized_img)
