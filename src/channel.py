import os
from googleapiclient.discovery import build


class Channel:
    """
    Класс для ютуб-канала
    """
    # запись API ключа из переменной окружения
    api_key: str = os.getenv('YT_API_KEY')
    # специальный объект для работы с YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id
        self.info = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(self.info)
