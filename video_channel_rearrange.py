import cv2

camera=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc("X","V","I","D")
out=cv2.VideoWriter('output.avi',fourcc,30,(640,480))

while(camera.isOpened()):
    ret,frame=camera.read()
    frame_color=cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
    if ret==True:
        out.write(frame_color)
        cv2.imshow('My camera',frame)
        
        cv2.imshow('Canny Detection',frame_color)
        
        if cv2.waitKey(1)==27:
            break
    else:
        break
camera.release()
out.release()
cv2.destroyAllWindows()