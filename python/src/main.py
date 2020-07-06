import argparse
import skyTransformer as sky

def main():
    parser = argparse.ArgumentParser(description='Sky Notation Tranformer')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', help="list support formats", action="store_true")
    group.add_argument('-s', '--show', help="show usage example ", action="store_true")
    parser.add_argument('-i', '--input_file', help="input file name")
    parser.add_argument('-o', '--output', help="output file name(no path)")
    
    args = parser.parse_args()

    if args.list:
        sky.cmd_list()
        return 0

    if args.show:
        sky.cmd_help()
        return 0

    if args.input_file:
        input_name = args.input_file
    else:
        print("input file is required, use -h / -s to show help/usage")
        return 0
    
    if args.output:
        output_name = args.output
    else:
        output_name = input_name.split('.')[0] + '.png'


    sky.sky_trans(input_name, output_name)

if __name__ == "__main__":
    main()
