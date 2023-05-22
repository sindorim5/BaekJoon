//
//  ex05_1157_단어공부.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

let input = readLine()!
var inputUpper = input.uppercased()
var dic = [String : Int]()
var result: [String] = []

inputUpper.forEach {
    if (dic[String($0)] == nil) {
        dic[String($0)] = 1
    }
    else {
        dic[String($0)]! += 1
    }
}

for key in dic.keys {
    if dic[key] == dic.values.max() {
        result.append(key)
    }
}

if (result.count == 1) {
    print(result[0])
}
else {
    print("?")
}
