//
//  ex03_1193_분수찾기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

let input = Int(readLine()!)!
var numerator: Int = 1; var denominator: Int = 1
var checker: Int = 1

if (input > 1) {
    for _ in 2...input {
        numerator = numerator - checker
        denominator = denominator + checker
        if (numerator < 1) {
            numerator = 1
            checker *= -1
        }
        if (denominator < 1) {
            denominator = 1
            checker *= -1
        }
    }
}

print("\(numerator)/\(denominator)")
