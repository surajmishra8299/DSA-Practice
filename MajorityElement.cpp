#include<iostream>
using namespace std;

int main(){

    int arr[] = {1,2,2,6,4,6};
    int n = sizeof(arr)/sizeof(arr[0]);

    for(int val : arr){
        int frq=0;
        for(int el : arr){
            if(el==val){
            frq++;
            }
        }
        if(frq>n/2)
            cout<<val;
    }
}