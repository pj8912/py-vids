from moviepy.editor import *
video1 = VideoFileClip("Sobriety.mp4")
video2 = VideoFileClip("muted_temple.mp4")

video2 = video2.resize(width=video1.w)

result = concatenate_videoclips([video1, video2], method='compose')

result.write_videofile("output.mp4")

