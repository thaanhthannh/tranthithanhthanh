# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:46:59 2024

@author: Thanh Thanh
"""
chuoi = "Dai hoc quoc gia, Khu pho 6, P.Linh Trung, Q.Thu duc, Tp.HCM"
sub_string_2=[a.strip() for a in chuoi.replace("P.", " ").replace("Q."," ").replace("Tp."," ").split(",")]
for a in sub_string_2:
    print(a)