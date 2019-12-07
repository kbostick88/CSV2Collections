import csv
import os
import sys
import json
import requests
import time
import platform
from lxml import html
from plexapi.server import PlexServer
from tmdbv3api import TMDb
from tmdbv3api import Movie
import re

os.system('cls' if os.name == 'nt' else 'clear')

if hasattr(__builtins__, 'raw_input'):
    input=raw_input

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser

parser = ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
didreadreadme = os.path.isfile(config_path)
if not didreadreadme:
    print("You need to read the README. Please create a config.ini in the same folder as this program.")
    print("\n")
    input("Press Enter to exit, and then go and read the README.")
    sys.exit()

parser.read(config_path)
PLEX_URL = parser.get('plex', 'url')
slash = '/'
if (PLEX_URL[-1] == slash):
    PLEX_URL = PLEX_URL.rstrip('//')
PLEX_TOKEN = parser.get('plex', 'token')
MOVIE_LIBRARIES = parser.get('plex', 'library').split(',')
COLLECTION_NAME = input("Collection Name (eg - Disney Classics): ")
CSV_LOCATION = input("File location (eg - Shorts.csv): ")
print("\n")

def script():
    def add_collection(library_key, rating_key, title, year):
        headers = {"X-Plex-Token": PLEX_TOKEN}
        params = {"type": 1,
                  "id": rating_key,
                  "collection[0].tag.tag": COLLECTION_NAME,
                  "collection.locked": 1
                  }
        url = "{base_url}/library/sections/{library}/all".format(base_url=PLEX_URL, library=library_key)
        r = requests.put(url, headers=headers, params=params)
        print("Added {title} ({year}) to {collection}".format(title=title, year=year, collection=COLLECTION_NAME))

    if not os.path.isfile(CSV_LOCATION):
        print("Invalid file specified.")
        print("\n")
        input("Press Enter to exit, and then go and read the README.")
        sys.exit()

    plex = PlexServer(PLEX_URL, PLEX_TOKEN)
   
    all_movies = []
    for movie_lib in MOVIE_LIBRARIES:
        try:
            print("Retrieving a list of movies from the '{library}' library in Plex.".format(library=movie_lib))
            print("\n")
            movie_library = plex.library.section(movie_lib)
            library_language = movie_library.language
            all_movies.extend(movie_library.all())
        except:
            print("The '{library}' library does not exist in Plex.".format(library=movie_lib))
            print("Please check that config.ini exists, and is correct.")
            print("\n")
            input("Press Enter to exit")
            sys.exit()
    print("Finding movies in libraries...")
    print("\n")
   
    with open(CSV_LOCATION) as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=['title', 'year'])
        for row in csv_reader:
            if bool(row['title']) == False:
                continue
            title = row['title']
            year = False
            if bool(row['year']) == False:
                year_search = re.search('.*(\([1-2][0-9][0-9][0-9]\))', row['title'], re.IGNORECASE)
                if year_search:
                    year = year_search.group(1)
                    year = year[1:-1]
                    title = row['title'].replace(" (" + year + ")", "")
                for movie in all_movies:
                    if (movie.title.lower() == title.lower() and str(movie.year) == year):
                        add_collection(movie.librarySectionID, movie.ratingKey, movie.title, movie.year)
    sys.exit()
script()
