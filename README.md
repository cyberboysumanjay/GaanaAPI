## Gaana API [Unofficial]

### Show some :heart: and :star: the repo to support the project

[![GitHub stars](https://img.shields.io/github/stars/cyberboysumanjay/gaanaapi.svg?style=social&label=Star)](https://github.com/cyberboysumanjay/GaanaAPI) ![GitHub followers](https://img.shields.io/github/followers/cyberboysumanjay.svg?style=social&label=Follow)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-orange)](https://t.me/sjprojects)
#### Gaana API written in Python using Flask  

 ---
###### **NOTE:** You need to have Gaana link of the song in order to fetch the song details, search feature may be implemented in future if requested.  

 ---
  
#### Features:
##### Currently the API can get the following details for a specific song in JSON format:
- **Album Name**
- **Artist Name**
- **Bitrate Fetched**
- **Duration of song**
- **Song Language**
- **Playable m3u8 Link**
- **Release Date**
- **Album Art Link (Max Resolution)**
- **Song Title**
- **Lyrics**

```json
{
"album":"Alone",
"artist":"Alan Walker",
"bitrate":"96",
"duration":"2min 39sec",
"gaana_url":"https://gaana.com/song/alone-1435",
"language":"English",
"link":"https://vodhls-vh.akamaihd.net/i/songs/54/1854954/21232014/21232014_96.mp4/master.m3u8?set-akamai-hls-revision=5&hdnts=st=1562082331~exp=1562100331~acl=/i/songs/54/1854954/21232014/21232014_96.mp4/*~hmac=1dac0568ef4d53a5aadc314fba45f5b587dc1e098cd7dddb76fe1f1d2b4a24a1",
"released":"Dec 02, 2016",
"thumb":"https://a10.gaanacdn.com/images/albums/54/1854954/crop_640x640_1854954.jpg",
"title":"Alone"
}
```

#### Installation:

Clone this repository using
```sh
$ git clone https://github.com/cyberboysumanjay/GaanaAPI
```
Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
Run the app using
```sh
$ python3 app.py
```
Navigate to 127.0.0.1:5000 to see the Homepage

#### Usage:
Lyrics fetching is optional and is triggered only when ```&lyrics=true``` is added with the url
```sh
http://127.0.0.1:5000/result/?url=<insert-gaana-link-here>&lyrics=true
```
**Example:** Navigate to http://127.0.0.1:5000/result/?url=https://gaana.com/song/alone-1435&lyrics=true to get a json response of song data in return.


### You can fork the repo and deploy on VPS or deploy it on Heroku :)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cyberboysumanjay/gaanaapi/tree/master)
**Note:** Heroku gives US/Europe servers which won't be able to fetch all songs flawlessly. Use any Indian VPS for fetching accurate results.
## Made using this API :heart:
##### [@songdl_bot](https://t.me/songdl_bot) - Song Downloader Bot on Telegram

#### Star the Repo in case you liked it :)
#### Made with :heart: in India

# © [Sumanjay](https://cyberboysumanjay.github.io)
