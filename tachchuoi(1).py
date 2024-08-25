# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:45:35 2024

@author: Thanh Thanh
"""
chuoi = "Dai hoc quoc gia, Khu pho 6, P.Linh Trung, Q.Thu duc, Tp.HCM"
#Tach chuoi
sub_string= [i.strip() for i in chuoi.split(",")]
for i in sub_string:
    print(i)