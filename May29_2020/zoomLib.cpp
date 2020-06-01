#include <stdc++.h>
#include <algorithm>
#include <utility>

using namespace std;


int* create_array(int size)
{
    int *arr = (int *) malloc(2 * size * sizeof(int));
    
    for(int i = 0; i < (2*size); i++)
    {
        arr[i] = i+1;
    }

    return arr;
}


int solve(int perm[], int size)
{
    int earliest_dep = (2 * size) + 1;
    int latest_arr = - 1;
    int *caller;
    int matches;

    for(int i = 0; i < size; i++)
    {
        caller = &perm[2*i];

        if (min(*(caller), *(caller+1)) > latest_arr)
        {
            latest_arr = min(*(caller), *(caller+1));
        }
        if (max(*(caller), *(caller+1)) < earliest_dep)
        {
            earliest_dep = max(*(caller), *(caller+1));
        }
    }

    matches = 0;

    for(int i = 0; i < size; i++)
    {
        caller = &perm[2*i];

        if ((min(*(caller), *(caller+1)) <= earliest_dep) && (max(*(caller), *(caller+1)) >= latest_arr))
        {
            matches++;
        }
    }

    return matches;
}


void cout_arr(int *arr, int size)
{
    cout << size << " arr: ";

    for(int i=0; i < 2*size; i++)
    {
        cout << arr[i] << ",";
    }

    cout << endl;
}
