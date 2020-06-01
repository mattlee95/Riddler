#include <stdc++.h>
#include <algorithm>
#include <utility>
#include <random>

#include "zoomLib.h"

using namespace std;


void permutate(int arr[], int size)
{
    int perms = 0;
    int successes_1 = 0;
    int successes_2 = 0;
    int outcome;
    float rate;

    do
    {
        outcome = solve(arr, size);
        perms++;
        
        if (outcome > 0)
        {
            successes_1++;
        }
        if (outcome > 1)
        {
            successes_2++;
        }

    }
    while (next_permutation(arr, arr+(2*size)));

    free(arr);

    cout << size << " caller Zoom call" << endl;
    cout << "Permutations: " << perms; 

    cout << "\n\tSuccesses (at least 1 caller): " << successes_1; 
    rate = successes_1 / float(perms);
    cout << "\n\tSuccess Rate (1+ caller): " << rate;

    cout << "\n\tSuccesses (at least 2 callers): " << successes_2;
    rate = successes_2 / float(perms);
    cout << "\n\tSuccess Rate (2+ caller): " << rate << endl << endl;

    return;
}


int main()
{
    int const MAX = 7;
    int *arr;

    for(int i = 2; i < MAX; i++)
    {
        arr = create_array(i);
        permutate(arr, i);
    }
}
