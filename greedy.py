# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: Greedy
# Authors: Zachary Yamaoka (18th October 2017)
# Last updated: 13th September 2017
# ####################################################

import numpy as np

def greedy_search(game):

    start_state = game.getStartState_()
    game.clearSolution()

    if start_state == None:
        return None

    game.updateBoard(start_state)
    game.updateSolution(start_state)
    next_states = []

    for state in game.getSuccessors(start_state):
        next_states.append(state)

    for i in range(3):
        successor_values = []
        caches = []

        if len(next_states) == 0:
           break

        for action_state in next_states:
            value = game.estimateValue(action_state, i)
            successor_values.append(value)
            if value <= -800:
                break

        index = np.argmin(successor_values)
        action = next_states.pop(index)

        game.updateBoard(action)
        game.updateSolution(action)

        for state in game.getSuccessors(action):
            if state not in next_states:
                next_states.append(state)
