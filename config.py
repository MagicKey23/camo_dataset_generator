import argparse
import textwrap
def getConfig():
    # Format the args parser

    parser = argparse.ArgumentParser(prog='Help Tool',
                                     formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40))

    # Training parameter settings
    parser.add_argument('--width', type=int, default=800,
                        help='Width of the image (Minimum value: 0)')
    parser.add_argument('--height', type=int, default=600,
                        help='Height of the image (Minim value: 0)')
    parser.add_argument('--polygon_size', type=int, default=400,
                        help='Minimum perimeter of a polygon (Minimum value: 0)')
    parser.add_argument('--color_bleed', type=int, default=0,
                        help='Bleeding of the colors, i.e. number of neighbouring polygons with the same color')
    parser.add_argument('--colors', type=list, default=['#264722', '#023600', '#181F16'], help='List of all the colors.')
    parser.add_argument('--max_depth', type=int, default=15,
                        help='Maximum depth for creating the polygon')
    parser.add_argument('--num_spot', type=int, default=0,
                        help='Number of spots (Minimum value: 0)')
    parser.add_argument('--radius', type=dict, default={'min': 0, 'max': 10}, help='Dictionary with the min and max radius')
    parser.add_argument('--spot_var', type=int, default=5, help='Variation for the sampling, i.e. how far it goes looking for the color for the spot.')
    parser.add_argument('--pixel_scale', type=int, default=0.2,
                        help='Percentage of pixelization (Between 0 and 1)')
    parser.add_argument('--pixel_var', type=int, default=4,
                        help='Variation for the sampling, i.e. how far it goes looking for the color for the spot.')
    parser.add_argument('--density', type=dict, default={'x': 100, 'y': 200},
                        help='Density of the pixels, i.e. inverse of the size of the pixels.')

    opt = parser.parse_args()

    return opt


if __name__ == '__main__':
    opt = getConfig()
    opt = vars(opt)
    print(opt)