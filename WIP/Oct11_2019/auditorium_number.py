















def number_indivisible(num):

    indivisible_count = 0
    indivisible_list = []

    for i in range(200):
        
        if (200 % (i + 1)) != 0:
            indivisible_count += 1
            indivisible_list.append(i + 1)

        if indivisible_count > 2:
            return (False, [])


    if indivisible_count != 2:
        return (False, [])

    return (True, indivisible_list)


def find_number():
    lower_lim = 1
    upper_lim = 1000 * 1000 * 100

    for i in range(lower_lim, upper_lim):

        print i 

        ret = number_indivisible(i)
        if ret[0] == True:
            
            if ret[1][0] + 1 == ret[1][1]:
            
                print "Number is {0}, indivisible by {1} & {2}".format(i, ret[1][0], ret[1][1])
                return


find_number()
