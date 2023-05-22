//
//  ex04_14681_사분면 고르기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var input1 = readLine()
var input2 = readLine()
var x, y: Int

if (input1 != nil && input1 != "") && (input2 != nil && input2 != ""){
    x = Int(input1!)!
    y = Int(input2!)!
}
else {
    print("NO INPUT")
    exit(1)
}

if (x > 0 && y > 0) {
    print("1")
}
else if (x < 0 && y > 0) {
    print("2")
}
else if (x < 0 && y < 0) {
    print("3")
}
else if (x > 0 && y < 0) {
    print("4")
}
