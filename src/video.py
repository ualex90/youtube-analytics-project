from src.channel import Channel


class Video:
    """
    Класс для видео
    """
    youtube = Channel.get_service()

    def __init__(self, video_id: str) -> None:
        self.__video_id = video_id
        self.info = self.youtube.videos().list(id=video_id, part='snippet,statistics').execute()
        self.title = self.info.get('items')[0].get('snippet').get('title')
        self.url = f'https://www.youtube.com/watch?v={video_id}'
        self.viewCount = self.info.get('items')[0].get('statistics').get('viewCount')
        self.likeCount = self.info.get('items')[0].get('statistics').get('likeCount')

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
