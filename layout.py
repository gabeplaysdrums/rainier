#!python
"""
Generates layout for Rainier keyboard
"""

from optparse import OptionParser
import math
import os
import sys
import svgwrite

KEY_1U_INCHES = 0.70866142


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

def k(label, x, y):
    return (label, x, y, 1)

# Key information
# [row][plate][col] = ( label, x (inches), y (inches), keycap_width (u) )
KEYS = [
    [ [ k('Esc', 0.215, 1.269), k('F1', 1.654, 1.365) ],
      [ k('F2', 2.574, 1.535), k('F3', 3.307, 1.703), k('F4', 4.027, 1.860), k('F5', 4.779, 2.010) ],
      [ k('F6', 6.775, 1.978), k('F7', 7.511, 1.804), k('F8', 8.246, 1.631), k('F9', 9.000, 1.471) ],
      [ k('F10', 9.906, 1.286), k('F11', 10.665, 1.188), k('F12', 11.412, 1.147), k('FnLk', 12.168, 1.139), k('PrScn', 13.191, 1.128), k('ScrLk', 13.948, 1.125), k('Pause', 14.695, 1.125) ] ],
    [ [ k('`~', 0.303, 2.230), k('1!', 1.262, 2.280), k('2@', 2.016, 2.395) ],
      [ k('3#', 2.924, 2.590), k('4$', 3.654, 2.748), k('5%', 4.391, 2.900), k('6^', 5.169, 3.066) ],
      [ k('7&', 6.587, 3.000), k('8*', 7.530, 2.775), k('9(', 8.262, 2.613), k('0)', 9.005, 2.430) ],
      [ k('-_', 9.910, 2.246), k('=+', 10.677, 2.147), k('Backspace', 11.816, 2.135), k('Ins', 13.199, 2.095), k('Home', 13.956, 2.095), k('PgUp', 14.696, 2.080) ] ],
    [ [ k('Tab', 0.395, 3.038), k('Q', 1.515, 3.083) ],
      [ k('W', 2.421, 3.243), k('E', 3.160, 3.405), k('R', 3.895, 3.563), k('T', 4.858, 3.760) ],
      [ k('Y', 6.567, 3.773), k('U', 7.349, 3.589), k('I', 8.081, 3.414), k('O', 8.804, 3.240), k('P', 9.543, 3.085) ],
      [ k('[{label}]', 10.465, 2.933), k(']}', 11.234, 2.861), k('\|', 12.096, 2.832), k('Del', 13.222, 2.848), k('End', 13.956, 2.839), k('PgDn', 14.713, 2.831) ] ],
    [ [ k('Caps', 0.353, 3.772), k('A', 1.527, 3.841) ],
      [ k('S', 2.431, 4.038), k('D', 3.171, 4.182), k('F', 3.903, 4.334), k('G', 4.798, 4.512) ],
      [ k('H', 6.797, 4.487), k('J', 7.700, 4.289), k('K', 8.425, 4.119), k('L', 9.166, 3.935) ],
      [ k(';:', 10.066, 3.732), k('\'"', 10.841, 3.645), k('Enter', 11.893, 3.606) ] ],
    [ [ k('Shift', 0.506, 4.529) ],
      [ k('Z', 1.869, 4.675), k('X', 2.609, 4.825), k('C', 3.338, 4.968), k('V', 4.079, 5.132), k('B', 4.833, 5.289) ],
      [ k('N', 7.149, 5.212), k('M', 8.226, 4.917), k(',<', 8.965, 4.743), k('.>', 9.704, 4.567) ],
      [ k('/?', 10.626, 4.408), k('Shift', 11.791, 4.382), k('Up', 13.970, 4.330) ] ],
    [ [ k('Ctrl', 0.366, 5.276), k('Gui', 1.492, 5.600) ],
      [ k('Alt', 2.528, 5.825), k('Space', 5.845, 6.586) ], #TODO: space bar
      [ k('Space', 5.845, 6.586), k('Alt', 9.256, 5.711) ], #TODO: space bar
      # [ k('App', 10.558, 5.438), k('Ctrl', 11.888, 5.117), k('Left', 13.237, 5.078), k('Down', 13.991, 5.085), k('Right', 14.730, 5.080) ] ],
      [ k('App', 10.558, 5.438), k('Ctrl', 11.888, 5.117), k('Left', 13.237, 5.080), k('Down', 13.991, 5.080), k('Right', 14.730, 5.080) ] ],
]
# template
"""
    [ [  ],
      [  ],
      [  ],
      [  ] ],
"""

def adjacent_keys(row, plate, col):
    left = None
    if col > 0:
        left = KEYS[row][plate][col-1]
    elif plate > 0 and plate != 2:
        left = KEYS[row][plate-1][-1]
    right = None
    if col < len(KEYS[row][plate]) - 1:
        right = KEYS[row][plate][col+1]
    elif plate < len(KEYS[row]) - 1 and plate != 1:
        right = KEYS[row][plate+1][0]
    return left, right

if __name__ == '__main__':

    (options, args) = parse_command_line()

    dwg = svgwrite.Drawing(filename='layout.svg', size=('15in', '7in'))
    dwg.viewbox(0, 0, 15, 7)

    for row, row_data in enumerate(KEYS):
        for plate, plate_data in enumerate(row_data):
            for col, (label, x, y, keycap_width) in enumerate(plate_data):
                print 'row=', row, 'plate=', plate, 'col=', col, 'label=', label, 'x=', x, 'y=', y

                color = ('red', 'orange', 'green', 'blue')[plate]

                # center dot
                dwg.add(dwg.circle(
                    center=(x, y),
                    r=0.111/2,
                    stroke_width=0,
                    fill=color
                ))

                # slope
                left_key, right_key = adjacent_keys(row, plate, col)
                slope_left = 0
                slope_right = 0
                if left_key:
                    label1, x1, y1, keycap_width1 = left_key
                    if (x - x1) != 0:
                        slope_left = (y - y1) /(x - x1)
                if right_key:
                    label1, x1, y1, keycap_width1 = right_key
                    if (x1 - x) != 0:
                        slope_right = (y1 - y) / (x1 - x)
                slope_mean = 0
                if left_key and right_key:
                    slope_mean = (slope_left + slope_right) / 2
                elif left_key:
                    slope_mean = slope_left
                elif right_key:
                    slope_mean = slope_right

                dwg.add(dwg.line(start=(x, y), end=(x + 0.25, y + slope_mean * 0.25), stroke_width=0.01, stroke='gray'))

                # key cap
                keycap_rect = dwg.rect(
                    (x - KEY_1U_INCHES/2, y - KEY_1U_INCHES/2),
                    (KEY_1U_INCHES, KEY_1U_INCHES),
                    fill=color
                )
                keycap_rect.rotate(
                    angle=math.atan(slope_mean) * 180.0 / math.pi,
                    center=(x, y)
                )
                dwg.add(keycap_rect)

    dwg.save()

    #TODO: main program
