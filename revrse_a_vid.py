import cv2
#capture video
cap=cv2.VideoCapture('output.avi')
#propertise of video
frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps=cap.get(cv2.CAP_PROP_FPS)
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('reversevideo.avi',fourcc,fps,(int(width*.6),int(height*.7)))
#index of last frame
frame_index=frames-1
if(cap.isOpened()):
    while(frame_index!=0):
        #we set current frame position to last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame=cap.read()
        frame=cv2.resize(frame,(int(width*.6),int(height*.7)))
        #writing the reverse video
        out.write(frame)
        #decreminting frame index in each step
        frame_index=frame_index-1
        #printing the progress
        if(frame_index%100==0):
            print(frame_index)
    out.release()
    cap.release()
    cv2.destroyAllWindows()
