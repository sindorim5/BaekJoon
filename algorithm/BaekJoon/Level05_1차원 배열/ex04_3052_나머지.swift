//
//  ex04_3052_나머지.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var array: [Int] = []
var count: Int = 10

for _ in 0...9 {
    array.append(Int(readLine()!)! % 42)
}
for i in 0..<9 {
    for j in (i+1)...9 {
        if (array[i] == array[j]) {
            count -= 1
            break
        }
    }
}
print(count)
