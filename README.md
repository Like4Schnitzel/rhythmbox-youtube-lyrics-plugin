# rhythmbox-youtube-lyrics-plugin
A plugin for Rhythmbox' builtin lyrics plugin that fetches the lyrics from YouTube Music.
Depends on [ytmusicapi](https://github.com/sigma67/ytmusicapi).
## Installation instructions
### Debian:
```bash
git clone https://github.com/Like4Schnitzel/rhythmbox-youtube-lyrics-plugin && \
cd rhythmbox-youtube-lyrics-plugin && \

# Install dependencies
sudo apt install python3-pip python3-venv && \

# Download ytmusicapi. There is currently no deb package so we need to do some hacky stuff.
python3 -m venv .venv && \
.venv/bin/pip install ytmusicapi && \

# Great! We now have ytmusicapi downloaded in .venv/lib/ytmusicapi/ Now we move that whole module into the system's python3.* folder.
sudo mv .venv/lib/python3.*/site-packages/ytmusicapi/ /usr/lib/python3.*/ && \

# Test that the installation was successful.
printf "from ytmusicapi import YTMusic\nyt = YTMusic()\nprint('Module installation successful.')" | python3 && \

# Then we can remove the venv again.
rm -r .venv && \

# Copy YTMusicLyricsParse.py to Rhythmbox' lyrics plugin folder.
sudo cp ./src/YTMusicLyricsParser.py /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/ && \

# Create backup of parser index if it does not already exist
(test -f /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py.bak || \
sudo cp /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py.bak) && \

# Link the parser
printf "\
with open(\"/lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py.bak\", 'r') as file:\n\
\tlines = file.readlines()\n\
\tlines_string = ''.join(lines)\n\
\ts = lines_string.replace(\"import JetlyricsParser\", \"import JetlyricsParser\\\nfrom YTMusicLyricsParser import YTMusicLyricsParser\").replace(\"}\\\n]\", \"},\\\n\\\t{ 'id': 'music.youtube.com','class': YTMusicLyricsParser,'name':_('YouTube Music (music.youtube.com)') }\\\n]\")\n\
\twith open(\"./.tmp\", \"w\") as out_file:\n\
\t\tout_file.write(s)\n\
" | python3 && \
sudo mv .tmp /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py && \

echo "Installation Successful!"
```
### Arch:
```bash
git clone https://github.com/Like4Schnitzel/rhythmbox-youtube-lyrics-plugin && \
cd rhythmbox-youtube-lyrics-plugin && \

# Install dependencies
sudo pacman -S python3 python-ytmusicapi && \

# Copy YTMusicLyricsParse.py to Rhythmbox' lyrics plugin folder.
sudo cp ./src/YTMusicLyricsParser.py /lib/rhythmbox/plugins/lyrics/ && \

# Create backup of parser index if it does not already exist
(test -f /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py.bak || \
sudo cp /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py /lib/x86_64-linux-gnu/rhythmbox/plugins/lyrics/LyricsSites.py.bak) && \

# Link the parser
printf "\
with open(\"/lib/rhythmbox/plugins/lyrics/LyricsSites.py.bak\", 'r') as file:\n\
\tlines = file.readlines()\n\
\tlines_string = ''.join(lines)\n\
\ts = lines_string.replace(\"import JetlyricsParser\", \"import JetlyricsParser\\\nfrom YTMusicLyricsParser import YTMusicLyricsParser\").replace(\"}\\\n]\", \"},\\\n\\\t{ 'id': 'music.youtube.com','class': YTMusicLyricsParser,'name':_('YouTube Music (music.youtube.com)') }\\\n]\")\n\
\twith open(\"./.tmp\", \"w\") as out_file:\n\
\t\tout_file.write(s)\n\
" | python3 && \
sudo mv .tmp /lib/rhythmbox/plugins/lyrics/LyricsSites.py && \

echo "Installation Successful!"
```
### Other Distros:
Idk figure it out. You can submit a PR if you do. Good luck!
