# Globals

# Initializing the 2 levels of the tree I will use to solve the permutations
lvl = list()
lvl_holder = list()

# Storing the probabilities in globals
p_dark = 0
p_milk = 0

class bag_state:
    '''
    This bag_state class is meant to just be a cleaner way of representing the
    state of one of these choclate bags. Attributes are as follows:
        dark: number of dark chocolates in bag
        milk: number of milk chocolates in bag
        last: thing consumed on last round ("milk", "dark", or None)
        prob: probability of this states occurance on this tree level
    '''
    def __init__(self, darks_i, milks_i, last_i, prob_i):
        self.dark = darks_i
        self.milk = milks_i
        self.last = last_i
        self.prob = prob_i

    '''
    Returns boolean on whether only 1 candy remains
    '''
    def last_choc_b(self):

        if self.dark + self.milk == 1:
            return True
        return False

    '''
    Returns type of remaining candy
    '''
    def last_choc_t(self):

        if self.dark != 0:
            return "dark"
        return "milk"

    '''
    Returns probability milk is picked
    '''
    def prob_milk(self):

        ret = self.milk / (self.milk + self.dark)
        return ret

    '''
    Returns probability dark is picked
    '''
    def prob_dark(self):

        ret = self.dark / (self.milk + self.dark)
        return ret

    '''
    Returns boolean for the eqivilency of both states.  Probability not
    accounted for since this is meant for collapsing the tree level into only
    single instances of each state
    '''
    def equals_b(self, bag):

        if (self.dark == bag.dark) and (self.milk == bag.milk) and (self.last == bag.last):
            return True
        return False


def init_level():
    '''
    Initializes the first level of the tree to begin
    '''
    global lvl

    lvl = [bag_state(8, 2, None, 1)]


def add_bag_to_holder(bag):
    '''
    Adds bag state to next level of tree, first searches for eqivalent state
    to add probability to rather than adding dupe states
    '''
    global lvl_holder

    for b in lvl_holder:
        if b.equals_b(bag):
            b.prob = b.prob + bag.prob
            return

    lvl_holder.append(bag)


def solve_bag_state(bag):
    '''
    Solves a bag state, adding probability if last candy or adding permutatins
    to next tree level
    '''
    global p_dark
    global p_milk

    # Last Piece
    if bag.last_choc_b():
        if bag.last_choc_t() == "dark":
            p_dark += bag.prob
        else:
            p_milk += bag.prob
        return

    # Milk
    prob_m = bag.prob_milk()
    if prob_m > 0:

        if bag.last != "dark":
            new_bag = bag_state(bag.dark, bag.milk-1, "milk", bag.prob*prob_m)
        else:
            new_bag = bag_state(bag.dark, bag.milk, None, bag.prob*prob_m)
        add_bag_to_holder(new_bag)

    # Dark
    prob_d = bag.prob_dark()
    if prob_d > 0:

        if bag.last != "milk":
            new_bag = bag_state(bag.dark-1, bag.milk, "dark", bag.prob*prob_d)
        else:
            new_bag = bag_state(bag.dark, bag.milk, None, bag.prob*prob_d)
        add_bag_to_holder(new_bag)


def solve_lvl():
    '''
    Solves one level of the tree to the next level
    '''
    global lvl
    global lvl_holder

    if len(lvl) == 0:
        return False

    for bag in lvl:
        solve_bag_state(bag)

    lvl = lvl_holder
    lvl_holder = list()

    return True


def main():
    global p_milk
    global p_dark

    init_level()

    while solve_lvl():
        print("Solving level")
    
    print("P(Milk) = {0}".format(p_milk))
    print("P(Dark) = {0}".format(p_dark))

main()
