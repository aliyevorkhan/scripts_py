import cv2

path = "lal/"
cap = cv2.VideoCapture("video2.mp4")

i = 0
counter = 0
stop = 0
while cap.isOpened():
    ret, frame = cap.read()
    counter +=1
    i += 1
    stop += 1
    if not ret:
        break
    if counter >= 100000:
    	if counter % 5 == 0:
            cv2.imwrite(path + 'sack_img_' + str(i) + '.jpg', frame)
            if stop == 113300:
                break
cap.release()
cv2.destroyAllWindows()
