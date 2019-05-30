#!/usr/bin/python3
import requests
import json
import base64

response = requests.get("https://raw.githubusercontent.com/DuoVR/PPFarming/master/js/songlist.tsv")
rows = response.text.split('\r\n')

songs = []

for row in rows:
  vals = row.split('\t')
  name = vals[0]
  key = vals[5]
  songs.append({"songName": name, "key": key})

image_base64 = ""
with open("cover.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    image_base64 = "data:image/png;base64,{}".format(encoded_string.decode("utf-8"))

result = {
  "playlistTitle": "Ranked by PP",
  "playlistAuthor": "wiadron",
  "image": image_base64,
  "songs": songs
}

print(json.dumps(result))
