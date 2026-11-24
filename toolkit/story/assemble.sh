#!/bin/bash
N=$1; D=/home/claude/ep5/e$N; cd $D
F=$(python3 -c "import json;print(int(json.load(open('data.json'))['total']*30)+1)"); H=$((F/2))
until [ -f part_0000.mp4 ] && [ -f $(printf "part_%04d.mp4" $H) ]; do sleep 3; done
printf "file 'part_0000.mp4'\nfile 'part_%04d.mp4'\n" $H > list.txt
ffmpeg -nostdin -v error -y -f concat -safe 0 -i list.txt -c copy v.mp4
ffmpeg -nostdin -v error -y -i v.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -af loudnorm=I=-14:TP=-1.5 -shortest /home/claude/ep5/$2.mp4
echo "DONE $N $(ffprobe -v error -show_entries format=duration -of csv=p=0 /home/claude/ep5/$2.mp4)"
