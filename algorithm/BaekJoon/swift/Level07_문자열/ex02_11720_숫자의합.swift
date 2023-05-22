//
//  ex02_11720_숫자의합.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

let input1 = readLine()
let input2 = readLine()
var array: [Int] = []

array = (input2?.map{ Int(String($0))! })!

print(array.reduce(0, +))
