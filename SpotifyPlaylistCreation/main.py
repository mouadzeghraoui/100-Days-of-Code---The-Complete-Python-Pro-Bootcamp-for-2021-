# Import Necessary Packages
from bs4 import BeautifulSoup
import requests
import spotipy
import spotipy.util as util


year = input("what year you would like to travel to in YYY-MM-DD format:")
link = "https://www.billboard.com/charts/hot-100/"+ year
response = requests.get(link)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
titles = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
titles = [title.string for title in titles]
singers = soup.find_all(name='span', class_="chart-element__information__artist text--truncate color--secondary")
singers = [singer.string for singer in singers]

complete_list = [(item1+" - "+item2) for (item1, item2) in zip(singers, titles)]
print(complete_list)


# Create a Spotify Playlist
#Initiate Spotipy
scope = 'playlist-modify-public'
username = ''
client_id = ''
client_secret = ''
token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri='http://example.com')
sp = spotipy.Spotify(auth=token)

playlist_name = f"TOP 100 song for {year}"
playlist = sp.user_playlist_create(username, name=playlist_name)


user_id = sp.current_user()["id"]

song_uris = []
year = year.split("-")[0]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)