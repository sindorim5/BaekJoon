//
//  ex02_10950_A+B - 3.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/06.
//

import Foundation

var count = readLine()

if count != nil && count != "" {
    let countInt = Int(count!)!
    for i in 1...countInt {
        var line = readLine()
        var array: [String] = []
        if line != nil && line != "" {
            array = line!.components(separatedBy: " ")
            let a = Int(array[0])!
            let b = Int(array[1])!
            print(a+b)
        }
        else {
            print("NO INPUT")
            exit(1)
        }
    }
}
else {
    print("NO INPUT")
    exit(1)
}
