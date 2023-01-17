import cv2

# Read in the two videos
video1 = cv2.VideoCapture("Sobriety.mp4")
video2 = cv2.VideoCapture("muted_temple.mp4")

# Get the frames per second (fps) and the codec of video1
fps = int(video1.get(cv2.CAP_PROP_FPS))
#fourcc = int(video1.get(cv2.CAP_PROP_FOURCC))

#fourcc = cv2.VideoWriter_fourcc(*"MJPG")

fourcc = cv2.CAP_FFMPEG
# Get the frames per second (fps) and the codec of video2
fps2 = int(video2.get(cv2.CAP_PROP_FPS))
fourcc2 = int(video2.get(cv2.CAP_PROP_FOURCC))


# Get the frames from the videos
_, frame1 = video1.read()
_, frame2 = video2.read()

# Resize the frames to have the same width
frame2 = cv2.resize(frame2, (frame1.shape[1], frame2.shape[0]))

# Concatenate the frames vertically
result = cv2.vconcat([frame1, frame2])

# Define the codec and create VideoWriter object
out = cv2.VideoWriter('output.mp4', fourcc , fps, (result.shape[1], result.shape[0]), isColor=True)

while True:
    # Write the resulting frame to the output file
    out.write(result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
video1.release()
video2.release()
out.release()
cv2.destroyAllWindows()

