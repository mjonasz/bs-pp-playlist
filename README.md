# bs-pp-playlist
BeatSaber PP playlist generator.

It allows you to generate up-to-date Beat Saber playlist with highest PP songs, sorted by PP.

## Usage
0. Clone repo and enter to its directory
1. Put your playlist cover to `cover.png` (png 256x256px)
2. Change playlist name and author in `generate_latest_playlist.py` code
3. Run `./generate_latest_playlist.py > your_new_playlist.json` (or `python3 generate_latest_playlist.py > xxx.json`)
4. Copy generated playlist to `<beat_saber_dir>/Playlist/`
5. Playlist should be available in game

OR just [download ranked_by_pp_latest.json](https://raw.githubusercontent.com/mjonasz/bs-pp-playlist/master/ranked_by_pp_latest.json) playlist from this repo and directly jump to point 4 of guide above.

## Data sources
* http://scoresaber.com/api.php (list of songs with best PP)
* https://github.com/andruzzzhka/BeatSaberScrappedData (convert scoresaber IDs to playlist keys)
