//
//  ex04_2675_문자열반복.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

let num = Int(readLine()!)!

for _ in 1...num {
    let input = readLine()!
    var sArray: [String] = []
    let repeatNum = input.split(separator: " ")[0]
    sArray = input.split(separator: " ")[1].map{ String($0) }
    
    for c in sArray {
        for _ in 1...Int(repeatNum)! {
            print(c, terminator: "")
        }
    }
    print("")
}
