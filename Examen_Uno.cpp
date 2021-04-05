#include <iostream>
#include <stdio.h>
#include <cstdint>
//#include <windows.h>
using namespace std;

int main()
{
   FILE* salida, * entrada;
	salida = fopen("c:\\test_sniffer\\salida.txt", "w");
	
	if (salida == NULL)
	{
		printf("Error, no se puede abrir el archivo\n");

	}
	else
	{
	    /*	0000   6c 71 d9 2f 47 05 10 50 72 7c 86 6e 08 00 45 70
			0010   00 34 60 f5 40 00 ed 06 61 10 0d e2 fb 81 c0 a8
			0020   01 42 01 bb fb 6a c3 39 ba 12 40 31 73 87 80 10
			0030   00 7b 18 59 00 00 01 01 05 0a 40 31 73 86 40 31
			0040   73 87
		*/
	   int a=100, b=200;
	               //   0    1    2    3   4    5     6    7    8   9    10   11  12   13   14   15 //
	 int vals [66] ={0x6c,0x71,0xd9,0x2f,0x47,0x05,0x10,0x50,0x72,0x7c,0x86,0x6e,0x08,0x00,0x45,0x70,
	       /*16*/    0x00,0x34,0x60,0xf5,0x40,0x00,0xed,0x06,0x61,0x10,0x0d,0xe2,0xfb,0x81,0xc0,0xa8,/*31*/
	      /*32*/     0x01,0x42,0x01,0xbb,0xfb,0x6a,0xc3,0x39,0xba,0x12,0x40,0x31,0x73,0x87,0x80,0x10,/*47*/
	      /*48*/     0x00,0x7b,0x18,0x59,0x00,0x00,0x01,0x01,0x05,0x0a,0x40,0x31,0x73,0x86,0x40,0x31,
	                 0x73,0x87};
	                 
	  // Version
	  int version= vals[14];
	  printf("version: %d\n ", version >>4);
	  // Header Length
	  int length = ((vals[14]) & ((1 << (4)))-1);
	  printf("Header length: %d bytes (%d)\n" , length * 4, length);
	  // Differentiated Services Field
	  printf("Differentiated Services Field: %d\n" , vals[15]);
	  // Total Length
	  int totallength = ((vals[16] << 8) ^ vals[17]);
	  printf("Total Length: %d\n" , totallength);
	  // identicacion
	  int ID = ((vals[18] << 8) ^ vals[19]);
	  printf("identicacion : %d\n" , ID);
	  //Time to live
	  printf("Time to live: %d\n" , vals[22]);
	  // Protocol
	  printf("Protocol: %d\n" , vals[23]);
	  // Source
	  
	   int source4 = vals [26];
	   int source3 = vals [27];
	   int source2 = vals [28];
	   int source1 = vals [29];
	  
	  
	  printf("Source = %u", (source4 & 255));
	  printf(".");
	  printf("%u", (source3& 255));
	  printf(".");
	  printf("%u", (source2 & 255));
	  printf(".");
	  printf("%u\n", (source1 & 255));
	  
	  // Destino
	   int destino4 = vals [30];
	   int destino3 = vals [31];
	   int destino2 = vals [32];
	   int destino1 = vals [33];
	  
	
	  
	   printf("Destino = %u", (destino4 & 255));
	   printf(".");
	   printf("%u", (destino3 & 255));
	   printf(".");
	   printf("%u", (destino2 & 255));
	   printf(".");
	   printf("%u\n", (destino1 & 255));

	 /////////////////////////////// TCP   ////////////////////////////////////////
	 //Source Port
	 int Sport = ((vals[34] << 8) ^ vals[35]);
	  printf("Source Port: %d\n" , Sport);
	  //Destination Port
	  int Dport = ((vals[36] << 8) ^ vals[37]);
	  printf("Destination Port: %d\n" , Dport);
	  //Sequence number (raw)
	   int Snumber4 = vals [38];
	   int Snumber3 = vals [39];
	   int Snumber2 = vals [40];
	   int Snumber1 = vals [41];
	  
	  
	  printf("Sequence number (raw): = %u", (Snumber4 & 255));
	  printf("%u", (Snumber3& 255));
	  printf("%u", (Snumber2 & 255));
	  printf("%u\n", (Snumber1 & 255));
	  
	  //Acknowledgment number (raw):
	  
	  int Anumber4 = vals [42];
	   int Anumber3 = vals [43];
	   int Anumber2 = vals [44];
	   int Anumber1 = vals [45];
	  
	  
	  printf("Acknowledgment number (raw): = %u", (Anumber4 & 255));
	  printf("%u", (Anumber3& 255));
	  printf("%u", (Anumber2 & 255));
	  printf("%u\n", (Anumber1 & 255));
	}

    return 0;
}
