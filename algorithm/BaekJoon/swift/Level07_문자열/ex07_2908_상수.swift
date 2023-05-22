//
//  ex07_2908_상수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

let input = readLine()!
var array: [Int] = []

array = input.split(separator: " ").map{ Int(String($0))! }

func reverseNumber(number: Int) -> Int{
    var result, digit: Int
    var temp = number
    var revArray: [Int] = []
    while (temp > 0) {
        digit = temp % 10
        revArray.append(digit)
        temp /= 10
    }
    result = revArray[0] * 100 + revArray[1] * 10 + revArray[2]
    return result
}

print(max((reverseNumber(number: array[0])),(reverseNumber(number: array[1]))))
