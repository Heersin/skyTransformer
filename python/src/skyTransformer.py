import skyDecoder as sdr
import skyEncoder as ser
import skyConfig as skycfg
import skyDisplayer as splayer


if __name__ == '__main__':
    enc = ser.originEncoder()
    dec = sdr.originDecoder()
    #displayer = splayer.cmdPlayer()
    displayer = splayer.picsPlayer()

    data = enc.readfile("test/test_origin.txt")
    data = enc.process(data)
    data = dec.map2coord(data)
    displayer.display(data)
