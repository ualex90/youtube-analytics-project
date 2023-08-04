import json
from pathlib import Path

from googleapiclient.discovery import build

from settings import API_KEY, FIXTURES


class Channel:
    """
    Класс для ютуб-канала
    """
    # специальный объект для работы с YouTube API
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API.
        """
        self.__channel_id = channel_id
        self.__info = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__title = self.__info.get('items')[0].get('snippet').get('title')
        self._description = self.__info.get('items')[0].get('snippet').get('description')
        self._url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self._subscribers = int(self.__info.get('items')[0].get('statistics').get('subscriberCount'))
        self._video_count = int(self.__info.get('items')[0].get('statistics').get('videoCount'))
        self._view_count = int(self.__info.get('items')[0].get('statistics').get('viewCount'))

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self._description

    @property
    def url(self) -> str:
        return self._url

    @property
    def subscribers(self) -> int:
        return self._subscribers

    @property
    def video_count(self) -> int:
        return self._video_count

    @property
    def view_count(self) -> int:
        return self._view_count

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(self.__info)

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API.
        """
        return cls.youtube

    def to_json(self, name=None):
        """
        Сохраняет информацию о канале в файл в папке fixtures.
        Если файл не существует, он будет создан.

        :param name: имя файла
        """
        # Если не задано имя файла, то будет использовано имя из атрибутов
        if name is None:
            file_name = f'{self.__title}.json'
        else:
            file_name = name

        # формирование пути к файлу
        path_to_file = Path(FIXTURES, file_name)

        # если файл не существует, то создать его, иначе переписать существующий
        mode = 'w' if Path(path_to_file).is_file() else 'a'
        with open(path_to_file, mode, encoding='utf-8') as f:
            json.dump(self.__info, f, ensure_ascii=False, indent=4)

    def __add__(self, other):
        return self._subscribers + other.subscribers

    def __sub__(self, other):
        return self._subscribers - other.subscribers

    def __gt__(self, other):
        return self._subscribers > other.subscribers

    def __ge__(self, other):
        return self._subscribers >= other.subscribers

    def __lt__(self, other):
        return self._subscribers < other.subscribers

    def __le__(self, other):
        return self.subscribers <= other.subscribers

    def __eq__(self, other):
        return self._subscribers == other.subscribers

    def __str__(self):
        return f"'{self.title} ({self.url})'"
