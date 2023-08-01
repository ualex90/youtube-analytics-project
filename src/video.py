import googleapiclient.discovery
from googleapiclient.discovery import build

from src.channel import Channel


class Video:
    """
    Класс для видео
    """
    youtube = Channel.get_service()

    def __init__(self, video_id):
        self.__video_id = video_id
        self.info = self.youtube.videos().list(id=video_id, part='snippet,statistics').execute()
        self.title = self.info.get('items')[0].get('snippet').get('title')
        self.viewCount = self.info.get('items')[0].get('statistics').get('viewCount')
        self.likeCount = self.info.get('items')[0].get('statistics').get('likeCount')

    @property
    def video_id(self):
        return self.__video_id


video = Video('AWX4JnAnjBE')
print(video.likeCount)
