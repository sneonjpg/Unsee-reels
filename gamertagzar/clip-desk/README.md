# GamerTagZar clip desk

A GTA 6 clipping desk for GamerTagZar. It finds trending videos and live streams, picks the best moments, cuts 1080x1920 captioned clips with a hook, and checks them before you post.

Based on [Bodila51/gtavi-claudecode](https://github.com/Bodila51/gtavi-claudecode) (MIT, commit `dd95d39`). The original README is in `UPSTREAM-README.md`.

## What changed from upstream

- **Works without Whisper.** If the transcription model can't download (no access to huggingface.co) or faster-whisper isn't installed, `moments.py` now carries on. It scores on loudness, the YouTube heatmap and chat, and the clips come out without captions. Upstream crashed instead.
- `moments.py --no-transcribe` skips Whisper on purpose, for a fast first pass.
- `cut.py` still works when there is no transcript.

## Folders

- `clip-desk/`: this plugin (skills + scripts).
- `../page/`: GamerTagZar's page folder (playbook, facts, campaigns, scoreboard, media). Run the scripts from there so `jobs/` lands in it. `jobs/` and video files there are git-ignored.

## Run it on your computer

Downloading from YouTube, Twitch and Reddit needs your own machine. The cloud session this was built in can't reach those sites.

```
cd gamertagzar/page
python -m venv .venv && . .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r ../clip-desk/requirements.txt         # plus ffmpeg on PATH
python ../clip-desk/scripts/trends.py --query "gta 6" --hours 24
python ../clip-desk/scripts/streams.py --query "gta 6"
python ../clip-desk/scripts/moments.py "<youtube url>" --top 8
python ../clip-desk/scripts/cut.py jobs/<id> --pick 2 --layout fill --hook "Nobody noticed this"
python ../clip-desk/scripts/check.py jobs/<id>/edits/clip_2.mp4 --campaign campaigns.md
```

Or load it as a Claude Code plugin: `claude --plugin-dir gamertagzar/clip-desk`, then say "Use the clip desk: find today's trending GTA 6 videos and cut 3 clips."

## Rules

Nothing posts automatically. You approve every clip. Only clip creators who run a campaign or have given permission, and credit them in the caption. No leaks, "play early", piracy or GTA Online money content. No earnings are promised: campaigns pay on approved views, under their own rules.
