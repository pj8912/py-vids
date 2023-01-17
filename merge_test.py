import cv2

# Read in the two videos
video1 = cv2.VideoCapture("Sobriety.mp4")
video2 = cv2.VideoCapture("muted_temple.mp4")

# Get the frames per second (fps) and the codec of video1
fps = int(video1.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*"MJPG")

# Get the frames per second (fps) and the codec of video2
fps2 = int(video2.get(cv2.CAP_PROP_FPS))
fourcc2 = int(video2.get(cv2.CAP_PROP_FOURCC))

# Define the codec and create VideoWriter object
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame1.shape[1], frame1.shape[0]+frame2.shape[0]), isColor=True)

# Read the frames
while True:
    # Read the frames
    _, frame1 = video1.read()
    _, frame2 = video2.read()
    if not _:
        break
    
    # Resize frame2 to match the width of frame1
    frame2 = cv2.resize(frame2, (frame1.shape[1], frame2.shape[0]))

    # Concatenate the frames vertically
    result = cv2.vconcat([frame1, frame2])

    # Write the resulting frame to the output file
    out.write(result)

# Release everything if job is finished
video1.release()
video2.release()
out.release()
cv2.destroyAllWindows()
