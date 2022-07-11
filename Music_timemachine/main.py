from bs4 import BeautifulSoup
import requests
SPOTIPY_CLIENT_ID = "5852ae79a26548619a1fa71664e38f56"
SPOTIPY_CLIENT_SECRET = "164acf9859df466ba9dd2d8857b860bf"
import spotipy
from spotipy.oauth2 import SpotifyOAuth

## prompt the time to travel back
given_time = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD:")
year = given_time.split("-")[0]
month = given_time.split("-")[1]
date = given_time.split("-")[2]

## Get the soup of web
response = requests.get(f"https://www.billboard.com/charts/hot-100/{given_time}/")
billboard_web = response.text
soup = BeautifulSoup(billboard_web, "html.parser")

## to fetch the song list
song_name_list = []
top_song = soup.find(class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet "
                            "lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis "
                            "u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
song_name_list.append(''.join(top_song.get_text().split()))
song_name = soup.find_all(class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                 "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                 "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                 "u-max-width-230@tablet-only")
remaining_list = [''.join(song.get_text().split()) for song in song_name]
song_name_list.extend(remaining_list)

## To fetch track ##
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                                cache_path="token.txt"))
song_id_list = []
for name in song_name_list:
    user = sp.search(q='track:' + name, type='track')
    try:
        song_id_list.append(user['tracks']['items'][0]['id'])
    except:
        print("No song found, skipped!")
        pass

## create a playlist
username = sp.current_user().get("id")
playlist = sp.user_playlist_create(username, f"{given_time} Billboard 100", public=False, description="Takes top 100 "
                                                                                                      "misic from date "
                                                                                                      "in past to create "
                                                                                                      "a Spotify playlist")
## add track into playlist
playlist_id = playlist.get("id")
if sp.playlist_add_items(playlist_id, song_id_list):
    print("Successful")


