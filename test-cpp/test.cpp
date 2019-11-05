#include<iostream>
using namespace std;

int main () {
	bool B = false;
	cout << B << endl;
    if (1) { 
    	cout << B << endl;
        if (1) {
        	cout << B << endl;
            if (1) { 
            	cout << B << endl;
                bool B = true;
                cout << B << endl;
            } 
            cout << B << endl;
        }
        cout << B << endl;
    } 
    cout << B << endl;

cout << "#################" << endl;

	bool L = false;
	cout << L << endl;
    if (1) { 
    	cout << L << endl;
        if (1) {
        	cout << L << endl;
            if (1) { 
            	cout << L << endl;
                L = true;
                cout << L << endl;
            } 
            cout << L << endl;
        }
        cout << L << endl;
    } 
    cout << L << endl;

	return 1;
}