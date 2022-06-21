import cv2
frameWidth=640
frameHeight=480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
x_1=200
y_1=100
w=128*2+x_1
h=128*2+y_1

img_count=1
while True:
    success, img =cap.read()
    if cv2.waitKey(1) & 0xFF == ord('c'):        
        print(f"face_cap\image{img_count}.png")
        imgCropped = img[y_1:h,x_1:w]
        cv2.imshow("Image Cropped", imgCropped)
        imgResize = cv2.resize(imgCropped,(128,128))
        is_img_write = cv2.imwrite(f"face_cap\image{img_count}.png",imgResize)
        imgResize_1 = cv2.resize(img,(320,240))
        is_img_write_1 = cv2.imwrite(f"face_cap\K_image{img_count}.png",imgResize_1) 
        img_count=img_count+1       
    cv2.rectangle(img,(x_1,y_1),(w,h),(0,0,255),2)
    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break



