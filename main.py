from youtubesearchpython import VideosSearch
import pprint
videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

# print(videosSearch.result)
json = videosSearch.result()
print(json)
# m_json = pprint.pprint(json)
# print(m_json)