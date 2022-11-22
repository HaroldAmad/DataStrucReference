class Television:

    def __init__(self, channel ,volume, statusTV):
        self.getchannel = channel #Attribute yung self eme eme
        self.getvolume = volume 
        self.statusTV= statusTV
        if self.getchannel >120:
            self.getchannel =120
        elif self.getchannel < 1:
            self.getchannel =1
        if self.getvolume > 7:
            self.getvolume =7
        elif self.getvolume <1:
            self.getvolume =1

    def turnOn(self):#Method
        self.statusTV= True

    def turnOff(self):
        self.statusTV= False


    def getChannel(self):
        if self.getchannel >120:
            self.getchannel =120
        elif self.getchannel < 1:
            self.getchannel =1
        return self.getchannel
    
    def getVolume(self):
        if self.getvolume > 7:
            self.getvolume =7
        elif self.getvolume <1:
            self.getvolume =1
        return self.getvolume

    def setChannel(self, kahitanochannel):
        self.getchannel = kahitanochannel
        if self.getchannel >120:
            self.getchannel =120
        elif self.getchannel < 1:
            self.getchannel =1
        

    def setVolume(self, kahitanovolume):
        self.getvolume = kahitanovolume
        if self.getvolume > 7:
            self.getvolume =7
        elif self.getvolume <1:
            self.getvolume =1

    def channelUp(self):
        if self.getchannel <=119:
            self.getchannel = self.getchannel +1
        
    def channeldown(self):
        if self.getchannel >=2:
            self.getchannel = self.getchannel -1

    def volumeUp(self):
        if self.getvolume <=6:
            self.getvolume = self.getvolume +1

    def volumedown(self):
        if self.getvolume >=2:
            self.getvolume = self.getvolume -1
    
    



