import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyautogui
import time

SPOTIFY_CLIENT_ID = "YOUR_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

scope = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=scope))

def get_current_track():
    current_track = sp.currently_playing()
    if current_track and current_track['is_playing']:
        artist = current_track['item']['artists'][0]['name']
        track = current_track['item']['name']
        return f"Now playing: {artist} - {track}"
    return None

def send_to_thug_pro(message):
    pyautogui.press('enter')
    pyautogui.typewrite(message, interval=0.001)
    pyautogui.press('enter')

if __name__ == "__main__":
    last_track = None
    while True:
        try:
            current_track = get_current_track()
            if current_track and current_track != last_track:
                send_to_thug_pro(current_track)
                last_track = current_track
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)
