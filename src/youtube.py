import urllib
import re
from collections import defaultdict
import cPickle as pickle
import json
import urllib2
#import simplejson

def getYoutubeData():
	uidsfile = open('errorids.txt')
	uids = uidsfile.readlines()
	linkfile = open('youtubelinks.txt','w')
	count = 0
	uidcount = 0
	#https://gdata.youtube.com/feeds/api/playlists/8BCDD04DE8F771B2?v=2&alt=json
	
	for uid in uids:
		print uid
		usrurl = 'https://gdata.youtube.com/feeds/api/users/' + uid.rstrip() + '/uploads?alt=json'
		#print usrurl
		uploads = urllib2.Request(usrurl)
		opener = urllib2.build_opener()
		uploadsopen = opener.open(uploads)
		uploadsopenjson = json.load(uploadsopen)
		newfile = open('videos\youtubev_' + uid.rstrip()  + '.json','w')
		vidjsonstr = json.dumps(uploadsopenjson, ensure_ascii=False).encode('utf-8','ignore')	
		newfile.write(vidjsonstr)
		newfile.close()
		key = 'entry'
		if key in uploadsopenjson['feed']:     
			for entry in uploadsopenjson['feed']['entry']:
				#print entry['link'][0]['href']
				count = count + 1
				linkfile.write(entry['link'][0]['href'])
				linkfile.write('\n')
		
		
		usrplurl = 'https://gdata.youtube.com/feeds/api/users/' + uid.rstrip() + '/playlists?v=2&alt=json'
		playlist = urllib2.Request(usrplurl)
		opener = urllib2.build_opener()
		playlistopen = opener.open(playlist)
		playlistopenjson = json.load(playlistopen)
		newfile = open('playlists\playlist_' + uid.rstrip() + '.json','w')
		pljsonstr = json.dumps(playlistopenjson, ensure_ascii=False).encode('utf-8','ignore')	
		newfile.write(pljsonstr)
		newfile.close() 
		
		uidcount = uidcount + 1
		
	print count
	
	linkfile.close()

def getYoutubeDataDict():
    return  pickle.load(open( "./youtube.p", "rb" ) )
        
        
if __name__ == "__main__":
	getYoutubeData()
       
	
