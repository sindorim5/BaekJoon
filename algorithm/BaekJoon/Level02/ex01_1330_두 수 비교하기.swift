//
//  ex01_1330_두 수 비교하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var line = readLine()
var array: [String] = []
var a, b: Int
if line != nil && line != "" {
    array = line!.components(separatedBy: " ")
    a = Int(array[0])!
    b = Int(array[1])!
}
else {
    print("NO INPUT")
    exit(1)
}

if (a > b) {
    print(">")
}
else if (a < b) {
    print("<")
}
else if (a == b) {
    print("==")
}
