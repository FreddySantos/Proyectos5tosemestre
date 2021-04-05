#include <iostream>
#include <stdlib.h>
using namespace std;
const int fil =7;
const int col =8;

bool verificar_palabra(string,char[fil][col]);
void sopa_letras(string,char[fil][col]);

int main()
{ 
	string palabra,palabras_acertadas[fil*col];
	char sopa[fil][col] = {
							{'h','o','l','a','f','a','j'},
							{'r','t','a','j','r','n','n'},
							{'p','a','n','t','e','r','a'},
							{'f','g','d','a','d','e','n'},
							{'p','g','l','w','y','q','v'},
							{'i','o','n','x','z','t','h'},
							{'h','k','c','u','f','m','b'},
	                       };
	for(int i =0 ; i < fil ; i++)
	{
		for(int j =0 ; j < col ; j++)
		{
			cout<< sopa[i][j]<<" ";
		}
		cout << endl;
	}

	cout << "Ingrese la palabra a buscar: " ; 
	
	do
		cin >> palabra;
	while(palabra.length() < 3);

	sopa_letras(palabra,sopa);
	return 0;
}	

bool verificar_palabra(string palabra,char letras [fil][col])
{
	string aux, vacia;
	int cont = 0;
    //Busca palabra horizontal ->
	for(int i = 0; i < fil; i++)
	{
		for(int k = 0; k <= col-palabra.length(); k++)
		{
			for(int j = k; j < palabra.length()+k; j++)
			{
				aux += letras[i][j];
			}
			if(palabra==aux)
			{
				cont++;
				return true;
			}
			aux=vacia;
		}
	}
	//Busca palabras horizontal <-
	for(int i = 0; i < fil; i++)
	{
		for(int k = col-1; k >= palabra.length(); k--)
		{
			for(int j = k; j > k-palabra.length(); j--)
			{
				aux += letras[i][j];
			}
			if(palabra==aux)
			{
				cont++;
				return true;
			}
			aux=vacia;
		}
	}
	//Busca palabras en vertical bajando
	for(int i = 0; i < col; i++)
	{
		for(int k = 0; k <= fil-palabra.length(); k++)
		{
			for(int j = k; j < palabra.length()+k; j++)
			{
				aux += letras[j][i];
			}
			if(palabra==aux)
			{
				cont++;
				return true;
			}
			aux=vacia;
		}
	}
	//Buscar subida
	for(int i = 0; i > col; i++)
	{
		for(int k = fil-1; k >= palabra.length(); k--)
		{
			for(int j = k; j > palabra.length()-k; j--)
			{
				aux += letras[j][i];
			}
			if(palabra==aux)
			{
				cont++;
				return true;
			}
			aux=vacia;
		}
	}
	


	if(cont==0)
		return false;
}
void sopa_letras(string palabra,char sopa [fil][col])
{
	int acertadas = 0, erradas = 0;
	char salir;
	do
	{
		if(verificar_palabra(palabra,sopa))
		{
			cout << "Palabra encontrada." << endl;
			acertadas++;
		}
		else
		{
			cout << "La palabra no se encuentra en la sopa de letras." << endl;
			erradas++;
		}
		cout << "Para salir s/n: ";
		cin	>> salir;
		if(salir=='n')
		{
			system("cls");
			for(int i =0 ; i < fil ; i++)
			{
				for(int j =0 ; j < col ; j++)
				{
				cout<< sopa[i][j]<<" ";
				}
				cout << endl;
			}
			cout << "Acertadas:  " << acertadas << "  Erradas:  " <<erradas << endl;
			cout << "Introdusca la palabra que quiere buscar: " ;

			do
				cin >> palabra;
				while(palabra.length() < 3);
		}
	}
	while(salir != 's');
	system("cls");
	cout << "Acertadas: " << acertadas << "  Erradas: " <<erradas << endl;
	system("pause");
}

