def tiles(number: int):
    if number == 0:
        return [""]
    if number == 1:
        return[' ⏹️']
    return [' ⏹️' + t for t in tiles(number-1)] + [' ||' + t for t in tiles(number-2)]


if __name__ == '__main__':
    print(tiles(3))
