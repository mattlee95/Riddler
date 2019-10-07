import random
import sys

'''
MM : 40% walks 60% SO

DD : 20% double 80% SO

TT : 10% HR 90% SO
'''




def simulate_inning(team):
    outs = 0 
    runs = 0
    runners = 0

    if team == "MM":
        while outs < 3:
            if random.randint(1,10) > 6:
                if runners >= 3:
                    runs += 1
                else:
                    runners += 1
            else:
                outs += 1


    elif team == "DD":
        while outs < 3:
            if random.randint(1,10) > 8:
                if runners >= 1:
                    runs += 1
                else:
                    runners += 1

            else:
                outs += 1
 
    elif team == "TT":
        while outs < 3:
            if random.randint(1,10) > 9:
                runs += 1
            else:
                outs += 1
        
    else:
        exit(1)

    return runs



def simulate_game(team1, team2):
    team1points = 0
    team2points = 0

    for i in range(9):
        team1points += simulate_inning(team1)
        team2points += simulate_inning(team2)

    while (team1points == team2points):
        team1points += simulate_inning(team1)
        team2points += simulate_inning(team2)

    #print "\t{0} vs. {1} : {2} - {3}".format(team1, team2, team1points, team2points)

    if team1points > team2points:
        return 1

    else:
        return 0




def simulate_records():
    MM = "MM"
    DD = "DD"
    TT = "TT"

    NUM_SIMS = 182 * 10 * 1000 * 1000

    # record of MM vs. DD
    mm_wins = 0
    for i in range(NUM_SIMS):
        mm_wins += simulate_game(MM, DD)
        print i
        #sys.stdout.write("\033[F")
    print "MM vs. DD record: {0} - {1}".format(mm_wins, NUM_SIMS-mm_wins)

    # record of TT vs. MM
    tt_wins = 0
    for i in range(NUM_SIMS):
        tt_wins += simulate_game(TT, MM)
        print i
        #sys.stdout.write("\033[F")
    print "TT vs. MM record: {0} - {1}".format(tt_wins, NUM_SIMS-tt_wins)

    # record of DD vs. TT
    dd_wins = 0
    for i in range(NUM_SIMS):
        dd_wins += simulate_game(DD, TT)
        print i
        #sys.stdout.write("\033[F")
    print "DD vs. TT record: {0} - {1}".format(dd_wins, NUM_SIMS-dd_wins)



    # league records

    print "MM league winning percentage: {0}".format((mm_wins + (NUM_SIMS-tt_wins))/float(2.0*NUM_SIMS))

    print "DD league winning percentage: {0}".format((dd_wins + (NUM_SIMS-mm_wins))/float(2.0*NUM_SIMS))

    print "TT league winning percentage: {0}".format((tt_wins + (NUM_SIMS-dd_wins))/float(2.0*NUM_SIMS))


simulate_records()
