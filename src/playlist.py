import datetime

from src.channel import Channel
from src.video import Video


class PlayList:
    """
     Класс для плейлиста
     """
    youtube = Channel.get_service()

    def __init__(self, playlist_id: str) -> None:
        """

        """
        self.__pl_info = self.youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.__playlist_id = playlist_id
        self.title = self.__pl_info.get('items')[0].get('snippet').get('title')
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'

    def get_videos(self) -> list[Video]:
        """
        Метод "достает" видео из плейлиста и складывает объекты в список
        """
        videos: list[Video] = list()
        pl_items_info = self.youtube.playlistItems().list(playlistId=self.__playlist_id, part='snippet').execute()
        for item in pl_items_info.get('items'):
            videos.append(Video(item.get('snippet').get('resourceId').get("videoId")))
        return videos

    @property
    def total_duration(self) -> datetime.timedelta:
        for video in self.get_videos():
            pass
        return None


if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print(pl.url)

    duration = pl.total_duration
    print(duration)  # "1:49:52"
    print(isinstance(duration, datetime.timedelta))  # True
    print(duration.total_seconds())  # 6592.0
