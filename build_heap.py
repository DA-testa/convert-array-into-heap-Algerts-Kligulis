# python3
import math


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    for a in range(len(data),0,-1):
        i = a
        while i > 1:
            j = i//2
            if data[i-1]<data[j-1]:
                data[i-1], data[j-1] = data[j-1], data[i-1]
                swaps.append([j-1,i-1])
                i = j
            else:
                i=0
    return swaps


def main():
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    choice = input()

    if 'I'in(choice):
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    else:
        with open(input()) as fails:
            n = int(fails.readline())
            data = list(map(int, fails.readline().split()))
        # file = input()
        # n = file[0]
        # data = list(map(int, file[1].split()))
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
