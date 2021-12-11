
def read_input(filename='input', separator=''):
    with open(filename, 'r') as f:
        contents = f.read()

    if len(separator) > 0:
        contents = contents.split(separator)
        return contents[:-1] if not contents[-1] else contents

    return contents