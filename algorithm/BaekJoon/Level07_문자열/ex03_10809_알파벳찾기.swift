//
//  ex03_10809_알파벳찾기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

let S = readLine()
let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
var sArray: [String] = []

sArray = (S?.map{ String($0) })!

for i in 0...25 {
    if sArray.contains(alphabet[i]) {
        print(sArray.firstIndex(of: alphabet[i])!, terminator: " ")
    }
    else {
        print("-1", terminator: " ")
    }
}
