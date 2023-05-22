//
//  ex03_1065_한수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

let input = Int(readLine()!)!

func hansu(number: Int) -> Int {
    var hansuCount: Int = 0
    if (number >= 1 && number < 100) {
        hansuCount = number
    }
    else if (number >= 100 && number < 1000) {
        hansuCount = 99
        for i in 100...number {
            var temp = i
            var array: [Int] = []
            for _ in 1...3 {
                array.append(temp % 10)
                temp /= 10
            }
            if (array[0] - array[1] == array[1] - array[2]) { hansuCount += 1 }
        }
    }
    else if (number == 1000) {
        hansuCount = hansu(number: 999)
    }
    
    return hansuCount
}

print(hansu(number: input))
