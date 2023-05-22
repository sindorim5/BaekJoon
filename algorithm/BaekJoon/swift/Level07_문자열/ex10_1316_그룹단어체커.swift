//
//  ex10_1316_그룹단어체커.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/10.
//

let N = Int(readLine()!)!
var count: Int = 0

for _ in 0..<N {
    let input = readLine()!
    var dic: [Character] = []
    
    for c in input {
        if !dic.contains(c) {
            dic.append(c)
        }
        else if dic.last != c {
            dic.removeAll()
            break
        }
    }
    if dic.count != 0 {
        count += 1
    }
}
print(count)
