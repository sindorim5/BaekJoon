//
//  ex05_2741_N찍기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var count = readLine()
let countInt: Int
var result: Int = 1

if count != nil && count != "" {
    countInt = Int(count!)!
}
else {
    print("NO INPUT")
    exit(1)
}

for _ in 1...countInt {
    print(result)
    result += 1
}
