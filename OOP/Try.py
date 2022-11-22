class TV:
    def __init__(self, channel=2, volumeLevel=4, on=True):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on

    def turnOn(self):
        return self.on

    def turnOff(self):
        return self.on == False
        quit()

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        self.channel = channel

    def getVolume(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        self.volumeLevel = volumeLevel

    def channelUp(self):
        if self.channel == 120:
            channel = 120
        else:
            channel = self.channel
        return self.channel

    def channelDown(self):
        if self.channel == 1:
            channel = 1
        else:
            self.channel = channel
        return self.channel

    def volumeUp(self):
        if self.volume == 7:
            volume = 7
        else:
            self.volumeLevel = volumeLevel
        return self.volumeLevel

    def volumelDown(self):
        if self.volume == 1:
            volume = 1
        else:
            self.volumeLevel = volumeLevel
        return self.volumeLevel