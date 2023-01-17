from moviepy.editor import *

# Read in the two videos
video1 = VideoFileClip("Sobriety.mp4")
video2 = VideoFileClip("muted_temple.mp4")

# resize the video 2 to match the width of video 1
video2 = video2.resize(width=video1.w)

# Concatenate the videos vertically
result = concatenate_videoclips([video1, video2], method='compose')

# write the final video
result.write_videofile("output.mp4")

