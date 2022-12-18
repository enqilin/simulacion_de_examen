import math
import os
import random
import re
import sys

def verticalRooks(r1, r2):
    N=int(input())
    pos1=[]
    pos2=[]
    for i in range(N):
        r1,r2=map(int,input().split())
        pos1.append(r1)
        pos2.append(r2)
    has_advantage=False
    for i in range(N):
        if pos1[i]<pos2[i]:
            has_advantage=True
            break
    if has_advantage:
        best_move=-1
        max_diff=-1
        for i in range(N):
                diff=pos2[i]-pos1[i]
                if diff>max_diff:
                    max_diff=diff
                    best_move=i
        pos2[best_move]=N
        for i in range(N):
            print(pos1[i],pos2[i])
    else:

