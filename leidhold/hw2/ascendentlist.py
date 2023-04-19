#import mysqrt_withouttemplate
def ascendentsortedlist(list):
    i = len(list)-1
    while i >= 0:
        j = len(list)-1
        while j >= 0:
            if list[i] > list[j]:
                w = list[i]
                list[i] = list[j]
                list[j] = w
            j -= 1
        i -= 1
    return list

def main():
    list = ascendentsortedlist([4, 5, 7, 2, 3, 1, 1, 9, 5, 3, 1, 3, 2, 7, 5, 34, 8, 5])
    print(f'The ascendent sorted list is {list}')

    #mysqrt = mysqrt_withouttemplate.sqrt(5)


if __name__ == '__main__':
    main()


