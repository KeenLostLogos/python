import unittest
from television import Television


class TestTelevision(unittest.TestCase):

    def test_init(self):
        tv = Television()
        self.assertEqual("Power = False, Channel = 0, Volume = 0", tv.__str__())

    def test_power(self):
        tv = Television()
        self.assertEqual("Power = False, Channel = 0, Volume = 0", tv.__str__())
        tv.power()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", tv.__str__())
        tv.power()
        self.assertEqual("Power = False, Channel = 0, Volume = 0", tv.__str__())

    def test_muted(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        self.assertEqual("Power = True, Channel = 0, Volume = 1", tv.__str__())
        tv.mute()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", tv.__str__())
        tv.mute()
        self.assertEqual("Power = True, Channel = 0, Volume = 1", tv.__str__())
        tv.power()
        tv.mute()
        self.assertEqual("Power = False, Channel = 0, Volume = 1", tv.__str__())
        tv.mute()
        self.assertEqual("Power = False, Channel = 0, Volume = 1", tv.__str__())

    def test_channel_up(self):
        tv = Television()
        tv.channel_up()
        self.assertEqual("Power = False, Channel = 0, Volume = 0", tv.__str__())
        tv.power()
        tv.channel_up()
        self.assertEqual("Power = True, Channel = 1, Volume = 0", tv.__str__())
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", tv.__str__())

    def test_channel_down(self):
        tv = Television()
        tv.channel_down()
        self.assertEqual("Power = False, Channel = 0, Volume = 0", tv.__str__())
        tv.power()
        tv.channel_down()
        self.assertEqual("Power = True, Channel = 3, Volume = 0", tv.__str__())

    def test_volume_up(self):
        tv = Television()
        tv.volume_up()
        self.assertEqual("Power = False, Channel = 0, Volume = 0", tv.__str__())
        tv.power()
        tv.volume_up()
        self.assertEqual("Power = True, Channel = 0, Volume = 1", tv.__str__())
        tv.mute()
        tv.volume_up()
        self.assertEqual("Power = True, Channel = 0, Volume = 2", tv.__str__())
        tv.volume_up()
        self.assertEqual("Power = True, Channel = 0, Volume = 2", tv.__str__())

    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.power()
        tv.volume_down()
        self.assertEqual("Power = False, Channel = 0, Volume = 2", tv.__str__())
        tv.power()
        tv.volume_down()
        self.assertEqual("Power = True, Channel = 0, Volume = 1", tv.__str__())
        tv.volume_up()
        tv.mute()
        tv.volume_down()
        self.assertEqual("Power = True, Channel = 0, Volume = 1", tv.__str__())
        tv.volume_down()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", tv.__str__())
        tv.volume_down()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", tv.__str__())


if __name__ == "__main__":
    unittest.main()
