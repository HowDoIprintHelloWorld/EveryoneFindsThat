# Everyone finds that


## What is this
I've made a simple tool which downloads all songs saved on the [Italodiscoboutique Bandcamp page](https://italodiscoboutique.bandcamp.com/). Then, with vlc, you can easily skim through all songs 
and automatically skip to the middle of each one. Unfortulately, the program is not threaded, meaning that it took *me* 1.5h to download all songs (Results may vary). Still, this makes skimming through them a breeze. 
Make yourself a coffee while you're downloading and have a listen sometime later.


## Usage
Note that I only tested this on Linux. It *should* also work on MacOS, it *probably* doesn't work on Windows, at least the playing bit. You can still *maybe* download the songs just fine.

Use the following command to download all songs in all albums:

`python3 main.py download`


To launch VLC and start each song 90 seconds in (Because I'm assuming the snippet we have is not at the start of the song, so you'd always have to
skip forwards each song) run the following command:

`python3 main.py play`

## Other purposes:
You can also download some pretty neat songs :)
