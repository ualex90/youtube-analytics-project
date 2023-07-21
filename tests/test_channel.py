import googleapiclient.discovery

from src.channel import Channel


def test_init(channel):
    assert channel.channel_id == 'UCwHL6WHUarjGfUM_586me8w'
    assert channel.title == 'HighLoad Channel'
    assert len(channel.description) > 3
    assert channel.url.startswith('https://')
    assert int(channel.subscribers) > 0
    assert int(channel.video_count) > 0
    assert int(channel.view_count) > 0


def test_info(channel):
    assert isinstance(channel.info, dict)


def test_get_service(channel):
    assert isinstance(Channel.get_service(), googleapiclient.discovery.Resource)
