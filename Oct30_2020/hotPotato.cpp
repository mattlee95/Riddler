#include <cstdlib>
#include <iostream>

using namespace std;


int index_to_elim(int game[61], int index_start, int N)
{
    /*
    Based on where we are starting this round of the game and what the N value
    is, this function returns the next index to be marked as out of the game
    */

    int alive_seen = 0;
    int idx = index_start;

    while (1)
    {
        idx = idx % 61;
        if (game[idx] == 0)
        {
            alive_seen++;
            if (alive_seen == N)
            {
                return idx;
            }
        }
        idx++;
    }
}


int next_index_alive(int game[61], int index_last_elim)
{
    /*
    Based on the last index to be marked as out of the game, this function
    returns the index of the next player still in who can start next round
    */

    int idx = index_last_elim + 1;

    while (1)
    {
        idx = idx % 61;
        if (game[idx] == 0)
        {
            return idx;
        }
        idx++;
    }
}


int who_wins(int N, bool verbose)
{
    /*
    Function returns the index of the winner of a game given the starting value of N
    */

    int game[61] = {};
    int players_remaining = 61;
    int player_start = 0;
    int curr_N;
    int elim_idx;

    if (verbose) {cout << "Starting Game with N = " << N << endl;}

    while (players_remaining > 1)
    {
        /*
        Modulus by the number of remaining players to cut down on unneeded
        cycles around the array

        Interesting edge case is since we start counting at 1, not 0, we need
        to catch when modulus results in 0 and set it to remianing players
        */
        curr_N = N % players_remaining;
        if (curr_N == 0)
        {
            curr_N = players_remaining;
        }

        elim_idx = index_to_elim(game, player_start, curr_N);
        game[elim_idx] = 1;
        if (verbose) {cout << "Eliminating Player: " << elim_idx+1 << endl;}

        player_start = next_index_alive(game, elim_idx);
        players_remaining--;
    }
    return player_start+1;
}


int extra_extra_credit()
{
    int n = 0;
    int winner = 0;

    while (winner != 1)
    {
        n++;
        cout << "Extra Extra Credit: Attempting N = " << n << endl;
        winner = who_wins(n, false);
    }
    return n;
}


int solve_classic()
{
    /*
    - In the game’s first round, the player 18 spaces to your left is the first to be eliminated
        - (N - 19) % 61 == 0

    - The second round sees the elimination of the player 31 spaces to Ricky’s left
        - (N - 32) % 60 == 0
        
    - Zach begins the third round, only to find himself eliminated in a cruel twist of fate
        - (N - 1) % 59 == 0
    */

    int i = 0;
    int val;

    while (1)
    {
        val = 19 + (61 * i);
        if ((((val - 32) % 60) == 0) && (((val - 1) % 59) == 0))
        {
            return val;
        }
        i++;
    }
}


int main()
{
    int classic_answer;
    int extra_credit_answer;
    int extra_extra_credit_answer;

    classic_answer = solve_classic();
    cout << "Value of N for Classic: " << classic_answer << endl << endl;

    extra_credit_answer = who_wins(classic_answer, true);
    cout << "Winner for Extra Credit Riddle: " << extra_credit_answer << endl << endl;

    extra_extra_credit_answer = extra_extra_credit(); 
    cout << "Lowest N so I win (Extra Extra Credit Riddle): " << extra_extra_credit_answer << endl;

    return 1;
}
