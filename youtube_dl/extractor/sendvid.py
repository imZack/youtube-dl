# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class SendvidIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?sendvid\.com/(?P<id>[0-9a-z]+)'
    _TEST = {
        'url': 'https://sendvid.com/b6ro83t4',
        'md5': '3bd69c6a4bbb43351b2ad5bdfd74b1fa',
        'info_dict': {
            'id': 'b6ro83t4',
            'ext': 'mp4',
            'title': 'funny foothball',
            'thumbnail': 'https://sendvid.com/b6ro83t4.jpg'
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        a = {
            'id': video_id,
            'title': self._og_search_title(webpage),
			'url': self._parse_html5_media_entries(url, webpage, video_id)[0]['formats'][0]['url']
        }

        return {
            'id': video_id,
            'title': self._og_search_title(webpage),
			'url': self._parse_html5_media_entries(url, webpage, video_id)[0]['formats'][0]['url'],
			'thumbnail': 'https://sendvid.com/{}.jpg'.format(video_id)
        }
