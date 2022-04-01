from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth



date = input("Which year you would like to live again? \nEnter in YYYY-MM-DD format:- ")

# Billboard 100 website is scraped and the name of top 100 songs is stored in the song_list[[
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
songs = soup.select(selector="li h3.c-title")
songs_list = []
for song in songs:
    songs_list.append(song.get_text().strip())

# Spotify Authentication is done (Refer to Spotify documentation)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri="https://example.com/", client_id="*****************************",
                     client_secret="***********************", show_dialog=True, cache_path="token.txt"))
user_id = sp.current_user()["id"]


song_urls = []
year = date.split("-")[0]
print(year)

# Songs stored in songs_list[] are searched in the spotify and their urls are stored in song_urls[]
#print("start")

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_urls.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_urls)

#print("end")

# A new playlist is created in spotify and the songs are added to that playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)
