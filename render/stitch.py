import subprocess, os, glob
loops = sorted(glob.glob("loops/*.mp4"))
with open("file_list.txt","w") as f:
    for l in loops:
        f.write(f"file '{l}'\n")
subprocess.run([
    "ffmpeg","-f","concat","-safe","0","-i","file_list.txt",
    "-i","audio/moon_whisper_1hr.wav",
    "-shortest","-c:v","copy","-c:a","aac","-b:a","128k",
    "-movflags","+faststart","../SootheScribe_MoonStory_1hr.mp4"
])
