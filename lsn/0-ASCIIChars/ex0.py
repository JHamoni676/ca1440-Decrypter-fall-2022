def displayASCII():
    # TODO: Display all printable ASCII characters in the range [32, 126].
    for i in range(32, 126):
        character = chr(i)
        print(character)
    pass

if __name__ == '__main__':
    displayASCII()
