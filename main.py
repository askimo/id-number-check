#!/usr/bin/env/ python
#-*-coding:utf-8-*-

import re


def id_number_check(id_number,debug = False):

    #regular of id_number:
    #/^\d{6}(18 | 19 | 20)?\d{2}(0[1-9]|1[012])(0[1-9]|[12]\d|3[01])\d{3}(\d|X)$/
    if debug:
         print('---check----')
    num=id_number.upper()
    id_re=re.compile('^\d{6}(18|19|20)\d{2}(0[1-9]|1[012])(0[1-9]|[12]\d|3[01])\d{3}(\d|X)$')
    if not id_re.match(num) :
        if debug:
            print(num,' is Not ID Number')
        return False
    if debug:
        print('id-no='+num)
    pri=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    rest='10X98765432'
    sum=0
    for i,n, in enumerate(pri):
        sum+=int(num[i])*n
    if debug:
        print('sum='+str(sum)+'\r\nsum mod 11 = '+str(sum%11))
        print('check res='+str(rest[sum%11]))
    if num[17] == rest[sum%11]:
        return True
    else:
        return False



if __name__=='__main__':

    line=0
    with open('id.txt',encoding='utf-8') as file:
        for id_n in file:
            line=line+1
            try:
                if(not id_number_check(id_n)):
                    print(line,id_n)
            except :
                print(line,id_n)