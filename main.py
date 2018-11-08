# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN FILE EXAMPLEb
# Authors: Liuqing Chen, Feng Shi,
#          and Isaac Engel (13th September 2017)
# Last updated: 13th September 2017
# ####################################################

# Write or import your functions in this file
import numpy as np
from greedy import greedy_search
from gamemanager import GameManager
from utils import *
import time
# import matplotlib.pyplot as plt

def Tetris(target):
    gameboard = np.array(target)
    game = GameManager(gameboard)
#
# # Viz Stuff
#     # wrong_list = checkshape(solution)
#     Ty_len = len(target)
#     Tx_len = len(target[0])
#     Sy_len = len(target)
#     Sx_len = len(target[0])
#
#     fig, (ax1, ax2) = plt.subplots(1, 2)  # Create figure and axes
#     im = Image.new('RGB', (Tx_len, Ty_len), (255, 255, 255))  # white background-image
#     dr = ImageDraw.Draw(im)
#     ax1.imshow(im)  # Display the background-image
#     ax2.imshow(im)
#
#     # -------------------- Target Display ----------------------
#     for y in range(Ty_len):
#         row = target[y]
#         for x in range(Tx_len):
#             if row[x] == 1:
#                 ax1.add_patch(patches.Rectangle((x, y), 0.88, 0.88, color='b'))  # draw a block
#     ax1.set_title('The Display of Task')
#     ax1.set_xlim([-1, Tx_len + 1])
#     ax1.set_ylim([-1, Ty_len + 1])
#     ax1.invert_yaxis()
#
#     ax2.set_title('The Display of Solutioin')
#     ax2.set_xlim([-1, Sx_len + 1])
#     ax2.set_ylim([-1, Sy_len + 1])
#     ax2.invert_yaxis()
#
#     # plt.draw()
#     # plt.pause(5)
#     plt.draw()
#     plt.pause(10)
    while not game.done():
        greedy_search(game)
    #
    #     solution = game.getSolution()
    #     # --------------- Solution Display ----------------------
    #     def get_color(num):  # generate a random color
    #         np.random.seed(num)
    #         c = list(np.random.rand(3))
    #         c.append(1.0)
    #         return tuple(c)
    #
    #     wrong_label_count = {}
    #     for y in range(Sy_len):
    #         row = solution[y]
    #         for x in range(Sx_len):
    #             shape, num = row[x]
    #             if shape != 0:
    #                 ax2.add_patch(patches.Rectangle((x, y), 0.88, 0.88, color=get_color(num)))  # draw a block
    #                 # if num in wrong_list:
    #                 #     if wrong_label_count.setdefault(num, 0) == 0:
    #                 #         ax2.text(x, y + 0.8, '{}'.format(num))  # add label to blocks that have wrong shapes
    #                 #         wrong_label_count[num] += 1
    #     plt.draw()
    #     plt.pause(0.01)
    #
    # valid, missing, excess, error_pieces = check_solution(target, game.getSolution())
    #
    # total_blocks = sum([sum(row) for row in target])
    # total_blocks_solution = total_blocks - missing + excess
    #
    # s1 = "The number of blocks in the TARGET is {:.0f}.".format(total_blocks)
    # s2 = "The number of blocks in the SOLUTION is {:.0f}.".format(total_blocks_solution)
    # s3 = "There are {} MISSING blocks ({:.4f}%) and {} EXCESS blocks ({:.4f}%).\n".format \
    #       (missing, 100 * missing / total_blocks, excess, 100 * excess / total_blocks)
    #
    # ax2.annotate(s1, (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
    # ax2.annotate(s2, (0,0), (0, -30), xycoords='axes fraction', textcoords='offset points', va='top')
    # ax2.annotate(s3, (0,0), (0, -40), xycoords='axes fraction', textcoords='offset points', va='top')
    #
    # plt.draw()
    # plt.pause(10)
    return game.getSolution()




def liveViz(target, solution):
    """
    Displays the target vs the solution
    :param target: target shape
    :param solution: student's solution
    """
    print("working")

    wrong_list = checkshape(solution)
    Ty_len = len(target)
    Tx_len = len(target[0])
    Sy_len = len(solution)
    Sx_len = len(solution[0])

    fig, (ax1, ax2) = plt.subplots(1, 2)  # Create figure and axes
    im = Image.new('RGB', (Tx_len, Ty_len), (255, 255, 255))  # white background-image
    dr = ImageDraw.Draw(im)
    ax1.imshow(im)  # Display the background-image
    ax2.imshow(im)

    # -------------------- Target Display ----------------------
    for y in range(Ty_len):
        row = target[y]
        for x in range(Tx_len):
            if row[x] == 1:
                ax1.add_patch(patches.Rectangle((x, y), 0.88, 0.88, color='b'))  # draw a block
    ax1.set_title('The Display of Task')
    ax1.set_xlim([-1, Tx_len + 1])
    ax1.set_ylim([-1, Ty_len + 1])
    ax1.invert_yaxis()

    # # --------------- Solution Display ----------------------
    # def get_color(num):  # generate a random color
    #     np.random.seed(num)
    #     c = list(np.random.rand(3))
    #     c.append(1.0)
    #     return tuple(c)
    #
    # wrong_label_count = {}
    # for y in range(Sy_len):
    #     row = solution[y]
    #     for x in range(Sx_len):
    #         shape, num = row[x]
    #         if shape != 0:
    #             ax2.add_patch(patches.Rectangle((x, y), 0.88, 0.88, color=get_color(num)))  # draw a block
    #             if num in wrong_list:
    #                 if wrong_label_count.setdefault(num, 0) == 0:
    #                     ax2.text(x, y + 0.8, '{}'.format(num))  # add label to blocks that have wrong shapes
    #                     wrong_label_count[num] += 1


    ax2.set_title('The Display of Solutioin')
    ax2.set_xlim([-1, Sx_len + 1])
    ax2.set_ylim([-1, Sy_len + 1])
    ax2.invert_yaxis()
    plt.show() # draw the plot
    secs = 0.1
    plt.draw()
    plt.pause(5)
    # time.sleep(secs)
    plt.clf()
