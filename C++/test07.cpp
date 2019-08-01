#include <iostream>
using namespace std;

int main()
{
    int a[5][2] = {{0,0},{1,2},{3,4},{4,5},{5,6}};
    for(int i = 0;i<5;i++)
        for(int j = 0;j<2;j++)
        {
            cout<<a[i][j]<<endl;
        }
    return 0;
}