from bs4 import BeautifulSoup
from requests import get
from json import loads
from sys import exit, argv
from tqdm import tqdm
from os import listdir, system

start_url = "https://italodiscoboutique.bandcamp.com"

def get_albums() -> list:
    links = []
    with open("links.txt", "r") as f:
        links = f.readlines()
        links = [link[link.index("\"")+1:] for link in links]
        links = [link[:link.index("\"")] for link in links]
        links = [start_url+link for link in links]
    return links


def get_songs(album_link: str) -> list:
    song_links = []
    page = get(album_link).text
    soup = BeautifulSoup(page, "html.parser")
    links = soup.find_all("a")
    for link in links:
        og_link = link
        link = link.get("href")
        if not link:
            continue
        if not link.startswith("/track/"):
            continue
        song_links.append(start_url + link)
    return song_links

# Returns song_link, song_name
def get_song_audio_link(song_link: str) -> (str, str):
    page = get(song_link).text
    soup = BeautifulSoup(page, "html.parser")
    for script in soup.find_all("script"):
        data = script.get("data-tralbum")
        if not data:
            continue
        file_data = loads(data)["trackinfo"][0]
        file_name = file_data["title"]
        song_name = file_name.replace(" ", "") +".webm"
        audio_link = file_data["file"]["mp3-128"]
        return audio_link, song_name


def download_audio(audio_link: str, song_name: str, already_downloaded: list):
    if song_name in already_downloaded:
        return
    file = get(audio_link)
    with open("songs/" + song_name, "wb") as f:
        f.write(file.content)


def get_already_downloaded() -> list:
    names = listdir("songs/")
    return names


def play():
    files = get_already_downloaded()
    for song_name in files:
        system("vlc --start-time=90 " + "songs/"+song_name)


def download():
    already_downloaded = get_already_downloaded()
    for album_link in tqdm(get_albums()):
        for song_link in get_songs(album_link):
            audio_link, song_name = get_song_audio_link(song_link)
            download_audio(audio_link, song_name, already_downloaded)
            already_downloaded.append(song_name)

if __name__ == "__main__":
    commands = {"download": download, "play": play}
    if len(argv) != 2 or argv[1] not in commands.keys():
        print("Please supply argument: \"download\" OR \"play\"")
        exit(1)
    commands[argv[1]]()