//
//  ex08_10757_큰수A+B.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

let input = readLine()!
var array = input.split(separator: " ")

var X = array[0].map{ Int(String($0))! }
var Y = array[1].map{ Int(String($0))! }

let zeros = X.count - Y.count
if (zeros > 0) {
    for _ in 0..<zeros {
        Y.insert(0, at: Y.startIndex)
    }
}
else if (zeros < 0) {
    for _ in 0..<abs(zeros) {
        X.insert(0, at: X.startIndex)
    }
}
var Z = Array(repeating: 0, count: X.count)

for i in 0..<X.count {
    Z[i] = X[i] + Y[i]
}

for i in (0..<X.count).reversed() {
    if (Z[i] >= 10) && (i != 0) {
        Z[i - 1] += 1
        Z[i] %= 10
    }
    else if (Z[i] >= 10) && (i == 0) {
        Z[i] %= 10
        Z.insert(1, at: Z.startIndex)
    }
}

var result = Z.map{ String($0) }.joined(separator: "")

print(result)
