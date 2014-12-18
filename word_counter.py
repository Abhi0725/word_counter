#-------------------------------------------------------------------------------
# Name:        word_counter
# Purpose:     This programme takes a file name as input and gives the numbe
#              times that word occured in that file.
# Author:      Abhishek Chakravarty
#
# Created:     18-12-2014
#-------------------------------------------------------------------------------

def main():
    f = raw_input("enter the file name: ")
    word = raw_input("enter the word: ")
    f = open(f)
    count = 0
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        else:
            line = line.split()
            for w in line:
                if w == word:
                    count +=1
    return count
if __name__ == '__main__':
    count = main()
    print count
