#include <iostream>

using namespace std;

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;

    
    for (int i = 1; i <= number; ++i) {
        if (number % i == 0) {
            cout << "Factors of " << number << " are: "<< i<<" ";
        }
    }

    return 0;
}
