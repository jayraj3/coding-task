#include <bits/stdc++.h>

using namespace std;



/*
 * Complete the 'getMaxDeletions' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int getMaxDeletions(string s) {
    int R = 0;
    int L = 0;
    int U = 0;
    int D = 0; 
    //cout<<R<<" "<<L<<" "<<U<<" "<<D;

    for(int i=0; i<s.size(); i++){
        if(s[i]=='R'){
            R++;
        }
        if(s[i]=='L'){
            L++;
        }
        if(s[i]=='U'){
            U++;
        }
        if(s[i]=='D'){
            D++;
        }
    }
    int NumHorizontal = 0;
    int NumVertical = 0; 


    if(D>U){
       NumVertical = D - U; 
    }
    else {
        NumVertical = U - D;
    }
    if(R>L){
       NumHorizontal = R - L; 
    }
    else {
        NumHorizontal = L - R;
    }
    //cout<<s.size()<<endl;
    int ValidSteps = NumVertical + NumHorizontal;
    //cout<<total<<endl; 
    int StepReduction = s.size() - ValidSteps;
    //cout<<R<<" "<<L<<" "<<U<<" "<<D;
    return StepReduction;
}

int main()