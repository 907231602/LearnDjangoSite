#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
import numpy as np
from cmdb.excise import picHandle

def makeShuzu(ss,):
    print(ss)
    kk = []
    for x in range(100):
        kk.append(x)
    return kk

if __name__ == "__main__":
    sa = picHandle.imageHanle('../pic/pic.png')
    ff=makeShuzu(sa)

    #print(ff)
    # c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    # print(c.shape)
    # c.shape=2,2,-1
    # print(c)