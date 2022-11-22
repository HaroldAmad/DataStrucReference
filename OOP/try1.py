from wait import Television

def main():
    tv1= Television(30, 3, True)
    tv2 = Television(3, 2, True)

    print("The current channel for tv 1 is", tv1.getChannel())
    print("The current volume for tv 1 is", tv1.getVolume())
    print("The current channel for tv 2 is", tv2.getChannel())
    print("The current volume for tv 2 is", tv2.getVolume())

    tv1.setChannel(18)
    print("New Channel tv1:", tv1.getchannel)
    tv1.setVolume(9)
    print("The new current volume for tv 1 is", tv1.getVolume())
    tv2.setChannel(169)
    print("New Channel 2:", tv2.getchannel)
    tv2.setVolume(-5)
    print("The new current volume for tv 2 is", tv2.getVolume())

    tv1.channelUp()
    print("Channel Up 1",tv1.getchannel)
    tv1.channeldown()
    print("Channel down 1",tv1.getChannel())
    tv2.channelUp()
    print("Channel Up 2",tv2.getchannel)
    tv2.channeldown()
    print("Channel Up 2",tv2.getchannel)
    tv1.volumeUp()
    print("Volume Up 1",tv1.getvolume)
    tv1.volumedown()
    print("Volume Down 1",tv1.getvolume)
    tv2.volumeUp()
    print("Volume Up 2",tv2.getvolume)
    tv2.volumedown()
    print("Volume Down 2",tv2.getvolume)

main()
    











    


