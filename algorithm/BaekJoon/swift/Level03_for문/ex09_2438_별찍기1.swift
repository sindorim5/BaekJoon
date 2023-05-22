//
//  ex09_2438_별찍기1.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var count = readLine()

if count != nil && count != "" {
    let countInt = Int(count!)!
    for i in 1...countInt {
        for j in 1...i{
            print("*", terminator: "")
        }
        print(" ")
    }
}
else {
    print("NO INPUT")
    exit(1)
}
