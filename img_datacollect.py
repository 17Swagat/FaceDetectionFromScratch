import cv2 as cv
import uuid
import os

cap = cv.VideoCapture(0)

if not os.path.exists('data'):
    os.mkdir('data')

collectedImgCount = len(os.listdir('data'))

while cap.isOpened():
    ret, frame = cap.read()
    frame_height, frame_width = frame.shape[0], frame.shape[1]
    if not ret:
        print("Error: Cannot receive frame. Exiting...")
        break
    frame_withText = frame.copy()
    # Adding the text to the image:
    cv.putText(img=frame_withText, text=f'Images Captured: {collectedImgCount}', 
               org=(cv.CAP_PROP_FRAME_WIDTH, 50), # (bottom-left corner of the text)
               fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255), 
               thickness=2)

    cv.imshow('Image Collection', frame_withText)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break
    # Save image on pressing 's':=>
    elif key == ord('s'):
        cv.imwrite(filename=os.path.join('data', str(uuid.uuid1()) + '.jpg'), 
                   img=frame) # saving frame without the "Text"
        collectedImgCount = len(os.listdir('data'))
else:
    print('No camera capture')