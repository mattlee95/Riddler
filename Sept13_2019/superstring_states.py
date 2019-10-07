import time

# States and Territories
STATE_LIST = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']

# States Territories and Military "States"
#STATE_LIST = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AE', 'AP', 'AA']

'''
Level Structure
[("current string", [unused_state_list]), ...]


'''

current_level = []
holder_level = []


def create_next_level():
    global current_level
    global holder_level

    for node in current_level:

        for state in node[1]:

            if state[0] == node[0][len(node[0])-1]:
                tup = (node[0]+state[1], list(node[1]))
                tup[1].remove(state)

                holder_level.append(tup)


    current_level = list(holder_level)
    holder_level = []



def get_longest_string_for_state(state):
    global current_level
    global holder_level

    global STATE_LIST

    start_list = list(STATE_LIST)
    start_list.remove(state)

    current_level = [(state, start_list)]
    holder_level = []

    lowest_level = 1
    lowest_level_list = list(current_level)

    print "\n\n{0}: ".format(state)

    while True:
        t1 = time.time()
        #print current_level
        #print "\t{0}".format(lowest_level)
        create_next_level()
        if len(current_level) > 0:
            lowest_level += 1
            lowest_level_list = list(current_level)

        else:
            '''for i in lowest_level_list:
                print i[0]'''
            return (lowest_level, lowest_level_list)
            
        t2 = time.time()
        print "\t{0}, compute time: {1} sec(s)".format(lowest_level,int(t2-t1))


def run_for_all():
    global STATE_LIST

    current_longest = 0
    current_longest_list = []

    for state in STATE_LIST:
        result_tup = get_longest_string_for_state(state)

        if result_tup[0] > current_longest:
            current_longest_list = list(result_tup[1])
            current_longest = result_tup[0]
        elif result_tup[0] == current_longest:
            current_longest_list.append(list(result_tup[1]))
        else:
            pass

    print "Longest String: {0}".format(current_longest)
    #print current_longest_list
    for unique_string in current_longest_list:
        print unique_string[0]



run_for_all()
#get_longest_string_for_state("FM")
