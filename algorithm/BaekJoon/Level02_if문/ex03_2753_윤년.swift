//
//  ex03_2753_윤년.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var line = readLine()
var year: Int
if line != nil && line != "" {
    year = Int(line!)!
}
else {
    print("NO INPUT")
    exit(1)
}

if (year % 4 == 0) && (year % 100 != 0){
    print("1")
}
else if (year % 400 == 0) {
    print("1")
}
else {
    print("0")
}
