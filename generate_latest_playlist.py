#!/usr/bin/python3
import requests
import json
import base64
import sys
from datetime import date

number_of_top_songs = 300

top_pp_response = requests.get("https://scoresaber.com/api.php?function=get-leaderboards&cat=3&page=1&ranked=1&limit={}".format(number_of_top_songs))
bsaver_data_response = requests.get("https://raw.githubusercontent.com/andruzzzhka/BeatSaberScrappedData/master/beatSaverScrappedData.json")

top_pp = json.loads(top_pp_response.text)
bsaber_data = json.loads(bsaver_data_response.text)

song_hash_key = {}

for song in bsaber_data:
  hash = song['hashMd5'].lower()
  key = song['key']
  song_hash_key[hash] = key

songs = []

for song in top_pp['songs']:
  name = song['name']
  hash = song['id'].lower()
  try:
    key = song_hash_key[hash] 
    songs.append({"songName": name, "key": key})
  except KeyError:
    print("Cannot find \"{}\" song with hash \"{}\" in BeatSaver data, skipping..".format(name, hash), file=sys.stderr)

image_base64 = ""
with open("cover.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    image_base64 = "data:image/png;base64,{}".format(encoded_string.decode("utf-8"))

result = {
  "playlistTitle": "Ranked by PP ({})".format(date.today()),
  "playlistAuthor": "wiadron",
  "image": image_base64,
  "songs": songs
}

print(json.dumps(result, indent=2))
