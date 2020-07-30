import os
import sys

def main():
    for i, old_filepath in enumerate(sys.argv):
        if i != 0:
            print('old_filepath =', old_filepath)
            directory = old_filepath[: old_filepath.rfind('\\')+1]
            filename = old_filepath[len(directory): ]
            print('filename =', filename)
            first = filename[: filename.find('_')]
            second = filename[len(first)+1: ]
            if '(' in second:
                third = second[second.find('('): ]
                second = second[: second.find('(')]
                last = third[third.find('.'): ]
                third = third[: third.find('.')]
            else:
                third = ''
                last = second[second.find('.'): ]
                second = second[: second.find('.')]
            new_filepath = directory + second + '_' + first + third + last
            print(first, second, third, last)
            print('new_filepath =', new_filepath)
            os.rename(src=old_filepath, dst=new_filepath)

if __name__ == '__main__':
    main()
