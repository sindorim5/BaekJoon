//
//  ex07_4344_평균은넘겠지.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

import Foundation

var C = Int(readLine()!)!

while (C > 0) {
    var line = readLine()!.split(separator: " ").map{ Double($0)! }
    let member = Double(line[0])
    line.remove(at: 0)
    let total = line.reduce(0, +)
    let avg = total/member
    let result = round(Double(line.filter{ $0 > avg }.count) / member * 100 * 1000) / 1000
    let resultString = String(format: "%.3f", result)
    print("\(resultString)%")
    C -= 1
}
