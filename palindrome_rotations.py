def pr(string):
    success = 0
    for i in range(0, len(string)):
        result = string[i:] + string[0:i]
        if result == result[::-1]:
            success += 1
            print(result)
    if success is 0:
        print('NONE')


def main():
    pr('akawwaka')


if __name__ == '__main__':
    main()
