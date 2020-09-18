import os
import sys

kugiri_list = ['_', ' ']

def kugiriCheck(filename):
    for kugiri in kugiri_list:
        if kugiri in filename:
            return kugiri
    return 0

def main():
    for i, old_filepath in enumerate(sys.argv):
        if i != 0:

            print('old_filepath =', old_filepath)
            directory = old_filepath[: old_filepath.rfind('\\')+1]
            filename = old_filepath[len(directory): ]
            kugiri = kugiriCheck(filename)
            if not kugiri:
                continue
            print('filename =', filename)
            first = filename[: filename.find(kugiri)]
            second = filename[len(first)+1: ]
            if '(' in second:
                third = second[second.find('('): ]
                second = second[: second.find('(')]
                last = third[third.find('.'): ]
                third = third[: third.find('.')]
            else:
                third = ''
                last = ''
                if second.find('.') != -1:
                    last = second[second.find('.'): ]
                    second = second[: second.find('.')]
            new_filepath = directory + second + kugiri + first + third + last
            print(f'{first}-{second}-{third}-{last}')
            print('new_filepath =', new_filepath)
            os.rename(src=old_filepath, dst=new_filepath)

if __name__ == '__main__':
    main()
