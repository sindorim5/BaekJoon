//
//  ex01_2739_구구단.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/06.
//

import Foundation

var line = readLine()
var number: Int
if line != nil && line != "" {
    number = Int(line!)!
}
else {
    print("NO INPUT")
    exit(1)
}
for i in 1...9 {
    print("\(number) * \(i) = \(number*i)")
}
