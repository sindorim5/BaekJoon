//
//  ex02_2292_벌집.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

let input = Int(readLine()!)!
var index: Int = 0
var rangeNum: Int = 1


while (rangeNum <= input) {
    if (index == 0) { rangeNum = 1 }
    else if (index == 1) { rangeNum = 2 }
    else {
        rangeNum = 6 * (index - 1) + rangeNum
    }
    index += 1
}
print(index - 1)
