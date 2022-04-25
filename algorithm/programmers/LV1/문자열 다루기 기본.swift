//
//  문자열 다루기 기본.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/23.
//

func solution(_ s:String) -> Bool {
    if s.count == 4 || s.count == 6 {
        if Int(s) != nil {
            return true
        }
    }
    return false
}
