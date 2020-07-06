import skyDecoder as sdr
import skyEncoder as ser
import skyConfig as skycfg
import skyDisplayer as splayer

def cmd_help():
    print("Example Usage : python main.py -i test.txt -o test.png")
    print("Example Usage : python main.py -i test.txt -o notation.txt")

def cmd_list():
    enc_list = skycfg.input_format_configs
    displayer_list = skycfg.output_format_configs

    print("Support Input Format : ")
    for enc in enc_list:
        print(enc)

    print("Support Output Format")
    for displayer in displayer_list:
        print(displayer)


def handle_input(input_format):
    ipf_map = skycfg.input_format_map
    
    if input_format in ipf_map:
        format_name = ipf_map[input_format]
    else:
        format_name = None

    if format_name == 'origin':
        return ser.originEncoder()
    elif format_name == 'abc':
        print("NO IMPLEMNT TO HANDLE ABC FORMAT")
        return None
    else:
        print("NO IMPLEMNT TO HANDLE {} FORMAT".format(input_format))
        return None

def handle_output(output_format):
    opf_map = skycfg.output_format_map

    if output_format in opf_map:
        format_name = opf_map[output_format]
    else:
        format_name = None

    if format_name == 'cmd':
        return splayer.cmdPlayer()
    elif format_name == 'pics':
        return splayer.picsPlayer()
    else:
        print("NO IMPLEMENT FOR OUTPUT {} FORMAT".format(output_format))
        return None

def sky_trans(input_filename, output_name):
    # Get File Format
    input_format = input_filename.split('.')[-1]
    output_format = output_name.split('.')[-1]

    # set encoder , decoder and displayer
    enc = handle_input(input_format)
    dec = sdr.originDecoder()
    displayer = handle_output(output_format)

    if None in (enc, dec, displayer):
        exit(0)

    # process
    data = enc.readfile(input_filename)
    data = enc.process(data)
    data = dec.map2coord(data)
    displayer.display(data, output_name)


if __name__ == '__main__':
    '''
    enc = ser.originEncoder()
    dec = sdr.originDecoder()
    #displayer = splayer.cmdPlayer()
    displayer = splayer.picsPlayer()

    data = enc.readfile("test/test_origin.txt")
    data = enc.process(data)
    data = dec.map2coord(data)
    displayer.display(data)
    '''

    #sky_trans("test/test_origin.txt", "test.png")
    sky_trans("test/test_origin.txt", "test.txt")
