from src.channel import Channel


class Video:
    """
    Класс для видео
    """
    youtube = Channel.get_service()

    def __init__(self, video_id: str) -> None:
        self.__video_id = video_id
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None
        self.duration = None
        self._get_info(video_id)

    def _get_info(self, video_id):
        """
        Получение информации о видео
        """
        try:
            info = self.youtube.videos().list(id=video_id, part='snippet, statistics, contentDetails').execute()
            item = info.get('items')[0]
        except IndexError:
            pass
        else:
            self.title = item.get('snippet').get('title')
            self.url = f'https://youtu.be/{video_id}'
            self.view_count = item.get('statistics').get('viewCount')
            self.like_count = item.get('statistics').get('likeCount')
            self.duration = item.get('contentDetails').get('duration')

    @property
    def video_id(self) -> str:
        return self.__video_id

    def __str__(self) -> str:
        return self.title


class PLVideo(Video):
    """
    Класс для видео c информацией о плейлисте где оно находится
    """
    def __init__(self, video_id: str, pl_id: str) -> None:
        super().__init__(video_id)
        self.__pl_id = pl_id

    @property
    def pl_id(self) -> str:
        return self.__pl_id
