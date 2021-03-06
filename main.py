import argparse
from mkhdr import *
from ui import start_ui


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory',
                        help="""the directory that contains the
                        original images. If not specified,
                        the current working direcory is used.""")
    parser.add_argument('-o', '--output', default='hdr.jpg',
                        help='the output hdr image filename')
    parser.add_argument('-g', '--gui',
                        help='use gui interface', action='store_true')

    # parse arguments
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        directory = os.getcwd()
    output = args.output

    if args.gui:
        start_ui(sys.argv)
    else:
        files = list_files(directory)
        images, times = read_images(files)
        hdr = make_hdr(images, times)
        hdr.save(output)
