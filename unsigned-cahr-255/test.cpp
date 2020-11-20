#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
   cout << "Hello World" << endl; 
   
   int l = 100, r= 400;
   
   vector<int> res;
   int x=0,y=0;
   int limit = 0;
   while(limit<1000){
       
       int n = pow(3,x) * pow(5,y);
       cout<< n <<endl;
       if(l<=n && n<=r){
           res.push_back(n);
       }
       if(n>r){
            if(x==0)
                break;
           x=0;
           y++;
       }
       
       x++;
       limit++;
   }
   
   for(auto n:res)
        cout<< n <<endl; 
   return 0;
}
