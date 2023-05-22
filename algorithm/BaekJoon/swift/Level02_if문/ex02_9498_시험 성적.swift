//
//  ex02_9498_시험 성적.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var line = readLine()
var score: Int
if line != nil && line != "" {
    score = Int(line!)!
}
else {
    print("NO INPUT")
    exit(1)
}

if (score >= 90 && score <= 100) {
    print("A")
}
else if (score >= 80 && score <= 89) {
    print("B")
}
else if (score >= 70 && score <= 79) {
    print("C")
}
else if (score >= 60 && score <= 69) {
    print("D")
}
else {
    print("F")
}
