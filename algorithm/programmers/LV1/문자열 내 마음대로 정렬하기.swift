//
//  문자열 내 마음대로 정렬하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/04.
//

func solution(_ strings:[String], _ n:Int) -> [String] {
    var result: [String] = []
    let index = strings[0].index(strings[0].startIndex, offsetBy: n)

    result = strings.sorted(by: {(s1: String, s2: String) -> Bool in
        if s1[index] == s2[index] {
            return s1 < s2
        } else {
            return s1[index] < s2[index]
        }
    })

    return result
}
