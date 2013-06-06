'''
Created on Jun 5, 2013

@author: legolas
'''
import os
import json
import urllib2

#first change

def getPlaylistData():
    videojsons = os.listdir('playlists');
    #print videojsons
    
    count = 0
    for vid in videojsons:
        f = open('playlists/' + vid);
        for line in f:
            data = json.loads(line.decode("utf-8", "replace"))
            if 'entry' in data['feed']:
                entries =  data['feed']['entry']
                for entry in entries:
                    print entry['yt$playlistId']['$t']
                    
                    plylisturl = 'https://gdata.youtube.com/feeds/api/playlists/' + entry['yt$playlistId']['$t'] + '?v=2&alt=json'
                    playlist = urllib2.Request(plylisturl)
                    opener = urllib2.build_opener()
                    videosopen = opener.open(playlist)
                    videosopenjson = json.load(videosopen)
                    newfile = open('videos/youtubev_' + vid + '.json','w') 
                    str = json.dumps(videosopenjson, ensure_ascii=False).encode('utf-8', 'ignore')  
                    newfile.write(str)
                    newfile.close()
                    
            count = count + 1

    print count
    
if __name__ == "__main__":
    getPlaylistData()



