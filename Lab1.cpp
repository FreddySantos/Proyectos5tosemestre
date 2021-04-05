#######################################    Ejercicio 1    ##############################################
#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;

double p;
double n;
double v;

int V1 = rand()%100;

int main()
{
    bool a[V1];

    for (int i=0; i<V1;i++)
    {
        if(a[i])
        {
            puts("T");
            v = v+1;
        }
        else {
            puts("F");
            n = n + 1;
        }
    }
    p=(v/sizeof(a))*100;
    cout << "True: " << v << endl;
    cout << "False: " << n << endl;
    cout << "% of True: " << setprecision(6) << p << endl;
}


#####################################      Ejercicio 3      ###############################################

#include <iostream>

using namespace std;

int main()
{
    const char* name[] = { "F", "R", "E", "D", "Y" };
    for(int i = 4; i >= 0; i--)
    {
        cout << name[i] << endl;
    }
    return 0;
}

######################################       Ejercicio 5    #####################################################

#include <iostream>

using namespace std;
int main()
{

    string x = "Hola mundo de Fredy";
        for(int c : x)
        {
            cout << c
                << endl;
        }
    return 0;
}

########################################       Ejercicio 8       ###################################################

#include <iostream>
using namespace std;

int main()
{
    double sum = 0, promedio;
    int contador = 0,x,y;
    int arr[10];
    
    cout << "Ingrese solo 10 valores : ";
    for (int& i : arr)
    {   
        cin >> x;
        i = x;
    }
    y = sizeof(arr) / sizeof(arr[0]);
    for (int j = 0; j < y; j++)
    {
        sum += arr[j];
        promedio = sum / y;
    }
    for (int k : arr)
    {
        {
            contador++;
        }
    }
    cout << "Numeros encima del promedio: " << contador << endl;
    cout << "El promedio es: " << promedio << endl;
    
    return 0;
}

#########################################################################################################

