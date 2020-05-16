#include <cstdlib>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

/*
Advantage:
    2 rolls, keep higher roll

DisAdvantage:
    2 rolls, keep lower roll

Advantage + DisAdvantage:
    1 roll

Advantage of DisAdvantage:
    Do the following twice:
        2 rolls, keep lower roll
    Keep the higher of the 2 instances

DisAdvantage of Advantage
    Do the following twice:
        2 rolls, keep higher roll
    Keep the lower of the 2 instances
*/

float my_own_accum(int arr[20])
{
    // std accumulate was getting the pointer wrong half the time, made my own
    int i;
    float ret = 0;

    for (i = 0; i < 20; i++)
    {
        ret = ret + arr[i];
    }

    return ret;
}

void calc_ex(int arr[20])
{
    float probability, expected = 0;
    int i, j, sum;
    // Get the number of rolls within the array to find expected val
    float n = my_own_accum(arr);

    //cout << "\tN: " << n << endl;

    // calculate expected value for roll
    for (i = 0; i < 20; i++)
    {
        // expected value += value * number_of_instances_of_value / total_number_of_rolls
        expected = expected + ((i + 1) * (arr[i] / n));
    }
    cout << "\tExpected Value of Roll: " << expected << endl;

    // for indexes 1-19, calculate the probability that you score better than that index
    for (i = 1; i < 20; i++)
    {
        sum = 0;
        for (j = i; j < 20; j++)
        {
            sum = sum + arr[j];
        }
        probability = sum / n;
        cout << "\t\tProbability of Scoring >" << i << ": " << probability << endl;
    }

    return;
}


void expected_val_a()
{
    int results[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int r1 = 0, r2 = 0;

    for (r1 = 1; r1 <= 20; r1++)
    {
        for (r2 = 1; r2 <= 20; r2++)
        {
            results[max(r1, r2) - 1]++;
        }
    }
    
    calc_ex(results);
    return;
}

void expected_val_d()
{
    int results[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int r1 = 0, r2 = 0;

    for (r1 = 1; r1 <= 20; r1++)
    {
        for (r2 = 1; r2 <= 20; r2++)
        {
            results[min(r1, r2) - 1]++;
        }
    }
    
    calc_ex(results);
    return;
}

void expected_val_ad()
{
    // just sending an array of 1's as this is the case for a fair dice
    int results[20]  = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    calc_ex(results);
    return;
}

void expected_val_aofd()
{
    int results[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int r1_1 = 0, r1_2 = 0;
    int r2_1 = 0, r2_2 = 0;

    for (r1_1 = 1; r1_1 <= 20; r1_1++)
    {
        for (r1_2 = 1; r1_2 <= 20; r1_2++)
        {
            for (r2_1 = 1; r2_1 <= 20; r2_1++)
            {
                for (r2_2 = 1; r2_2 <= 20; r2_2++)
                {
                    results[max(min(r1_1, r1_2), min(r2_1, r2_2)) - 1]++;
                }
            }
        }
    }
    
    calc_ex(results);
    return;
}

void expected_val_dofa()
{
    int results[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int r1_1 = 0, r1_2 = 0;
    int r2_1 = 0, r2_2 = 0;

    for (r1_1 = 1; r1_1 <= 20; r1_1++)
    {
        for (r1_2 = 1; r1_2 <= 20; r1_2++)
        {
            for (r2_1 = 1; r2_1 <= 20; r2_1++)
            {
                for (r2_2 = 1; r2_2 <= 20; r2_2++)
                {
                    results[min(max(r1_1, r1_2), max(r2_1, r2_2)) - 1]++;
                }
            }
        }
    }
    
    calc_ex(results);
    return;
}

int main()
{
    cout << "With Advantage" << endl;
    expected_val_a();

    cout << "With Disadvantage" << endl;
    expected_val_d();

    cout << "With Advantage+Disadvantage" << endl;
    expected_val_ad();
    
    cout << "With Advantage of Disadvantage" << endl;
    expected_val_aofd();
    
    cout << "With Disadvantage of Advantage" << endl;
    expected_val_dofa();

    return 1;
}
