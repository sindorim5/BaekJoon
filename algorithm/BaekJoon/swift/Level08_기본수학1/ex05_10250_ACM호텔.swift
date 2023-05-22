//
//  ex05_10250_ACM호텔.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

let testCase = Int(readLine()!)!

for _ in 1...testCase {
    var array: [Int] = []
    array = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let H = array[0]; let W = array[1]; let N = array[2]
    var floor: Int; var ho: Int
    
    floor = N % H
    ho = N / H + 1
    if (floor == 0) {
        floor = H
        ho = N / H
    }
    
    if (ho < 10) {
        print("\(floor)0\(ho)")
    }
    else {
        print("\(floor)\(ho)")
    }
}
