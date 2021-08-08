import re
import math
import collections
from functools import reduce
import numpy as np
from src.common.util import read_input

def parse_input(input):
    images, edges = {}, {}
    id, image, bin_image = -1, [], []

    # add a empty line at the end that serves as a terminator
    input.append('')

    for line in input:
        id_match = re.match(r'Tile (\d+)', line)

        if not line and image:
            top, right, bot, left = bin_image[0], 0, bin_image[-1], 0

            for i, im in enumerate(bin_image):
                left |= (im & 1) << i
                right |= ((im & (1 << (len(bin_image) - 1)))
                          >> (len(bin_image) - 1)) << i

            images[id] = image
            edges[id] = edge_variations((top, right, bot, left), len(bin_image))

            bin_image, image = [], []
        elif id_match:
            id = int(id_match.group(1))
        else:
            bits = 0
            image_line = []

            for i, c in enumerate(line):
                if c == '#':
                    bits |= 1 << i
                    image_line.append(1)
                else:
                    image_line.append(0)

            bin_image.append(bits)
            image.append(image_line)

    return images, edges

def edge_variations(edges, size):
    top, right, bot, left = edges

    def reverse_bits(n, width):
        b = '{:0{width}b}'.format(n, width=width)
        return int(b[::-1], 2)

    result = [(top, right, bot, left)]      # inital orientation
    result.append((reverse_bits(top, size), left, reverse_bits(bot, size), right))  # horizontal flip 1/2
    result.append((bot, reverse_bits(right, size), top, reverse_bits(left, size)))  # vertical flip 1/2
    result.append((reverse_bits(left, size), top, reverse_bits(right, size), bot))  # rotate right 1/3
    result.append((left, bot, right, top))  # horizontal flip 2/2
    result.append((reverse_bits(right, size), reverse_bits(top, size), reverse_bits(left, size), reverse_bits(bot, size)))  # vertical flip 2/2
    result.append((reverse_bits(bot, size), reverse_bits(left, size), reverse_bits(top, size), reverse_bits(right, size)))  # rotate right 2/3
    result.append((right, reverse_bits(bot, size), left, reverse_bits(top, size)))  # rotate right 3/3

    return result

def get_ascii_edge_image(edge, size):
    if size > 1:
        top, right, bot, left = edge
        spaces = size - 2

        top_line, bot_line = '', ''
        center = []

        for i in range(size):
            top_line += '#' if top & 1 << i else '.'
            bot_line += '#' if bot & 1 << i else '.'

            center.append(('#' if left & 1 << i else '.') + ' ' *
                          spaces + ('#' if right & 1 << i else '.'))

        frame = [top_line] + center[1:-1] + [bot_line]

        # for line in frame:
        #     print(line)

        return frame
    return []

def get_ascii_image(image):
    ascii_image = []

    for image_line in image:
        line = ''
        for digit in image_line:
            line += '#' if digit == 1 else '.'
        ascii_image.append(line)

    return ascii_image

def debug_edge_variations(image, edges):
    if len(edges) > 7:
        size = len(image)

        ascii_im = get_ascii_image(image)
        inital = get_ascii_edge_image(edges[0], size)
        hflip_inital = get_ascii_edge_image(edges[1], size)
        vflip_inital = get_ascii_edge_image(edges[2], size)
        rot1 = get_ascii_edge_image(edges[3], size)
        hflip_1 = get_ascii_edge_image(edges[4], size)
        vflip_1 = get_ascii_edge_image(edges[5], size)
        rot2 = get_ascii_edge_image(edges[6], size)
        rot3 = get_ascii_edge_image(edges[7], size)

        print('Image')
        for line in ascii_im:
            print(line)

        print('{:<{width}}  {:<{width}}  {:<{width}}  {:<{width}}'.format(
            'Inital', 'Rot1', 'Rot2', 'Rot3', width=size))

        for line in zip(inital, rot1, rot2, rot3):
            print('  '.join(line))

        print('Horizontal Flips')
        for line in zip(hflip_inital, hflip_1):
            print('  '.join(line))
           
        print('Vertical Flips')
        for line in zip(vflip_inital, vflip_1):
            print('  '.join(line))

def print_panorama(images, image_order):
    for row in image_order:
        ascii_images = map(get_ascii_image, map(lambda i: images[i], row))
        print('')
        for imgs in zip(*ascii_images):
            print(' '.join(imgs))
            
def from_ascii(ascii):
    result = []

    for line in ascii:
        result_line = []
        for c in line:
            if c == '#':
                result_line.append(1)
            else:
                result_line.append(0)
        result.append(result_line)
        
    return result

def tiles_fit(tile_a, tile_b):
    # looks bad but is constant in n... 8 orientations for 4 edges ... 16 checks at most for one tile
    for orientation_a in tile_a:
        for edge_a in orientation_a:
            for orentation_b in tile_b:
                for edge_b in orentation_b:
                    if edge_a == edge_b:
                        return True

    return False

def get_fitting_tiles(edges):
    fitting_tiles = {}
    edge_list = list(edges.items())

    for i in range(len(edge_list)):
        for j in range(i + 1, len(edge_list)):
            (tile_a_id, tile_a), (tile_b_id, tile_b) = edge_list[i], edge_list[j]

            if tiles_fit(tile_a, tile_b):
                if tile_a_id in fitting_tiles:
                    fitting_tiles[tile_a_id].append(tile_b_id)
                else:
                    fitting_tiles[tile_a_id] = [tile_b_id]
                
                if tile_b_id in fitting_tiles:
                    fitting_tiles[tile_b_id].append(tile_a_id)
                else:
                    fitting_tiles[tile_b_id] = [tile_a_id]

    return fitting_tiles

def get_corner(tiles):
    # get a corner in the tile DS 
    for tile, adjacent in tiles.items():
        if len(adjacent) == 2:
            return tile
    return None

def assemble(fitting_tiles, size):
    tiles = dict(fitting_tiles) # local copy
    result = np.zeros((size, size), dtype=int)
    
    previous = None

    for y in range(size):
        for x in range(size):
            if not previous:
                result[y][x] = get_corner(tiles)
            else:
                if y > 0:
                    next = [tile for tile in tiles[previous] if tile not in result[y] and tile in fitting_tiles[result[y - 1][x]]]
                else:
                    next = [tile for tile in tiles[previous] if len(tiles[tile]) != 4 and tile not in result[y]]
                
                result[y][x] = next[0]
            
            previous = result[y][x]

        # update tiles
        tiles = {t: [t for t in ts if t not in result[y]] for t, ts in tiles.items() if t not in result[y][1:]}
        # set previous
        previous = result[y][0]
             
    return result

def tile_orientation(edges, center, top=None, right=None, bot=None, left=None, cutoff=None):
    result = []

    for i, tile_o in enumerate(edges[center]):
        center_top, center_right, center_bot, center_left = tile_o
        for j, top_o in enumerate(edges[top] if top is not None else [(0, 0, center_top, 0)]):
            _, _, top_bot, _ = top_o
            for k, right_o in enumerate(edges[right] if right is not None else [(0, 0, 0, center_right)]):
                _, _, _, right_left = right_o
                for l, bot_o in enumerate(edges[bot] if bot is not None else [(center_top, 0, 0, 0)]):
                    bot_top, _, _, _ = bot_o
                    for m, left_o in enumerate(edges[left] if left is not None else [(0, center_left, 0, 0)]):
                        _, left_right, _, _ = left_o

                        if center_top == top_bot and center_right == right_left and center_bot == bot_top and center_left == left_right:
                            result.append((i, j, k, l, m))

                        if cutoff and len(result) >= cutoff:
                            return result       

    return result

def reorientate(tile, orientation):
    if orientation == 1:
        return np.fliplr(tile)
    elif orientation == 2:
        return np.flipud(tile)
    elif orientation == 3:
        return np.rot90(tile, k=1, axes=(1,0))
    elif orientation == 4:
        rotated = np.rot90(tile, axes=(1,0))
        return np.fliplr(rotated)
    elif orientation == 5:
        rotated = np.rot90(tile, axes=(1,0))
        return np.flipud(rotated)
    elif orientation == 6:
        return np.rot90(tile, k=2, axes=(1,0))
    elif orientation == 7:
        return np.rot90(tile, k=3, axes=(1,0))
    else:
        return np.array(tile)

def orientate(images, edges, order):
    result = {}

    first_tile = order[0][0]
    orientation, *_ = tile_orientation(edges, center=first_tile, right=order[0][1], bot=order[1][0], cutoff=1)[0]
    orientation_edge = edges[first_tile][orientation]
    _, previous_right, previous_bot, _ = orientation_edge

    for y, row in enumerate(order):
        if y > 0:
            for o, tile_o in enumerate(edges[order[y][0]]):
                current_top, current_right, current_bot, _ = tile_o
                if current_top == previous_bot:
                    orientation = o
                    previous_bot = current_bot
                    previous_right = current_right
                    break

        for x, tile in enumerate(row):
            if x > 0:
                for o, tile_o in enumerate(edges[tile]):
                    _, current_right, _, current_left = tile_o
                    if current_left == previous_right:
                        orientation = o
                        previous_right = current_right
                        break

            result[tile] = reorientate(images[tile], orientation)

    return result

def stich(images, order):
    image = []

    for row in order:
        image_row = list(map(lambda id: images[id][1:-1, 1:-1], row))
        image_row = np.hstack(image_row)

        if len(image) < 1:
            image = image_row
        else:
            image = np.vstack((image, image_row))
            
    return image

def match(image, pattern):
    pattern_width, pattern_height = len(pattern[0]), len(pattern)
    result = 0

    relevant_indices = []
    for y, row in enumerate(pattern):
        for x, element in enumerate(row):
            if element == 1:
                relevant_indices.append((x, y))


    for y in range(len(image) - pattern_height):
        for x in range(len(image[y]) - pattern_width):
            matches = 0

            for idx_x, idx_y in relevant_indices:
                if image[y + idx_y][x + idx_x]:
                    matches += 1

            if matches == len(relevant_indices):
                result += 1

    return result

def find_sea_monsters(image, pattern):
    for i in range(8):
        reorientated_image = reorientate(image, i)
        result = match(reorientated_image, pattern)

        if result != 0:
            return result

    return 0    

def part_one(input):
    _, edges = parse_input(input)

    fitting_tiles = get_fitting_tiles(edges)

    corner_pieces = list(map(lambda ft: ft[0], filter(lambda ft: len(ft[1]) == 2, fitting_tiles.items())))

    print('Corners: {}'.format(' '.join(map(str, corner_pieces))))
    return reduce(lambda x, y: x * y, corner_pieces)


def part_two(input):
    images, edges = parse_input(input)
    pattern = from_ascii([
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '])
    
    fitting_tiles = get_fitting_tiles(edges)

    image_order = assemble(fitting_tiles, int(math.sqrt(len(images))))

    images = orientate(images, edges, image_order)

    image = stich(images, image_order)

    match_count = find_sea_monsters(image, pattern)

    pattern_count = sum(map(lambda l: collections.Counter(l)[1], pattern))

    image_count = sum(map(lambda l: collections.Counter(l)[1], image))

    return image_count - (match_count * pattern_count)


def main():
    print('Day 20: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day20.txt', '\n'))))
    print('Day 20: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day20.txt', '\n'))))


if __name__ == "__main__":
    main()
