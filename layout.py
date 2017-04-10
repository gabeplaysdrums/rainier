#!python
"""
Generates layout for Rainier keyboard
"""

from optparse import OptionParser
import os
import sys
import svgwrite


def parse_command_line():

    parser = OptionParser(
        usage = '%prog [options]'
    )

    # options

    """
    parser.add_option(
        '-o', '--output', dest='output_path', default='output.txt',
        help='output path',
    )
    """

    (options, args) = parser.parse_args()

    # args

    """
    if len(args) < 1:
        parser.print_usage()
        sys.exit(1)
    """

    return (options, args)


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

# Key information
# [row][plate][col] = ( label, x (inches), y (inches) )
KEYS = [
    [ [ ('Esc', 0.215, 1.269), ('F1', 1.654, 1.365) ],
      [ ('F2', 2.574, 1.535), ('F3', 3.307, 1.703), ('F4', 4.027, 1.860), ('F5', 4.779, 2.010) ],
      [ ('F6', 6.775, 1.978), ('F7', 7.511, 1.804), ('F8', 8.246, 1.631), ('F9', 9.000, 1.471) ],
      [ ('F10', 9.906, 1.286), ('F11', 10.665, 1.188), ('F12', 11.412, 1.147), ('FnLk', 12.168, 1.139), ('PrScn', 13.191, 1.128), ('ScrLk', 13.948, 1.125), ('Pause', 14.695, 1.125) ] ],
]

if __name__ == '__main__':

    (options, args) = parse_command_line()

    dwg = svgwrite.Drawing(filename='layout.svg', width='15in', height='7in')

    for row, row_data in enumerate(KEYS):
        for plate, plate_data in enumerate(row_data):
            for col, (label, x, y) in enumerate(plate_data):
                print 'row=', row, 'plate=', plate, 'col=', col, 'label=', label, 'x=', x, 'y=', y
                # center dot
                dwg.add(dwg.circle(
                    center=(str(x) + 'in', str(y) + 'in'),
                    r=str(0.111/2) + 'in',
                    stroke_width=0,
                    fill = 'black' if plate % 2 == 0 else 'blue'))

    dwg.save()

    #TODO: main program
