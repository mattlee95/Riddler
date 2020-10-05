#include <stdc++.h>
#include <algorithm>
#include <utility>
#include <random>

#include "zoomLib.h"

using namespace std;


void matt_shuff(int *arr, int size)
{
    int holder;
    int shuff_idx;

    for(int i = 0; i < 2*size; i++)
    {
        //cout << "Shuffle Index: " << shuff_idx << ", Index: " << i << endl;
        shuff_idx = rand() % (2*size);
    
        holder = arr[shuff_idx];
        arr[shuff_idx] = arr[i];
        arr[i] = holder;
    }

    return;
}


void simulate(int *arr, int size, int SIMS)
{
    int successes_1 = 0;
    int successes_2 = 0;
    int outcome;
    float rate;
    unsigned seed = 0;

    for(int i = 0; i < SIMS; i++)
    {
        /*for(int n = 0; n < 2*size; n++)
        {
            cout << arr[n] << ", ";
        }
        cout << endl;*/
        //std shuffle doesnt work, ima make my own
        //shuffle(arr, arr+(2*size), default_random_engine(seed));
        matt_shuff(arr, size);

        outcome = solve(arr, size);

        if (outcome > 0)
        {
            successes_1++;
        }
        if (outcome > 1)
        {
            successes_2++;
        }
    }

    free(arr);

    cout << size << " caller Zoom call" << endl;
    cout << "Simulations: " << SIMS; 

    cout << "\n\tSuccesses (at least 1 caller): " << successes_1; 
    rate = successes_1 / float(SIMS);
    cout << "\n\tSuccess Rate (1+ caller): " << rate;

    cout << "\n\tSuccesses (at least 2 callers): " << successes_2;
    rate = successes_2 / float(SIMS);
    cout << "\n\tSuccess Rate (2+ caller): " << rate << endl << endl;

}


int main()
{
    //int const MAX = 3;
    //int const SIMS = 20;
    int const MAX = 100;
    int const SIMS = 1000 * 1000;
    int *arr;

    for(int i = 2; i < MAX; i++)
    {
        arr = create_array(i);
        simulate(arr, i, SIMS);
    }
}
