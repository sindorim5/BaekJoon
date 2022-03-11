//
//  신규 아이디 추천.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ new_id:String) -> String {

    var result: String = ""

    // 1단계
    let lowerNewId = new_id.lowercased()

    // 2단계
    for c in lowerNewId {
        if c.isLowercase || c.isNumber || c == "-" || c == "_" || c == "." {
            result = result + String(c)
        }
    }

    // 3단계
    while result.contains("..") {
        result = result.replacingOccurrences(of: "..", with: ".")
    }

    // 4단계
    if result.first == "." {
        result.removeFirst()
    }
    if result.last == "." {
        result.removeLast()
    }

    // 5단계
    if result.count == 0 {
        result = "a"
    }

    // 6단계
    if result.count >= 16 {
        let endIndex = result.index(result.startIndex, offsetBy: 14)
        result = String(result[result.startIndex ... endIndex])
        if result.hasSuffix(".") {
            result.removeLast()
        }
    }

    // 7단계
    if result.count <= 2 {
        while result.count < 3 {
            result = result + String(result.last!)
        }
    }

    return result
}
