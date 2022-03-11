//
//  크레인 인형뽑기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var result: [Int] = []
    var count: Int = 0
    let newMoves = moves.map { $0 - 1 }
    var newBoard = board
    for i in newMoves {
        for j in 0..<newBoard.count {
            if newBoard[j][i] != 0 {
                if result.last == newBoard[j][i] {
                    count += 2
                    result.removeLast()
                } else {
                    result.append(newBoard[j][i])
                }
                newBoard[j][i] = 0
                break
            }
        }
    }
    
    return count
}
