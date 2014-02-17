__author__ = 'charlie'

from mutagen.easyid3 import ID3
import fnmatch
import os


def file_list(root, pattern):
    for  r,d,f in os.walk(root):
        for fn in fnmatch.filter(f, pattern):
            yield os.path.join(r, fn)


def compare_artits_albulm_artist(f):

    song = ID3(f)

    if "TPE1" not in song and "TPE2" not in song:
        print f, "NO ARTIST OR ALBUM ARTIST"
        return

    if "TPE1" in song and "TPE2" not in song:
        # print f, "Album Artist Added"
        song["TPE2"] = str(song["TPE1"]).strip()

    elif "TPE2" in song and "TPE1" not in song:
        # print f, "Artist Added"
        song["TPE1"] = str(song["TPE2"]).strip()

    if str(song["TPE1"]) != str(song["TPE2"]):
        # print f, "Preferring Albulm Artist", "[" + str(song["TPE1"]) + "]", "[" + str(song["TPE2"]) + "]"
        song["TPE1"] = str(song["TPE2"]).strip()

    #cleanup whitespace
        song["TPE1"] = str(song["TPE1"]).strip()
        song["TPE2"] = str(song["TPE1"]).strip()

    song.save()

if __name__ == "__main__":
    files = file_list("D:/Media/From Blackberry/", "*.mp3")
    for f in files:
        compare_artits_albulm_artist(f)

