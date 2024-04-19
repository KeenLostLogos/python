
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if not self.__status:
            return

        self.__muted = not self.__muted

    def channel_up(self):
        if not self.__status:
            return

        self.__channel = self.__channel + 1 if self.__channel != Television.MAX_CHANNEL else Television.MIN_CHANNEL

    def channel_down(self):
        if not self.__status:
            return

        self.__channel = self.__channel - 1 if self.__channel != Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self):
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
        self.__volume = self.__volume + 1 if self.__volume != Television.MAX_VOLUME else Television.MAX_VOLUME

    def volume_down(self):
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
        self.__volume = self.__volume - 1 if self.__volume != Television.MIN_VOLUME else Television.MIN_VOLUME

    def __str__(self):
        volume = self.__volume if not self.__muted else Television.MIN_VOLUME
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"
