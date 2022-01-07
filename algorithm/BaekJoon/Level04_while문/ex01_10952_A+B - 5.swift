//
//  ex01_10952_A+B - 5.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var array: [Int] = []
var endLine = "0 0"

while (true) {
    var line = readLine()
    if line == endLine { break }
    array = line!.split(separator: " ").map{ Int(($0))! }
    print(array[0]+array[1])
}
