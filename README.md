# bs-pp-playlist
BeatSaber PP playlist generator based on DuoVR PPFarming (https://duovr.github.io/PPFarming/)

## Usage
0. Clone repo and enter to its directory
1. Put your playlist cover to `cover.png` (png 256x256px)
2. Change playlist name and author in `generate_latest_playlist.py` code
3. Run `./generate_latest_playlist.py > your_new_playlist.json` (or `python3 generate_latest_playlist.py > xxx.json`)
4. Copy generated playlist to `<beat_saber_dir>/Playlist/`
5. Playlist should be available in game

## Notes
* Order of songs in the playlist will be the same as on https://duovr.github.io/PPFarming/ website
