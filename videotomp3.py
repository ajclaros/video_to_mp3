import moviepy.editor as mp
file= "" #enter name
clip = mp.VideoFileClip(file+".mp4")
clip.audio.write_audiofile(file+".mp3")
