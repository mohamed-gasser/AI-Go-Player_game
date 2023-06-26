from agent2.evaluation import eval
from game.go import Model
BLACK=True
WHITE=False


def minimax_alpa_beta(depth, maximizingPlayer,pos,alpha, beta, model: Model):
    if depth == 0 or model.game_over:
        return None,eval(model,pos)
    model.count+=1
    moves = model.get_moves()
    if maximizingPlayer:
        max_eval = float("-inf")
        max_score_actions = None
        for move in moves:
            actions,val = minimax_alpa_beta(depth - 1, False,move, alpha, beta, model)
            if max_eval < val:
                max_eval = val
                max_score_actions = move
            alpha = max(alpha, val)
            if beta <= alpha:
                break

        return max_score_actions,max_eval

    else:
        min_eval = float("inf")
        mini_score_action = None
        for move in moves:
            actions,val = minimax_alpa_beta(depth - 1, True,move, alpha, beta, model)
            if min_eval > val:
                min_eval = val
                mini_score_action = move
            beta = min(beta, val)
            if beta <= alpha:
                break
        return mini_score_action,min_eval
