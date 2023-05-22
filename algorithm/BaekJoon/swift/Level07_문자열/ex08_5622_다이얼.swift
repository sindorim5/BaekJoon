//
//  ex08_5622_다이얼.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/10.
//

let input = readLine()!
var array: [Int] = []

for c in input {
    if ["A", "B", "C"].contains(c) { array.append(3) }
    else if ["D", "E", "F"].contains(c) { array.append(4) }
    else if ["G", "H", "I"].contains(c) { array.append(5) }
    else if ["J", "K", "L"].contains(c) { array.append(6) }
    else if ["M", "N", "O"].contains(c) { array.append(7) }
    else if ["P", "Q", "R", "S"].contains(c) { array.append(8) }
    else if ["T", "U", "V"].contains(c) { array.append(9) }
    else if ["W", "X", "Y", "Z"].contains(c) { array.append(10) }
}

print(array.reduce(0, +))
