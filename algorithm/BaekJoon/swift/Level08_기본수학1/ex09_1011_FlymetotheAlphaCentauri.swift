//
//  ex09_1011_FlymetotheAlphaCentauri.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

let testCase = Int(readLine()!)!

for _ in 1...testCase {
    let input = readLine()!
    let array = input.split(separator: " ").map{ Int(String($0))! }
    let distance = array[1] - array[0]
    var count: Int = 0
    
    while (true) {
        if distance <= count * (count + 1) {
            break
        }
        count += 1
        
    }
    if (distance <= count * count) {
        print(count * 2 - 1)
    }
    else {
        print(count * 2)
    }
}
