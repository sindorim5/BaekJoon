//
//  ex06_1152_단어의개수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

let input = readLine()!
var array: [String] = []

array = input.split(separator: " ").map{String($0)}

print(array.count)
