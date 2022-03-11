//
//  로또의 최고 순위와 최저 순위.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var match = 0
    let zeroNum = lottos.filter{ $0 == 0 }.count
    
    lottos.forEach { num in
        if win_nums.contains(num) {
            match += 1
        }
    }
    var highestRank: Int = 0
    if zeroNum == 0 && match == 0 {
        highestRank = 6
    } else {
        highestRank = 7 - (zeroNum + match)
    }
    let lowestRank = match <= 1 ? 6 : 7 - match
    
    return [highestRank, lowestRank]
}
