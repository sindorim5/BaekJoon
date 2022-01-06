//
//  ex03_8393_합.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/06.
//

import Foundation

var count = readLine()
var result: Int = 0
let countInt: Int

if count != nil && count != "" {
    countInt = Int(count!)!
}
else {
    print("NO INPUT")
    exit(1)
}

for i in 1...countInt {
    result = result + i
}
print(result)
