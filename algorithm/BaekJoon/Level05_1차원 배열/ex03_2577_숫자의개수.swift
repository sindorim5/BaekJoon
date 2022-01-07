//
//  ex03_2577_숫자의개수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var D: Int = 1
var result = [Int](repeating: 0, count: 10)

for _ in 0..<3 {
    let input = Int(readLine()!)!
    D = input * D
}

while D > 0 {
    let i = D % 10
    result[i] += 1
    D /= 10
}

result.forEach {print($0)}
