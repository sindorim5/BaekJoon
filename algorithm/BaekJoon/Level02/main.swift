//
//  main.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var line = readLine()
var H,M: Int
var array: [String] = []
if line != nil && line != "" {
    array = line!.components(separatedBy: " ")
    H = Int(array[0])!
    M = Int(array[1])!
}
else {
    print("NO INPUT")
    exit(1)
}

if ((M-45)<0) {
    if (H == 0) { H = 23 }
    else { H -= 1 }
    M = M + 15
}
else {
    M = M - 45
}
print(H,M)

