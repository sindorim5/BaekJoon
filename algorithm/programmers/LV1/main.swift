//
//  main.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

func solution(_ id_list: [String], _ report: [String], _ k: Int) -> [Int] {
    
    var idDict: [String: Int] = [:]
    var reportDict: [String: Set<String>] = [:]
    var resultArray = Array(repeating: 0, count: id_list.count)
    
    for (i,id) in id_list.enumerated() {
        idDict[id] = i
    }

    for element in report {
        let splitReport = element.split(separator: " ")
        let reporter = String(splitReport[0])   // 신고자
        let reported = String(splitReport[1])   // 피신고자
        
        // 피신고자 : [신고자]
        if reportDict[reported] == nil {
            reportDict[reported] = [reporter]
        } else {
            reportDict[reported]?.insert(reporter)
        }
    }

    for reported in reportDict {
        if reported.value.count >= k {
            for reporter in reported.value {
                resultArray[idDict[reporter]!] += 1
            }
        }
    }
    
    return resultArray
}
