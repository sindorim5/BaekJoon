//
//  ex08_1008_A:B.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var line = readLine()
var array: [String] = []
if line != nil && line != "" {
    array = line!.components(separatedBy: " ")
    let a = Double(array[0])!
    let b = Double(array[1])!
    print(a/b)
    exit(0)
}
else {
    print("NO INPUT")
    exit(1)
}
