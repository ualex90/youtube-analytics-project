from datetime import timedelta
import re

from src.channel import Channel
from src.video import Video


class PlayList:
    """
     Класс для плейлиста
     """
    youtube = Channel.get_service()

    def __init__(self, playlist_id: str) -> None:
        """
        Инициализация плейлиста
        """
        self.__pl_info = self.youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.__playlist_id = playlist_id
        self.title = self.__pl_info.get('items')[0].get('snippet').get('title')
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'

    def get_videos(self) -> list[Video]:
        """
        "достает" видео из плейлиста и складывает объекты в список
        """
        pl_items_info = self.youtube.playlistItems().list(playlistId=self.__playlist_id, part='snippet').execute()
        videos = [Video(i.get('snippet').get('resourceId').get("videoId")) for i in pl_items_info.get('items')]
        return videos

    @staticmethod
    def duration_to_dict(video_duration) -> dict:
        """
        Преобразует длительность видео с youtube
        в формате PT#H#M#S в словарь
        """
        match = re.match('PT((\d+)H)?((\d+)M)?((\d+)S)?', video_duration).groups()
        duration_dict = {
            'hours': int(match[1]) if match[1] else 0,
            'minutes': int(match[3]) if match[3] else 0,
            'seconds': int(match[5]) if match[5] else 0
        }
        return duration_dict

    @property
    def total_duration(self) -> timedelta:
        """
        Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста
        """
        total = {'hours': 0, 'minutes': 0, 'seconds': 0}
        for video in self.get_videos():
            total = {v: (total.get(v) + k) for (v, k) in self.duration_to_dict(video.duration).items()}
        return timedelta(**total)

    def show_best_video(self) -> str:
        """
        возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        best_url = max(self.get_videos(), key=lambda x: x.likeCount).url
        return best_url
