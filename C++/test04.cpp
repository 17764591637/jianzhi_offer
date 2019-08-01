#include <iostream>
using namespace std;
int main()
{
    char grade = 'B';
    switch (grade)
    {
    case 'A'/* constant-expression */:
        /* code */
        cout << "good" << endl;
        break;
    case 'B':
        cout << "good" << endl;
    // default:
    // cout << "not good" << endl;
    //     break;
    }

    return 0;
}