
class Television:
    """
    A Class that mimics basic TV functionality
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to set the default values of the Television
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to toggle the current power state of the Television
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to toggle the current mute state of the Television
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the channel of the television by one unless it is at its maximum in which case it rolls to
        the minimum channel
        """
        if self.__status:
            self.__channel = self.__channel + 1 if self.__channel != Television.MAX_CHANNEL else Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel of the television by one unless it is at its minimum in which case it rolls to
        the maximum channel
        """
        if self.__status:
            self.__channel = self.__channel - 1 if self.__channel != Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume of the television by one unless it is at its maximum in which case it stays at the maximum
        """
        if self.__status:

            if self.__muted:
                self.__muted = False

            self.__volume = self.__volume + 1 if self.__volume != Television.MAX_VOLUME else Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to decrease the volume of the television by one unless it is at its minimum in which case it stays at the minimum
        """
        if not self.__status:

            if self.__muted:
                self.__muted = False

            self.__volume = self.__volume - 1 if self.__volume != Television.MIN_VOLUME else Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method to return the current state of the Television
        :return: the current state details of the television
        """
        volume_string: str = str(self.__volume) if not self.__muted else str(Television.MIN_VOLUME)
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_string}"
