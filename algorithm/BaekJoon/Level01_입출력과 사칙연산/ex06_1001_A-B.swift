//
//  ex06_1001_A-B.swift
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
    print(a-b)
    exit(0)
}
else {
    print("NO INPUT")
    exit(1)
}
