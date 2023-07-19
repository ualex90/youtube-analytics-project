from src.channel import Channel


def test_channel():
    channel = Channel('UCwHL6WHUarjGfUM_586me8w')
    assert channel.channel_id == 'UCwHL6WHUarjGfUM_586me8w'    assert isinstance(channel.info, dict)
