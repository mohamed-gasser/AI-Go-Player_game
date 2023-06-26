from agent2.util import *
from game.go import Model
from numpy.random import normal
SCORE=100


def eval(model:Model,postion):
    x = postion[0]
    y = postion[1]
    score_l=0
    score_b=0
    score_w=0
    score_d=0
    score_s=0
    score_win = SCORE - model.count
    if model.ko == postion:
        return -score_win

    if corner(x,y):
        return -(score_win/2)
    if danger_self(x,y,model):
        score_s=20
    if oppo_danger(x,y,model): # in current move
        score_d= 10

    if check_edge(x,y,model):
        score_w= -50 # will loss in next

    if oppo_libert(x,y,model):#good probability to win 25%
        score_l=20
    if  in_board(x,y,model):
        score_b=10

    return (score_b+score_l+score_w+score_d+score_s)






