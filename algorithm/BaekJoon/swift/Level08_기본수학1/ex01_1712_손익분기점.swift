//
//  ex01_1712_손익분기점.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/10.
//

let input = readLine()!
let array = input.split(separator: " ").map{ Int(String($0))! }

let valid = array[2] - array[1]

if (valid > 0 ) {
    print(array[0] / valid + 1)
}
else {
    print(-1)
}
