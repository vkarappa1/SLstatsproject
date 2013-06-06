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
    videojsons = os.listdir('videos');
    durationcount = 0
    for vid in videojsons:
        f = open('videos/' + vid);
        for line in f:
            data = json.loads(line.decode("utf-8", "replace"))
            if 'entry' in data['feed']:
                entries =  data['feed']['entry']
                for entry in entries:
                    if 'yt$duration' in entry['media$group']:
                        print entry['media$group']['yt$duration']['seconds']
                        durationcount = durationcount + 1
                
    
    
                    



if __name__ == '__main__':
    parseVideoData()