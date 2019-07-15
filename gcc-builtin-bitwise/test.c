#include <stdio.h>

int main(void) {
// int __builtin_ffs (unsigned int x)
// 返回x的最后一位1的是从后向前第几位，比如7368（1110011001000）返回4。
printf("position of least significant 1 = %d \n", __builtin_ffs(7368) );

// int __builtin_clz (unsigned int x)
// 返回前导的0的个数。
printf("count leading zeros = %d \n", __builtin_clz(8) );

// int __builtin_ctz (unsigned int x)
// 返回后面的0个个数，和__builtin_clz相对。
printf("count trailing zeros = %d \n", __builtin_ctz(256) );

// int __builtin_popcount (unsigned int x)
// 返回二进制表示中1的个数。
printf("count ones = %d \n", __builtin_popcount(255) );

// int __builtin_parity (unsigned int x)
//返回x的奇偶校验位，也就是x的1的个数模2的结果。
printf("mod 2 of number of ones = %d \n", __builtin_parity(254) );

return 0;
}
