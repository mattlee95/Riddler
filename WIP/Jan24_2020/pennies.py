



class Node:

    def __init__(self, level_in, start_state):
        self.init_state = start_state
        self.level = level_in
        self.perm = list()


    def my_move():

        results = list()

        if "W" in self.perm:
            return True

        for p in self.perm:
            results.append(p.opp_move())

        if False in results:
            return False

        return True


    def opp_move():

        results = list()

        if "W" in self.perm:
            return False

        for p in self.perm:
            results.append(p.my_move())

        if True in results:
            return True

        return False


















'''
Permutation Factors

    - Number of Pennies

    - Initial Distribution of Pennies

    - 




perm_list = []

format of elements in perm list [numLeft, numRight]

'''


perm_list = []
perm_list_holder = []


def opponent_turn():
    global perm_list
    global perm_list_holder

    for perm in perm_list:

        opp_win = False
        holder_additions = list()

        # All possibilities for taking from one list (left)
        for i in range(1, perm[0]+1):
            new_perm = list(perm)
            new_perm[0] = perm[0] - i
            holder_additions.append(new_perm)

            if sum(perm) == 0:
                opp_win = True

        # All possibilities for taking from one list (right)
        for i in range(1, perm[1]+1):
            new_perm = list(perm)
            new_perm[1] = perm[1] - i
            holder_additions.append(new_perm)

            if sum(perm) == 0:
                opp_win = True

        # All possibilities for taking from both lists
        for i in range(1, min(perm)+1):
            new_perm = list(perm)
            new_perm[0] = perm[0] - i
            new_perm[1] = perm[1] - i
            holder_additions.append(new_perm)

            if sum(perm) == 0:
                opp_win = True

        if not opp_win:
            for elem in holder_additions:
                perm_list_holder.append(elem)


def my_turn():
    global perm_list
    global perm_list_holder

    for perm in perm_list:

        holder_additions = list()

        # All possibilities for taking from one list (left)
        for i in range(1, perm[0]+1):
            new_perm = list(perm)
            new_perm[0] = perm[0] - i
            holder_additions.append(new_perm)

            if sum(perm) == 0:
                return True

        # All possibilities for taking from one list (right)
        for i in range(1, perm[1]+1):
            new_perm = list(perm)
            new_perm[1] = perm[1] - i
            holder_additions.append(new_perm)

            if sum(perm) == 0:
                return True

        # All possibilities for taking from both lists
        for i in range(1, min(perm)+1):
            new_perm = list(perm)
            new_perm[0] = perm[0] - i
            new_perm[1] = perm[1] - i
            holder_additions.append(new_perm)

            if sum(perm) == 0:
                return True

        for elem in holder_additions:
            perm_list_holder.append(elem)



def test_dist():






def test_all_divisions(num_pennies):
    global perm_list

    for i in range((num_pennies+1)/2):

        perm_list = list()
        perm_list.append([i, num_pennies-i])

        test_dist()







