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
    vidcount = 0
    viddurfile = open('data_analysis/video_duartions.txt','w')
    for vid in videojsons:
        f = open('allvideos/' + vid);
        for line in f:
            data = json.loads(line.decode("utf-8", "replace"))
            if 'entry' in data['feed']:
                entries =  data['feed']['entry']
                for entry in entries:
                    vidcount = vidcount + 1
                    durationdata[entry['id']['$t']] = vidcount
                    if 'yt$duration' in entry['media$group']:
                        viddurfile.write(entry['media$group']['yt$duration']['seconds'])
                        viddurfile.write('\n')
                        
    viddurfile.close()
    print vidcount
    print len(durationdata.keys())                    
    
if __name__ == '__main__':
    parseVideoData()