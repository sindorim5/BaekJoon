//
//  ex11_10871_X보다 작은수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var count = readLine()
var line = readLine()
var array: [String] = []
var arrayInt: [Int] = []
var X: Int


if count != nil && count != "" {
    array = count!.components(separatedBy: " ")
    X = Int(array[1])!
}
else {
    print("NO INPUT")
    exit(1)
}
if line != nil && line != "" {
    arrayInt = line!.split(separator: " ").map{ Int(String($0))! }.filter{($0 < X)}
}
else {
    print("NO INPUT")
    exit(1)
}
for i in 0..<arrayInt.count {
    print(arrayInt[i], terminator: " ")
}
