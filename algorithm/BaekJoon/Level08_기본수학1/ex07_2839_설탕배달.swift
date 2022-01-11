//
//  ex07_2839_설탕배달.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

let input = Int(readLine()!)!
var X = input / 5
var Y = input % 5

while (X >= 0) {
    if (Y % 3 == 0) {
        Y = Y / 3
        break
    }
    else {
        X = X - 1
        Y = Y + 5
    }
}

if (5 * X + 3 * Y == input) {
    print(X+Y)
}
else {
    print("-1")
}
