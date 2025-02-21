import urllib.parse
from ytmusicapi import YTMusic

def search_for_lyrics(args: list):
	print("search_for_lyrics was called")
	yt = YTMusic()
	url = urllib.parse.urlparse(args[0])
	url_params = urllib.parse.parse_qs(url.query)
	# check if we have a valid url. If not, we'll have to treat the argument as a song name.
	if 'v' in url_params and len('v') == 1:
		video_id = url_params['v'][0]

		browse_id = yt.get_watch_playlist(video_id)['lyrics']
		if browse_id is None:
			return None
		lyrics = yt.get_lyrics(browse_id)
		lyrics_string: str = lyrics['lyrics']
		return lyrics_string

	# searching for the video
	else:
		query_string = ' '.join(args)
		search_results = yt.search(query_string, 'songs')
		if len(search_results) == 0:
			return None

		browse_id = yt.get_watch_playlist(search_results[0]['videoId'])['lyrics']
		if browse_id is None:
			return None
		lyrics = yt.get_lyrics(browse_id)
		lyrics_string: str = lyrics['lyrics']
		return lyrics_string

class YTMusicLyricsParser (object):
	def __init__ (self, artist, title):
		self.artist = artist
		self.title = title

	def search (self, callback, *data):
		lyrics = search_for_lyrics([self.title, "-", self.artist])
		callback (lyrics, *data)
