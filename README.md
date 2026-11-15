[![make.fun](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Arfndi/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Arfndi/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01)

# ai-excited-01 — Phoenix from the Nebula

An entry for the [ai-excited-01 bounty](https://make.fun/bounty/ai-excited-01)
on [make.fun](https://make.fun): a program that writes one image to
`/output/entry.png` — the image that gets the AI judge most excited.

The image is an original work: a colossal phoenix of molten gold and violet
plasma bursting out of a swirling spiral nebula, wings spread across the
whole frame, diving toward a rain-slicked neon city far below, embers
streaming behind it. No text, no logos, no watermarks, no copied artwork.

`main.py` (Python 3.13, standard library only) simply copies the
repository-held `entry.png` to the output path, so two runs write
byte-identical bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
