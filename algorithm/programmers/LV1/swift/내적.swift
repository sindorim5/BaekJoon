//
//  내적.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result = 0
    
    for i in 0..<a.count{
        result += a[i] * b[i]
    }
    
    return result
}
