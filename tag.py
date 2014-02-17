__author__ = 'charlie'

from mutagen.id3 import ID3, TIT1 as artist, TIT2 as album_artist
import fnmatch
import os

def file_list(root, pattern):
    for r,d,f in os.walk(root):
        for fn in fnmatch.filter(f, pattern):
            yield os.path.join(r, fn)

ARTIST_KEY = "TPE1"
ALBUM_ARTIST_KEY = "TPE2"

def fix_title(track):
    """@type track: ID3"""

    # No Author or Album Artist then we can't do anything
    if ARTIST_KEY not in track and ALBUM_ARTIST_KEY not in track:
        return

    if ARTIST_KEY not in track and ALBUM_ARTIST_KEY in track:
        a = unicode(track[ALBUM_ARTIST_KEY]).strip()
        print a
        track[ALBUM_ARTIST_KEY] = album_artist(encoding = 3, text = a)
        track[ARTIST_KEY] = artist(encoding = 3, text = a)
        return

    if ALBUM_ARTIST_KEY not in track and ARTIST_KEY in track:
        a = unicode(track[ARTIST_KEY]).strip()
        print a
        track[ARTIST_KEY] = artist(encoding = 3, text = a)
        track[ALBUM_ARTIST_KEY] = album_artist(encoding = 3, text = a)
        return

    a = unicode(track[ARTIST_KEY]).strip()
    aa = unicode(track[ALBUM_ARTIST_KEY]).strip()

    # prefer the album artist if its different (unless it Various!)
    if a != aa and "Various" not in aa:
        track[ARTIST_KEY] = artist(encoding = 3, text = aa)

if __name__ == "__main__":
    files = file_list("D:/Media/From Blackberry/Compilations/Wipeout 3/", "*.mp3")
    for f in files:
        print f
        t = ID3(f)
        fix_title(t)
        t.save()

