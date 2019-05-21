
board = [[2, 2, 0], [1, 0, 2], [1, 1, 0]]

def validate_board(board):
   count_1=0
   count_2=0
   lines = 3
   rows = 3
   if len(board)!=lines:
       return False
   for line in board:
       if line.count(0)+line.count(1)+line.count(2)!=len(line):
           return False
       if rows != len(line):
           return False

       count_1+=line.count(1)
       count_2+=line.count(2)

   if count_1-count_2 == 0:
       return True
   elif count_1-count_2 == 1:
       return True
   else:
       return False

def check_lines(board):  #done
    result =[]
    for line in (board):
        if len(line)==line.count(line[0]) and line[0]!=0: #если в строке все цифры = первой, и это не ноль - строка выйгрышная, возвращаем выйгрышную цифру
            result.append(line[0])
    return result


def check_rows(board): #done
    result = []
    for n_row in range(0,len(board[0])):
        row = []
        for line in range(0,len(board)):
            row.append(board[line][n_row]) #транспонируем колонку в строку
        if len(row) == row.count(row[0]) and row[0]!=0:
            result.append(board[0][n_row])
    return result


def check_cross(board):
    result =[]
    line1=[]
    line2 = []
    length = len(board)
    for i in range (0,length):
        line1.append(board[i][i])
        line2.append(board[length-1-i][i])
    if len(line1)==line1.count(line1[0]) and line1[0]!= 0:
        result.append(line1[0])
    if len(line2)==line2.count(line2[0]) and line1[0]!= 0:
        result.append(line2[0])
    return result


def game_finished(board):
    if not validate_board(board):
        return -1
    result =[]
    check_0=0
    result.append(check_lines(board))
    result.append(check_rows(board))
    result.append(check_cross(board))

    for check in result:
        if len(check)>1:
            return -1

    for check in result:
        if len(check)>0:
            return check[0]

    for check in board:
        check_0+=check.count(0)
    if check_0>0:
        return 0
    else:
        return -1
    return -1
def render_board(board):
    '''рисует доску
    '''
    result = '<table>'
    for line in board:
        result+="<tr>"
        for key in line:
            if key == 1:
                result+="<td>"+"X"+"</td>"
            elif key ==2 :
                result+="<td>"+"O"+"</td>"
            else:
                result+="<td>"+"&nbsp;"+"</td>"
        result+="</tr>"
    result+="</table>"
    return result
#print (type(validate_board(board)))
