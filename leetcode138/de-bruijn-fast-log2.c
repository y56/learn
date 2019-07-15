#include<stdio.h>
#include<stdlib.h>
#include<math.h>


void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i=size-1;i>=0;i--)
    {
        for (j=7;j>=0;j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
    puts("");
}

const int tab32[32] = {
     0,  9,  1, 10, 13, 21,  2, 29,
    11, 14, 16, 18, 22, 25,  3, 30,
     8, 12, 20, 28, 15, 17, 24,  7,
    19, 27, 23,  6, 26,  5,  4, 31};

int log2_32 (u_int32_t value)
{
    printBits(sizeof(value), &value);
    value |= value >> 1;
    printBits(sizeof(value), &value);
    value |= value >> 2;
    printBits(sizeof(value), &value);
    value |= value >> 4;
    printBits(sizeof(value), &value);
    value |= value >> 8;
    printBits(sizeof(value), &value);
    value |= value >> 16;
    
    printBits(sizeof(value), &value);
    
    u_int32_t value000 = (u_int32_t)(value*0x07C4ACDD);
    
    printBits(sizeof(value000), &value000);
    
    u_int32_t value001 = value000 >> 27;
    
    printBits(sizeof(value001), &value001);
    
    return tab32[(u_int32_t)(value*0x07C4ACDD) >> 27];
}
int main() {

   printf("%d", log2_32(pow(2,31)));

}
