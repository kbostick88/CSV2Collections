# CSV2Collection
Simple script CSV file, match the movies/shows
in your Plex Library and turn them into a collection.


# Disclaimer
I'm not a developer, this was a modified script. The modifications were madde by me, but the orginal file was not developed by me.

# Configuration
Create or edit config.ini with your favourite text editor. Keep config.ini in the same working directory as the script. 

**ONLY _"url="_, _"token="_ and _"library="_ underneath the [plex] header need to be set for the script to work**.

**url=** cannot end with a trailing slash - _**url=http://localhost:32400**_ & _**url=https://plex.woofwoof.wahoo**_ are both 
examples of proper formatting, _**url=https://plex.woofwoof.wahoo/**_ is not.

**token=** can be found using [this guide.](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)
A token can also be found in Tautulli or Ombi if you're using them. _**token=njkjdkHJJKAJKnjSAKJ**_ is an example of correct formatting.

**library=** is pretty self explanatory. Multiple libraries supported, seperated by a comma ",". _**library=Movies and library=4K Movies,Movies,Kids Movies**_ are examples of correct formatting.

**database=** point this to the Plex Media Server folder on your machine usually in the C drive, Users (USERNAME) AppData\Local\Plex Media Server\Plug-in Support\Databases\com.plexapp.plugins.library.db

They are the three variables most people will have to fill in.

**_If, and only IF you're using_** 'The Movie Database' agent instead of Plex Movie you'll also need to edit the _**apikey=**_ variable
located under the [tmdb] header.

**Once complete it should look like**

    [plex]
    url=http://PLEXSERVERURL:32400
    token=REPLACEmeWITHyourTOKEN
    library=Movies,Test Library,Kids
    database=C:\Users\Plex\AppData\Local\Plex Media Server\Plug-in Support\Databases\com.plexapp.plugins.library.db
    

    [tmdb]
    apikey=Optional

# Usage
If you are not using a [standalone binary](https://github.com/deva5610/IMDBList2PlexCollection/releases/) you'll need to install dependencies. Use pip to install the few listed requirements.

pip install -r requirements.txt **_OR_** "pip install lxml" "pip install plexapi" "pip install requests" "pip install tmdbv3api" in turn.

#Run the script, Name the collection, drag and drop a csv file into the program and let it do the rest.



# Issues
TV shows are not working

# Enjoy
This one is simple.
