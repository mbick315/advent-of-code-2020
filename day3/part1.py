def build_matrix():
    matrix = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            line_matrix = []
            for char in line:
                if char in ['.', '#']:
                    line_matrix.append(char)
            matrix.append(line_matrix)
    return matrix

def calculatex(currentx, x_forward, length_row):
    return (currentx + x_forward) % length_row

def find_trees(x_forward, y_forward):
    matrix = build_matrix()
    length_column = len(matrix)
    length_row = len(matrix[0])
    currentx = 0
    currenty = 0
    num_trees = 0
    while currenty < length_column:
        if matrix[currenty][currentx] == '#':
            num_trees += 1
        currenty += y_forward
        currentx = calculatex(currentx, x_forward, length_row)
    return num_trees

num_trees = find_trees(3, 1)
print('Num Trees: {}'.format(num_trees))

multiply_trees = find_trees(1, 1) * find_trees(3, 1) * find_trees(5, 1) * find_trees(7, 1) * find_trees(1, 2)
print('Multiply all slopes {}'.format(multiply_trees))