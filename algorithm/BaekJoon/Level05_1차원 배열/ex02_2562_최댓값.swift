//
//  ex02_2562_최댓값.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var array: [Int] = []

for _ in 1...9 {
    var number = Int(readLine()!)!
    array.append(number)
}

print(array.max()!)
print(array.firstIndex(of: array.max()!)!+1)
