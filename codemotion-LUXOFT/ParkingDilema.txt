#include <bits/stdc++.h>

using namespace std;

string ltrim(const string&);
string rtrim(const string&);



/*
 * Complete the 'carParkingRoof' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. LONG_INTEGER_ARRAY cars
 *  2. INTEGER k
 */

long carParkingRoof(vector<long> cars, int k) {
    // if(k==1){
    //     return 1;
    // }
    // for(int i=0; i < cars.size(); i++)
    //  cout << cars.at(i) << ' ';
    sort(cars.begin(), cars.end());
    // for(auto i:cars){
    //     cout<<i<<" ";
    // }
    //int LastOccupied = *max_element(cars.begin(), cars.end());
    //int FirstOccupied = *min_element(cars.begin(), cars.end());
    //cout << min<<endl;
    long Total = cars.size();
    long max = cars.at(Total - 1) - cars.at(0) + 1;
    // if(Total == k){
    //     //cout<<cars[Total-1];
    //     //int &LastCar = cars[0];
    //     return max;//LastOccupied - FirstOccupied +1;
    // }


    long Iteration = Total - k + 1;
    //cout<<k;

    long MinSpace = max;
    for (long i = 0; i < Iteration; i++) {
        long covered = cars.at(k + i - 1) - cars.at(i) + 1;
        //cout<<i;

        if (covered < MinSpace) {
            MinSpace = covered;
        }
    }

    return MinSpace;
}
