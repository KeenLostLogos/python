from television import Television


class TestTelevision:

    def test_init(self):
        tv = Television()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        tv = Television()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        tv.power()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_muted(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        tv.mute()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        tv.mute()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        tv.power()
        tv.mute()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 1"
        tv.mute()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        tv = Television()
        tv.channel_up()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        tv.channel_up()
        assert tv.__str__() == "Power = True, Channel = 1, Volume = 0"
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        tv = Television()
        tv.channel_down()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        tv.channel_down()
        assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        tv = Television()
        tv.volume_up()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        tv.volume_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        tv.mute()
        tv.volume_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 2"
        tv.volume_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.power()
        tv.volume_down()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 2"
        tv.power()
        tv.volume_down()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        tv.volume_up()
        tv.mute()
        tv.volume_down()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        tv.volume_down()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        tv.volume_down()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
