
ALMOND_INDEX = 0
BUTTER_INDEX = 1
KERNEL_INDEX = 2

candy_perms = list()


def recursive(candy_list):
    global candy_perms

    #Alotment full
    if sum(candy_list) => 100:
        return

    #Pick an Almond
    almond_list = list(candy_list)
    almond_list[ALMOND_INDEX] = almond_list[ALMOND_INDEX] + 1
    if almond_list not in candy_perms:
        candy_perms.append(almond_list)
        recursive(almond_list)

    #Pick a Butter
    butter_list = list(candy_list)
    butter_list[BUTTER_INDEX] = butter_list[BUTTER_INDEX] + 1
    if butter_list not in candy_perms:
        candy_perms.append(butter_list)
        recursive(butter_list)

    #Pick a Kernel
    kernel_list = list(candy_list)
    kernel_list[KERNEL_INDEX] = kernel_list[KERNEL_INDEX] + 1
    if kernel_list not in candy_perms:
        candy_perms.append(kernel_list)
        recursive(kernel_list)


def main():
    global candy_perms

    candy_list = [0, 0, 0]
    recursive(candy_list)

    print "Number of Candy Permutations: {0}".format(len(candy_perms))

main()
