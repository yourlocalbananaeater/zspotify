SAVED_TRACKS_URL = 'https://api.spotify.com/v1/me/tracks'

TRACKS_URL = 'https://api.spotify.com/v1/tracks'

TRACK_STATS_URL = 'https://api.spotify.com/v1/audio-features/'

TRACKNUMBER = 'tracknumber'

DISCNUMBER = 'discnumber'

YEAR = 'year'

ALBUM = 'album'

TRACKTITLE = 'tracktitle'

ARTIST = 'artist'

ARTISTS = 'artists'

ALBUMARTIST = 'albumartist'

ARTWORK = 'artwork'

TRACKS = 'tracks'

TRACK = 'track'

ITEMS = 'items'

NAME = 'name'

ID = 'id'

URL = 'url'

RELEASE_DATE = 'release_date'

IMAGES = 'images'

LIMIT = 'limit'

OFFSET = 'offset'

AUTHORIZATION = 'Authorization'

IS_PLAYABLE = 'is_playable'

DURATION_MS = 'duration_ms'

TRACK_NUMBER = 'track_number'

DISC_NUMBER = 'disc_number'

LYRICS = ['lyrics']

SHOW = 'show'

ERROR = 'error'

EXPLICIT = 'explicit'

PLAYLIST = 'playlist'

PLAYLISTS = 'playlists'

OWNER = 'owner'

DISPLAY_NAME = 'display_name'

ALBUMS = 'albums'

TYPE = 'type'

PREMIUM = 'premium'

USER_READ_EMAIL = 'user-read-email'

PLAYLIST_READ_PRIVATE = 'playlist-read-private'

USER_LIBRARY_READ = 'user-library-read'

WINDOWS_SYSTEM = 'Windows'

CODEC_MAP = {
    'aac': 'aac',
    'fdk_aac': 'libfdk_aac',
    'm4a': 'aac',
    'mp3': 'libmp3lame',
    'ogg': 'copy',
    'opus': 'libopus',
    'vorbis': 'copy',
}

EXT_MAP = {
    'aac': 'm4a',
    'fdk_aac': 'm4a',
    'm4a': 'm4a',
    'mp3': 'mp3',
    'ogg': 'ogg',
    'opus': 'ogg',
    'vorbis': 'ogg',
}

# Flag to check lyrics format download. Choose txt for regular text lyrics, lrc for time synced lyrics
LYRICS_FORMAT = 'lrc'
# embed embeds the lyrics into the mp3 file, choose standalone for a putting it into a separate file.
LYRICS_LOCATION = 'embed'

LYRICS_URL = "https://spclient.wg.spotify.com/color-lyrics/v2/track/"