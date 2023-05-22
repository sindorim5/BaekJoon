//
//  ex06_8958_OX퀴즈.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

var count = Int(readLine()!)!

while (count > 0) {
    var line = readLine()!
    var array = Array(line)
    var point: Int = 0
    var total: Int = 0
    for i in 0..<array.count {
        if (array[i] == "O") {
            point += 1
            total += point
        }
        else { point = 0 }
    }
    count -= 1
    print(total)
}
