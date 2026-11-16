# Sky Whale — ai-excited-01

[![make.fun](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Arfndi/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Arfndi/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01)

An entry for the [ai-excited-01 bounty on make.fun](https://make.fun/bounty/ai-excited-01):
a program that writes one image to `/output/entry.png` — the image that
gets make.fun's AI judge most excited.

## The image

A colossal bioluminescent whale breaches upward through a sea of glowing
clouds above a neon-lit city at night, trailing a spray of sparkling light,
while one tiny human watches from a rooftop far below. Impossible scale,
upward motion, and a rush of awe — the one moment the whole sky is looking at.

The artwork is original, made for this entry: no text, no logos, no
watermarks, no copied images.

## How it works

`main.py` (Python 3.13, standard library only) copies the repository-held
`entry.png` to `/output/entry.png`, byte for byte. Two runs always write
identical bytes.

```sh
python3 main.py
```
