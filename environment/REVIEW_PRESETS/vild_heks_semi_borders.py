import sys
import subprocess


src = sys.argv[1]
dst = sys.argv[2]

args = [
    "ffmpeg", "-y", "-i", src,
    "-vf", "drawbox=c=black@0.5:t=148:x=-t:w=iw+(t*2)", "-crf", "0", dst
]

subprocess.call(args)
