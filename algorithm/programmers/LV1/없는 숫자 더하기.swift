//
//  없는 숫자 더하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ numbers:[Int]) -> Int {
    
    var zeroToNine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var result = 0
    for num in numbers {
        if zeroToNine.contains(num) {
            zeroToNine.removeAll(where: { $0 == num })
        }
    }
    result = zeroToNine.reduce(0) { $0 + $1 }
    
    return result
}
