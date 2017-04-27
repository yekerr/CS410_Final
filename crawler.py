import os
import sys
from parser import *
import pickle
base_url = "http://lyrics123.net/"

#artist_initial = ["1", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
#               "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
#               "x", "y", "z"]

# change this to specify the page. all options are above
artist_initial = ["a", "b"]

all_data = []

for initial in artist_initial:
    data_with_initial = []
    artist_list_url = os.path.join(base_url, "artists", initial)
    artists = getListOfArtist(artist_list_url)
    totalArtists = len(artists)
    print "crawling artists starting with " + initial
    for i in range(totalArtists):
        # visualize the progress when each artist is done crawling
        print "{0:.3f}%\r".format((i+1) / float(totalArtists) * 100),
        sys.stdout.flush()

        # doing actual crawing
        artist = artists[i]
        artist_url = os.path.join(base_url, artist.attrs['href'])
        songs = getListofSongs(artist_url)
        for song_suffix in songs:
            song_url = os.path.join(base_url, song_suffix.attrs['href'])
            song = getSongFromURL(song_url)
            if song is not None:
                all_data.append(song)
                data_with_initial.append(song)
    pickle.dump(data_with_initial, open(initial + "_songs.dat", 'wb'))

# save all data
pickle.dump(all_data, open("songs.dat", 'wb'))

