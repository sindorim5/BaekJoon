//
//  숫자 문자열과 영단어.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ s:String) -> Int {
    
    var result = s
    
    result = result.replacingOccurrences(of: "zero", with: "0")
    result = result.replacingOccurrences(of: "one", with: "1")
    result = result.replacingOccurrences(of: "two", with: "2")
    result = result.replacingOccurrences(of: "three", with: "3")
    result = result.replacingOccurrences(of: "four", with: "4")
    result = result.replacingOccurrences(of: "five", with: "5")
    result = result.replacingOccurrences(of: "six", with: "6")
    result = result.replacingOccurrences(of: "seven", with: "7")
    result = result.replacingOccurrences(of: "eight", with: "8")
    result = result.replacingOccurrences(of: "nine", with: "9")

    return Int(result)!
}
