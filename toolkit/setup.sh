#!/bin/bash
# Recreates the content toolkit at the paths the scripts expect. Run from the repo root.
set -x
R=$(pwd)
mkdir -p /home/claude/cheat /home/claude/ep5 /home/claude/moon2/web /home/claude/show /home/claude/tts /home/claude/reels2
cp toolkit/pins/* /home/claude/cheat/
cp -r toolkit/story/* /home/claude/ep5/
cp toolkit/story/web/toon.js /home/claude/moon2/web/toon.js
cp toolkit/story/film_template.py /home/claude/moon2/film.py
cp toolkit/slides/make.py /home/claude/reels2/
# carousel slide sources for slideshow reels / TikTok re-use
mkdir -p /home/claude/cheat/car; cp carousels/*.jpg /home/claude/cheat/car/ 2>/dev/null
[ -d /home/claude/show/node_modules/three ] || (cd /home/claude/show && npm init -y >/dev/null && npm i three@0.160.0 >/dev/null)
pip install --break-system-packages -q kokoro-onnx soundfile scipy pocketsphinx 2>/dev/null
cd /home/claude/tts
[ -f kokoro.onnx ] || curl -sSL -o kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
[ -f voices.bin ] || curl -sSL -o voices.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
ls -la /home/claude/tts
