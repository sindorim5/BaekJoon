//
//  직사각형 별찍기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/29.
//

import Foundation

let input = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (n, m) = (input[0], input[1])
var line = ""

for _ in 1...n {
	line += "*"
}

for _ in 1...m {
	print(line)
}
