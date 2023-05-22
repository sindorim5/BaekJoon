//
//  평균 구하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/28.
//

func solution(_ arr:[Int]) -> Double {
    let sum = arr.reduce(0, +)
    return Double(sum) / Double(arr.count)
}
