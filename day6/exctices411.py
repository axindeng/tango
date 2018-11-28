'''
假定有一个列表的列表，内层列表的每个值都是包含一个字符的字符串，像这样： 
 
grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']] 
 
你可以认为grid[x][y]是一幅“图”在x、y坐标处的字符，该图由文本字符组
成。原点(0, 0)在左上角，向右x坐标增加，向下y坐标增加。 
复制前面的网格值，编写代码用它打印出图像。


你需要使用循环嵌套循环，打印出grid[0][0]，然后grid[1][0]，然后grid[2][0]，以此
类推，直到grid[8][0]。这就完成第一行，所以接下来打印换行。然后程序将打印出
grid[0][1]，然后grid[1][1]，然后grid[2][1]，以此类推。程序最后将打印出grid[8][5]。
'''


grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]
len_col=len(grid[0])
len_list=len(grid)

for y in range(len_col):
    for x in range(len_list):
        print(grid[x][y],end='')
    print()