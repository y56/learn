#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 03:36:56 2020

@author: y56
"""

def TetrisMove(strArr):
  def score(myp,row,col):
    tmpb=[[0]*gw for _ in range(gh)]

    _col=0
    for x in strArr[1::]:
      for xh in range(int(x)):
        tmpb[xh][_col]+=1
      _col+=1

    for i,_row in enumerate(myp):
      for j,x in enumerate(_row):
        if x==1:
          tmpb[row+i][col+j]=1
    res=0
    # print(tmpb)
    for _row in tmpb:
      if sum(_row)==gh:
        # print('^^')
        res+=1
    return res

  def goodbuttom(myp,row,col):
    for c in range(0, len(myp[0]) ):
      for r in range(0, len(myp)):
        # print(c,r)
        
          
          print(row+r+1)
          if row+r+1>=len(gb) or gb[row+r+1][col+c]==1:
            return True
          break
    return False
  #
  def goodtouch(myp,row,col):
    for r in range(0,len(myp)):
      for c in range(0,len(myp[0])):
        if gb[row+r][col+c]==1 and myp[r][c]==1:
          
          return False
    return True
  #
  def rotate(p):
    h=len(p)
    w=len(p[0])
    res=[[0]*h for _ in range(w)]
    for r in range(w):
      for c in range(h):
        res[r][c]=p[c][w-1-r]
    return res
    
  #
  gw=12
  gh=10
  mypletter=strArr[0]
  pshapedict={
    'I':[ [1,1,1,1] ],
    'J':[ [1,1,1],[0,0,1]],
    'L':[ [1,1,1],[1,0,0]],
    'O':[ [1,1],[1,1]],
    'S':[ [0,1,1],[1,1,0]],
    'T':[ [1,1,1],[0,1,0]],
    'Z':[ [1,1,0],[0,1,1]]}
  myp = pshapedict[mypletter]
  gb=[[0]*gw for _ in range(gh)]
  _col=0
  for x in strArr[1::]:
    for xh in range(int(x)):
      gb[xh][_col]+=1
    _col+=1
  # for x in gb:
  #   print(x)
  mypli=[myp]
  myp=rotate(myp)
  mypli.append(myp)
  myp=rotate(myp)
  mypli.append(myp)
  myp=rotate(myp)
  mypli.append(myp)
  ans=0
  for myp in mypli:
    myph=len(myp)
    mypw=len(myp[0])

    for row in range(0,gh-myph+1):
      for col in range(0,gw-mypw+1):
        if goodtouch(myp,row,col) and goodbuttom(myp,row,col):
          ans=max(ans,score(myp,row,col))

  return ans

# keep this function call here 
print(TetrisMove(
        ["I", "2", "4", "3", "4", "5", "2", "0", "2", "2", "3", "3", "3"]
        ))
