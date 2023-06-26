
from game.go import Model
WHITE=False

def get_liberty(x,y,model:Model):
    lis=[]
    for (u, v) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if u < 0 or v < 0 or u >= model.size or v >= model.size:
            continue
        if model.board[u][v] is None:
            lis.append((u,v))
    return lis


def oppo_libert(k,z,model):
    lis=[]
    lis2=[]
    for x in range(19):
        for y in range(19):
            if model.board[x][y] is  None:
                continue
            if model.board[x][y].color==WHITE:
                  lis.append((x,y))
    for point in lis:
        for (u, v) in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1]+ 1)]:
            if u < 0 or v < 0 or u >= model.size or v >= model.size:
                continue
            if model.board[u][v] is None:
                lis2.append((u,v))

    if (k,z) in lis2:
        return True


def check_edge(x,y,model:Model):
    lsit_up=[]
    lsit_do = []
    lsit_le = []
    lsit_rig = []
    empty=[]
    for j in range(19):
        lsit_up.append((0, j))
    for j in range(19):
         lsit_do.append((18,j))
    for j in range(19):
         lsit_rig.append((j,18))
    for j in range(19):
         lsit_le.append((j,0))
    if (x,y) in lsit_do or lsit_up or lsit_rig or lsit_le:
        for (u, v) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if u < 0 or v < 0 or u >= model.size or v >= model.size:
                continue
            if model.board[u][v] is not None and model.turn!=model.board[u][v].color:
                empty.append((u,v))
        if len(empty)>=2:
            return True
        else:
            return False
    else:
        return False


def in_board(x,y,model:Model):
    if not check_edge(x,y,model) :
        return True



def get_color(color):
    if  color:
        return "Black"
    else:
        return "White"

def get_groups(model:Model):
    lis=[]
    for i in range(19):
        for j in range(19):
            if model.board[i][j] is not None:
                lis.append(model.board[i][j])

    return lis


def danger_self(x,y,model:Model):
    lis=[]
    if get_groups(model):
        grb=get_groups(model)
        for groub in grb :
            for point in groub.stones:
                if model.board[point[0]][point[1]].color == model.turn:
                    lis.append(groub)
        if not lis:
            return False
        else:
            for groubs in lis:
                 for point in groubs.stones:
                    #print(point)
                    if len(get_liberty(point[0],point[1],model))==1 or len(get_liberty(point[0],point[1],model))==0 or \
                            len(get_liberty(point[0],point[1],model))==2:
                        if (x,y) in get_liberty(point[0],point[1],model):
                            return True


    else:
        return False


def corner(x,y):
    if (x,y) in [(0,0),(0,18),(18,18),(18,0)]:
        return True


def counter_stone(model:Model):
    lis=[]
    for i in range(19):
        for j in range(19):
            if model.board[i][j] is not None:
                lis.append((i,j))
    return len(lis)


def oppo_danger(x,y,model:Model):
    lis=[]
    if get_groups(model) :
        grb=get_groups(model)
        for groubs in grb:
            color = get_color(groubs.color)
            if color != get_color(model.turn):
                lis.append(groubs)
        if not lis:
            return False
        else:
            for groubs in lis:
                for point in groubs.stones:
                    if len(get_liberty(point[0],point[1],model))==1 or len(get_liberty(point[0],point[1],model))==2 or\
                            len(get_liberty(point[0],point[1],model))==0:
                        if (x, y) in get_liberty(point[0],point[1],model):
                            return True
    else:
        return False