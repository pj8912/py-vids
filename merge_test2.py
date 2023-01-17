import cv2

# Read in the two videos
video1 = cv2.VideoCapture("Sobriety_Checkpoint.mp4")
video2 = cv2.VideoCapture("muted_temple.mp4")

# Get the frames per second (fps) and the codec of video1
fps = int(video1.get(cv2.CAP_PROP_FPS))
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# fourcc = cv2.VideoWriter_fourcc(*"H264")
# fourcc = int(video1.get(cv2.CAP_PROP_FOURCC))
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# fourcc = cv2.VideoWriter_fourcc(*'FMP4')




# Read the frames
while True:
    # Read the frames
    _, frame1 = video1.read()
    _, frame2 = video2.read()
    if not _:
        break
    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame1.shape[1], frame1.shape[0]+frame2.shape[0]), isColor=True)

    # out = cv2.VideoWriter('output.mp4', cv2.CAP_FFMPEG, fps, (frame1.shape[1], frame1.shape[0]), isColor=True)


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
