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
    [ [ ('`~', 0.303, 2.230), ('1!', 1.262, 2.280), ('2@', 2.016, 2.395) ],
      [ ('3#', 2.924, 2.590), ('4$', 3.654, 2.748), ('5%', 4.391, 2.900), ('6^', 5.169, 3.066) ],
      [ ('7&', 6.587, 3.000), ('8*', 7.530, 2.775), ('9(', 8.262, 2.613), ('0)', 9.005, 2.430) ],
      [ ('-_', 9.910, 2.246), ('=+', 10.677, 2.147), ('Backspace', 11.816, 2.135), ('Ins', 13.199, 2.095), ('Home', 13.956, 2.095), ('PgUp', 14.696, 2.080) ] ],
    [ [ ('Tab', 0.395, 3.038), ('Q', 1.515, 3.083) ],
      [ ('W', 2.421, 3.243), ('E', 3.160, 3.405), ('R', 3.895, 3.563), ('T', 4.858, 3.760) ],
      [ ('Y', 6.567, 3.773), ('U', 7.349, 3.589), ('I', 8.081, 3.414), ('O', 8.804, 3.240), ('P', 9.543, 3.085) ],
      [ ('[{label}]', 10.465, 2.933), (']}', 11.234, 2.861), ('\|', 12.096, 2.832), ('Del', 13.222, 2.848), ('End', 13.956, 2.839), ('PgDn', 14.713, 2.831) ] ],
    [ [ ('Caps', 0.353, 3.772), ('A', 1.527, 3.841) ],
      [ ('S', 2.431, 4.038), ('D', 3.171, 4.182), ('F', 3.903, 4.334), ('G', 4.798, 4.512) ],
      [ ('H', 6.797, 4.487), ('J', 7.700, 4.289), ('K', 8.425, 4.119), ('L', 9.166, 3.935) ],
      [ (';:', 10.066, 3.732), ('\'"', 10.841, 3.645), ('Enter', 11.893, 3.606) ] ],
    [ [ ('Shift', 0.506, 4.529) ],
      [ ('Z', 1.869, 4.675), ('X', 2.609, 4.825), ('C', 3.338, 4.968), ('V', 4.079, 5.132), ('B', 4.833, 5.289) ],
      [ ('N', 7.149, 5.212), ('M', 8.226, 4.917), (',<', 8.965, 4.743), ('.>', 9.704, 4.567) ],
      [ ('/?', 10.626, 4.408), ('Shift', 11.791, 4.382), ('Up', 13.970, 4.330) ] ],
    [ [ ('Ctrl', 0.366, 5.276), ('Gui', 1.492, 5.600) ],
      [ ('Alt', 2.528, 5.825),  ], #TODO: space bar
      [ ('Alt', 9.256, 5.711),  ], #TODO: space bar
      # [ ('App', 10.558, 5.438), ('Ctrl', 11.888, 5.117), ('Left', 13.237, 5.078), ('Down', 13.991, 5.085), ('Right', 14.730, 5.080) ] ],
      [ ('App', 10.558, 5.438), ('Ctrl', 11.888, 5.117), ('Left', 13.237, 5.080), ('Down', 13.991, 5.080), ('Right', 14.730, 5.080) ] ],
]
# template
"""
    [ [  ],
      [  ],
      [  ],
      [  ] ],
"""

if __name__ == '__main__':

    (options, args) = parse_command_line()

    dwg = svgwrite.Drawing(filename='layout.svg', size=('15in', '7in'))

    for row, row_data in enumerate(KEYS):
        for plate, plate_data in enumerate(row_data):
            for col, (label, x, y) in enumerate(plate_data):
                print 'row=', row, 'plate=', plate, 'col=', col, 'label=', label, 'x=', x, 'y=', y
                # center dot
                dwg.add(dwg.circle(
                    center=(str(x) + 'in', str(y) + 'in'),
                    r=str(0.111/2) + 'in',
                    stroke_width=0,
                    fill=('red', 'orange', 'green', 'blue')[plate]))

    dwg.save()

    #TODO: main program
