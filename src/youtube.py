import urllib
import re
from collections import defaultdict
import cPickle as pickle
import json
import urllib2
#import simplejson

def getDataFromURL(url, filename):
	uploads = urllib2.Request(url)
	opener = urllib2.build_opener()
	uploadsopen = opener.open(uploads)
	uploadsopenjson = json.load(uploadsopen)
	newfile = open(filename,'w')
	vidjsonstr = json.dumps(uploadsopenjson, ensure_ascii=False).encode('utf-8','ignore')	
	newfile.write(vidjsonstr)
	newfile.close()
	return uploadsopenjson



def getYoutubeData():
	uidsfile = open('uids.txt')
	uids = uidsfile.readlines()
	linkfile = open('youtubelinks.txt','w')
	count = 0
	uidcount = 0
	key = 'entry'
	#https://gdata.youtube.com/feeds/api/playlists/8BCDD04DE8F771B2?v=2&alt=json
	
	
	for uid in uids:
		downloadcount = 50
		
		usrurl = 'https://gdata.youtube.com/feeds/api/users/' + uid.rstrip() + '/uploads?alt=json&max-results=' + str(downloadcount)
		filename = 'allvideos\youtubev_' + uid.rstrip()  + '_' + str(downloadcount) + '.json'
		uploadsopenjson = getDataFromURL(usrurl,filename)

		totalvids = uploadsopenjson['feed']['openSearch$totalResults']['$t']
		
		print totalvids 
		
		
		while downloadcount < totalvids:
			if key in uploadsopenjson['feed']:     
				for entry in uploadsopenjson['feed']['entry']:
					count = count + 1
					linkfile.write(entry['link'][0]['href'])
					linkfile.write('\n')
			startindex = downloadcount + 1
			downloadcount = downloadcount + 50
			usrurl = 'https://gdata.youtube.com/feeds/api/users/' + uid.rstrip() + '/uploads?alt=json&start-index=' + str(startindex) + '&max-results=50'
			filename = 'allvideos\youtubev_' + uid.rstrip()  + '_' + str(downloadcount) + '.json'
			uploadsopenjson = getDataFromURL(usrurl,filename)
		
		
		'''
		usrplurl = 'https://gdata.youtube.com/feeds/api/users/' + uid.rstrip() + '/playlists?v=2&alt=json'
		playlist = urllib2.Request(usrplurl)
		opener = urllib2.build_opener()
		playlistopen = opener.open(playlist)
		playlistopenjson = json.load(playlistopen)
		newfile = open('playlists\playlist_' + uid.rstrip() + '.json','w')
		pljsonstr = json.dumps(playlistopenjson, ensure_ascii=False).encode('utf-8','ignore')	
		newfile.write(pljsonstr)
		newfile.close() 
		'''
		
		uidcount = uidcount + 1
		
	print count
	
	linkfile.close()




def getYoutubeDataDict():
    return  pickle.load(open( "./youtube.p", "rb" ) )
        
        
if __name__ == "__main__":
	getYoutubeData()
       
	
