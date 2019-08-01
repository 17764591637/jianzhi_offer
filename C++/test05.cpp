#include <iostream>
using namespace std;

int max(int num1,int num2);
int main()
{
    int a = 100;
    int b = 200;
    int res;
    res = max(a,b);
    cout << res << endl;

    return 0;

}

int max(int num1,int num2)
{
    int result;
    if (num1>num2)
        result = num1;
    else
        result = num2;
    
    return result;
}