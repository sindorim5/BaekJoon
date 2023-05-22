//
//  ex10_10430_나머지.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var line = readLine()
var array: [String] = []
if line != nil && line != "" {
    array = line!.components(separatedBy: " ")
    let a = Int(array[0])!
    let b = Int(array[1])!
    let c = Int(array[2])!
    print((a+b)%c)
    print(((a%c) + (b%c))%c)
    print((a*b)%c)
    print( ((a%c) * (b%c))%c)
    exit(0)
}
else {
    print("NO INPUT")
    exit(1)
}
