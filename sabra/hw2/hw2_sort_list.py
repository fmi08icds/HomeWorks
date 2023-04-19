from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

def sort_values(numbers):
    sorted_list = sorted(numbers)
    return sorted_list

def main() :
    try:
        parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
        parser.add_argument('--numbers', type=int, nargs='+', help="A list of integers that should be sorted!")
        args = parser.parse_args()
        numbers = args.numbers
        print("You entered the list {} ".format(numbers))
        sorted_list = sort_values(numbers)
        print("The sorted list is {} ".format(sorted_list))
    except:
        print("Either you did not enter anything or the list do not contain all integers!")

if __name__ == '__main__':
    main()








