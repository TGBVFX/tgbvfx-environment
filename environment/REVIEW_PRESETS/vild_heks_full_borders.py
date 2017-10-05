import sys
import subprocess


src = sys.argv[1]
dst = sys.argv[2]
thumbnail = sys.argv[3]

# Generate review movie
args = [
    "ffmpeg", "-y",
    "-i", src,
    "-vf", "drawbox=c=black:t=148:x=-t:w=iw+(t*2)",
    "-crf", "0",
    dst
]

subprocess.call(args)

# Generate thumbnail
args = [
    "ffmpeg", "-y",
    "-i", src,
    "-vf", "drawbox=c=black:t=148:x=-t:w=iw+(t*2),select=gte(n\,1),"
    "scale=300:-1",
    "-vframes", "1",
    thumbnail
]

subprocess.call(args)
