//
//  키패드 누르기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var result: String = ""
    var left: Int = 10  // 왼손위치
    var right: Int = 12 // 오른손위치
    
    for i in numbers {
        if i == 1 || i == 4 || i == 7 {
            result = result + "L"
            left = i
        } else if i == 3 || i == 6 || i == 9 {
            result = result + "R"
            right = i
        } else {
            var tmp = 0
            if i == 0 {
                tmp = 11
            } else {
                tmp = i
            }
            let diffL = abs(tmp - left)
            let diffR = abs(tmp - right)
            let distanceL = diffL / 3 + diffL % 3
            let distanceR = diffR / 3 + diffR % 3
            if distanceL < distanceR {
                result = result + "L"
                left = tmp
            } else if distanceL > distanceR {
                result = result + "R"
                right = tmp
            } else {
                result = hand == "left" ? result + "L" : result + "R"
                if result.last == "L" {
                    left = tmp
                } else {
                    right = tmp
                }
            }
        }
    }
    return result
}
