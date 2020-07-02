from .base import BaseEncoder

'''
This is an origin file format of our program
its a txt file in fact, for example

"little star.txt"

1 1 5 5 6
6 5
4 4 3 3 2 2 1
5 5 4 4 3 3 2
=71 2 3 4 5 67#1
'''
class originEncoder(BaseEncoder):
    def readfile(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            text = "".join(lines)
            text = text.replace("\n"," ")
            text = text.replace("\r"," ")
            text = text.strip()
        return text

    # Input as "#1 123 2"
    # Output as [["#1"], ["1","2","3"], ["2"]]
    def process(self, text):
        results = []

        lines = text.split(" ")
        for line in lines:
            result = []
            current_char = '0'
            current_prefix = ''
            for index in range(len(line)):
                if line[index] == '-':
                   result.append(current_char) 
    
                elif line[index] == '=':
                    # the =- is not allowed
                    current_char = '0'
                    current_prefix = '='
                    
                elif line[index] == '#':
                    current_char = '0'
                    current_prefix = '#'
    
                elif line[index].isdigit():
                    current_char = current_prefix + line[index]
                    result.append(current_char)
                    current_prefix = ''
    
                else:
                    print("[Warning] Unexpected Char In Your File")
                    print("[Warning] Ignore It : {}".format(line[index]))
                    continue
            results.append(result)

        return results
