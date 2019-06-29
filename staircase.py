if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    test_length = int(input())
    first_three = [1, 2, 4, 0]
    for x in range(test_length):
        stairs = int(input())
        for i in range(3, stairs + 1):
            first_three.append(0)
            first_three[i] = first_three[i - 1] + first_three[i - 2] + first_three[i - 3]
    #     fptr.write(str(a[n - 1]) + '\n')
    #
    # fptr.close()
        print(str(first_three[stairs - 1]) + '\n')
