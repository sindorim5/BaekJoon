//
//  ex10_2439_별찍기2.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var count = readLine()

if count != nil && count != "" {
    let countInt = Int(count!)!
    for i in 1...countInt {
        for _ in 0..<(countInt - i) {
            print(" ", terminator: "")
        }
        for _ in 1...i {
            print("*", terminator: "")
        }
        print(" ")
    }
}
else {
    print("NO INPUT")
    exit(1)
}
