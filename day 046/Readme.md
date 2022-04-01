<h1 align="center">
    100 Days of Code: Day 46
  <br>
</h1>

## Objective 
- The goal of today's project is to use the musical time machine to build a Spotify playlist.

## main.py
- The user is asked to enter a date,  of which they want to listen the top 100 songs.
- The name of top under 100 songs on that date are fetched using the BeautifulSoup library from the [billboard website](https://www.billboard.com/).
- The spotipy library is used to authenticate Spotify.
- Once the connection has been established, the songs in the songs_list[] are searched on Spotify and their urls are added to the song_urls[].
- Following that, a new playlist is created with all of the previously specified songs in the songs_list[].
