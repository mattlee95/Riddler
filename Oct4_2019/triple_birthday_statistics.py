
'''
Structure of Node using to calculate permutations

[int number_of_2_bdays, int number_of_1_bdays, int number_of_0_bdays, float P(likelyhood_of_permuation)]
'''

tree_level = []
tree_level_holder = []


def init_tree():
    global tree_level
    global tree_level_holder

    tree_level_holder = list()
    tree_level = list()
    
    beginning_node = list([0, 0, 365, float(1)])

    tree_level.append(beginning_node)



def permutate_next_level():
    global tree_level
    global tree_level_holder

    
    #Indexes for variables in each node
    BDAY0 = 2
    BDAY1 = 1
    BDAY2 = 0
    P_PERM = 3

    #Flout representing probability of having triple birthday for specified group size
    p_chance_of_triple = float(0)

    #Flag used to track whether specific permutation is represented in next level
    flag_reused = False

    for node in tree_level:
        
        '''
        Check for the possibility of a permutation for the case in which
        someone has a birthday on a day with current no other birthdays

        0 Birthday Day -> 1 Birthday Day
        '''
        if node[BDAY1] < 365 and node[BDAY0] > 0:

            flag_reused = False

            '''
            Check to see if this particular permutation already has
            a node on the next level if so add the probability to that
            node
            '''
            for next_node in tree_level_holder:
                if next_node[BDAY1] == node[BDAY1] + 1 and next_node[BDAY0] == node[BDAY0] - 1 and next_node[BDAY2] == node[BDAY2]:
                    next_node[P_PERM] += node[P_PERM] * (float(node[BDAY0]) / float(365))
                    flag_reused = True

            '''
            If permuation does not exist create a node of that permutation
            and add it to the next level
            '''
            if not flag_reused:
                new_node = list(node)

                new_node[P_PERM] = node[P_PERM] * (float(node[BDAY0]) / float(365))
                new_node[BDAY1] = node[BDAY1] + 1
                new_node[BDAY0] = node[BDAY0] - 1

                tree_level_holder.append(new_node)

        
        '''
        Check for the possibility of a permutation for the case in which
        someone has a birthday on a day that shares with one other person

        1 Birthday Day -> 2 Birthday Day
        '''
        if node[BDAY2] < 365 and node[BDAY1] > 0:

            flag_reused = False
 
            '''
            Check to see if this particular permutation already has
            a node on the next level if so add the probability to that
            node
            '''
            for next_node in tree_level_holder:
                if next_node[BDAY2] == node[BDAY2] + 1 and next_node[BDAY1] == node[BDAY1] - 1 and next_node[BDAY0] == node[BDAY0]:
                    next_node[P_PERM] += node[P_PERM] * (float(node[BDAY1]) / float(365))
                    flag_resused = True

            '''
            If permuation does not exist create a node of that permutation
            and add it to the next level
            '''
            if not flag_reused:
                new_node = list(node)
    
                new_node[P_PERM] = node[P_PERM] * (float(node[BDAY1]) / float(365))
                new_node[BDAY2] = node[BDAY2] + 1
                new_node[BDAY1] = node[BDAY1] - 1

                tree_level_holder.append(new_node)


        '''
        Check for the possibility of a permutation for the case in which
        someone has a birthday on a day that shares with two other people

        2 Birthday Day -> 3 Birthday Day
        '''
        if node[BDAY2] > 0:
            p_chance_of_triple += node[P_PERM] * (float(node[BDAY2]) / float(365))


    '''
    Switch the holder list to be the tree level list, clean up holder for next
    level of permuation calcs
    '''
    tree_level = list(tree_level_holder)
    tree_level_holder = []

    return p_chance_of_triple



def calc_bday_stats():

    SIMPLIFIED_PRINT = True

    running_prob = float(0)
    single_run_prob = float(0)


    init_tree()

    '''
    Maximum number of people should be 731, run that many cycles of permutations
    wherein we add a single person to the group each cycle
    '''
    for i in range(731):

        single_run_prob = permutate_next_level()
        running_prob += single_run_prob

        if SIMPLIFIED_PRINT:
            print "n = {0}, p(triple bday) = {1}".format(i+1, running_prob)
        else:
            print "For group of n = {0} probability of having triple birthday is: {1}\n\t{2} more than a group of n-1\n".format(i+1, running_prob, single_run_prob)



calc_bday_stats()






