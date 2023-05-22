//
//  ex09_2941_크로아티아알파벳.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/10.
//

import Foundation

var input = readLine()!
let dic = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in 0...dic.count - 1 {
    input = input.replacingOccurrences(of: dic[i], with: "1")
}
print(input.count)
