class read():
    def __init__(self):
        self.content = self.read_lines()
        for i in range(0,len(self.content)):
            for j in range(0,len(self.content[0])):
                self.content[i][j] = int(self.content[i][j])
        self.ans = [[0,0],[0,1],[0,2],[0,3], 0]

    def read_lines(self):
        hold = []
        with open("grid.txt") as f:
            content = f.readlines()
        for lines in content:
            hold.append(lines.strip("\n").split(" "))
        return hold

    def horizontal_vert_diag(self):
        for i in range(0, len(self.content)):
            for j in range(0,len(self.content[0])):
                #horizontal
                if j < len(self.content[0]) - 3:
                    pos_ans = self.content[i][j] * self.content[i][j+1] * self.content[i][j+2] * self.content[i][j+3]
                    if pos_ans > self.ans[4]:
                        self.ans = [[i,j],[i,j+1],[i,j+2],[i,j+3],pos_ans]
                #vertical
                if i < len(self.content) - 3:
                    pos_ans = self.content[i][j] * self.content[i+1][j] * self.content[i+2][j] * self.content[i+3][j]
                    if pos_ans > self.ans[4]:
                        self.ans = [[i, j], [i+1, j], [i+2, j], [i+3, j], pos_ans]
                #diagonal to the right
                if (j < len(self.content[0])-3) and ( i < len(self.content) -3):
                    pos_ans = self.content[i][j] * self.content[i+1][j+1] * self.content[i+2][j+2] * self.content[i+3][j+3]
                    if pos_ans > self.ans[4]:
                        self.ans = [[i, j], [i+1, j+1], [i+2, j+2], [i+3, j+3], pos_ans]
                #diagonal to the left
                if (j > 2) and (i < len(self.content) - 3):
                    pos_ans = self.content[i][j] * self.content[i + 1][j - 1] * self.content[i + 2][j - 2] * self.content[i + 3][j - 3]
                    if pos_ans > self.ans[4]:
                        self.ans = [[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3], pos_ans]

def main():
    x = read()
    x.horizontal_vert_diag()
    print(x.ans)

main()