from common.util import read_input


def count(space_image, width, height, layer, what):
    image_size = width * height

    if image_size * layer >= len(space_image):
        return -1

    return space_image[image_size * layer:image_size * layer + image_size].count(what)


def calculate_checksum(space_image, width, height):
    image_size = width * height

    min_zeros, min_zeros_layer = count(space_image, width, height, 0, 0), 0

    if len(space_image) > image_size:
        for layer in range(1, int(len(space_image) / image_size)):
            zeros = count(space_image, width, height, layer, 0)

            if zeros < min_zeros:
                min_zeros, min_zeros_layer = zeros, layer

    ones = count(space_image, width, height, min_zeros_layer, 1)
    twos = count(space_image, width, height, min_zeros_layer, 2)

    return ones * twos


def get_pixel_color(space_image, width, height, index):
    image_size = width * height

    for layer in range(int(len(space_image) / image_size)):
        pixel = space_image[image_size * layer:image_size * layer + image_size][index]
        if pixel != 2:
            return pixel

    return 2


def decode_image(space_image, width, height):
    image = []
    for index in range(width * height):
        image.append(get_pixel_color(space_image, width, height, index))

    return image


def print_image(image, width, height):
    for row in range(height):
        print('{}'.format(''.join(map(str, image[width * row: (width * row) + width])).replace('0', ' ')))


def main():
    image_data = list(map(int, read_input()))
    image_width, image_height = 25, 6
    print('Answer for Day7 - Part 1: {}'.format(calculate_checksum(image_data, image_width, image_height)))
    print('Answer for Day7 - Part 2')
    print_image(decode_image(image_data, image_width, image_height), image_width, image_height)


if __name__ == "__main__":
    main()
