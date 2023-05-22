//
//  ex6_2742_기찍N.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var count = readLine()
var countInt: Int
var result: Int

if count != nil && count != "" {
    countInt = Int(count!)!
}
else {
    print("NO INPUT")
    exit(1)
}

while(countInt > 0){
    print(countInt)
    countInt -= 1
}
