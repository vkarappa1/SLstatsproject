'''
Created on Jun 6, 2013

@author: legolas
'''

#third change
#fourth change

import os
import json
from collections import defaultdict

durationdata = defaultdict(int)

def parseVideoData():
    videojsons = os.listdir('allvideos');
    durationcount = 0
    viddurfile = open('data_analysis/video_duartions.txt','w')
    vidcount = 0
    linkfile = open('youtubelinks.txt','w')
    
    for vid in videojsons:
        f = open('allvideos/' + vid);
        for line in f:
            data = json.loads(line.decode("utf-8", "replace"))
            if 'entry' in data['feed']:
                entries =  data['feed']['entry']
                for entry in entries:
                    
                    if 'yt$duration' in entry['media$group']:
                        viddurfile.write(entry['media$group']['yt$duration']['seconds'])
                        viddurfile.write('\n')
                    links = entry['link']
                    for link in links:
                        if 'alternate' in link['rel']:
                            linkfile.write(link['href'])
                            linkfile.write('\n')
                        if 'video.related' in link['rel']:
                            print link['href']
                            vidcount =  vidcount + 1
                    
    
    print vidcount                
    viddurfile.close()    
    linkfile.close()                 

if __name__ == '__main__':
    parseVideoData()