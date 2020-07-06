from .base import BaseDisplayer

class cmdPlayer(BaseDisplayer):
    def display(self, data, output_filename):
        output_filename = "./output/" + output_filename
        with open(output_filename, "w", encoding='utf-8') as f:
            for t in data:
                string = self.displaySingle(t)
                f.write(string)


    def displaySingle(self,coords):
        split_row = "-" * 21
        data_row = [list("|   |   |   |   |   |"),list("|   |   |   |   |   |"),list("|   |   |   |   |   |")]
        
        for coord in coords:
            if(coord == (-1,-1)):
                pass
            else:
                x = coord[0]
                y = coord[1]
                data_row[x][2 + y * 4] = '*'
    
        for i in range(len(data_row)):
            data_row[i] = "".join(data_row[i])

        empty = "                         \n\n"
        print(split_row)
        print(data_row[0])
        print(split_row)
        print(data_row[1])
        print(split_row)
        print(data_row[2])
        print(split_row)
        print(empty)

        total = split_row + '\n' + data_row[0] + '\n' + \
                split_row + '\n' + data_row[1] + '\n '+ \
                split_row + '\n' + data_row[2] + '\n '+ \
                split_row + '\n' + empty

        return total

