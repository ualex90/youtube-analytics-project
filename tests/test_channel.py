from src.channel import Channel


def test_channel():
    # Test case 1 # channel_id
    channel = Channel('UCwHL6WHUarjGfUM_586me8w')
    assert channel.channel_id == 'UCwHL6WHUarjGfUM_586me8w'
    # Test case 2 # info
    assert isinstance(channel.info, dict)
