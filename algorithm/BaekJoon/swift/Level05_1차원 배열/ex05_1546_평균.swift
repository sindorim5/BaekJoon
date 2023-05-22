//
//  ex05_1546_평균.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

let count = Double(readLine()!)!
var array: [Double] = []

array = readLine()!.split(separator: " ").map{ Double($0)! }
let maxValue = array.max()
var changed = array.map{ ($0 / maxValue!) * 100 }
var total = changed.reduce(0, +)
print(total/count)
