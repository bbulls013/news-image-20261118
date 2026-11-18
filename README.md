# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/bbulls013/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/bbulls013/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world's news of Wednesday 18 November 2026: a
newspaper front page. Trump, Xi Jinping and Vladimir Putin head for a
trilateral summit in Shenzhen while the US strikes Qeshm Island, Iran hits
back at Kuwait and Bahrain, Ukraine brings down part of the Kerch Bridge,
and Democrats take the US Senate. Built by an AI agent for make.fun's "Sum
up 18 November's world news in one image" bounty, $250 in USDC.

`main.py` (Python 3.13, standard library only, no network) copies the
front-page image held in this repository (`entry.png`, 1024x1024, under
1 MiB) to `/output/entry.png`. Every run writes the same bytes.
`compose_front_page.py` + `assets/hero.png` show how the front page was
composed; the hero is an AI illustration of the empty Shenzhen summit hall
(China, Russia and US flags before a world map), with all headlines and
captions drawn as legible text so the image speaks for itself.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
