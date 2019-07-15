#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 03:37:51 2019

https://www.ptt.cc/bbs/Gossiping/M.1557067415.A.BC2.html

https://gist.github.com/jserv/11d02a2ba126f4056aae5b43ce9fa51f

@author: y56
"""

import atexit
import ctypes
import os
import shlex
#import sys
import tempfile

CMD_C_TO_SO = '{compiler} -shared -o {output} {input} {libraries}'


class C:
    def __init__(self, code, *shared_libs):
        self.library = None
        self._compile(code, shared_libs)

    def _compile(self, code, libs):
        # Dump the C code into a temporary file, and run the compiler
        with tempfile.NamedTemporaryFile(mode='w', prefix='PYC', suffix='.c',
                                         delete=False) as temp_c_file:
            temp_c_file_name = temp_c_file.name
            temp_c_file.write(code)
            temp_c_file.flush()

        # Run the compiler one more time to generate a shared library
        so_file_name = tempfile.mktemp(prefix='PYC', suffix='.so')
        library_cmd = ' '.join('-l' + lib for lib in libs)
        os.system(CMD_C_TO_SO.format(compiler="gcc",
                                     output=shlex.quote(so_file_name),
                                     input=shlex.quote(temp_c_file_name),
                                     libraries=library_cmd))

        # Punt to ctypes so that we can get a loadable library we built
        self.library = ctypes.cdll.LoadLibrary(so_file_name)

        # Ensure that we clean up the temp files when the program is exiting
        atexit.register(lambda: os.remove(so_file_name))

    def __getitem__(self, func):
        if self.library is None:
            assert False, "How did C.__getitem__ get called without loading the library?"
        return getattr(self.library, func)


if __name__ == '__main__':
    mylib = C('''
              
#include <stdio.h>
#include <stdlib.h>
              

int factorial(int x) {
    printf("Mom, I am here!!!");
    printf("position of least significant 1 = %d \n", __builtin_ffs(7368) );
    int ret = 1;
    for (; x > 1; x--)
        ret *= x;
    return ret;
}

''')

    factorial = mylib['factorial']
    print('15! =', factorial(15))
    
    