//
//  실패율.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/18.
//

import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
	
	var stageArray = Array(repeating: 0.0, count: N+1)
	var failArray: [Double] = []
	var failRate: Double = 0.0
	var users = Double(stages.count)
	var result: [Int] = []
	
	for stage in stages {
		stageArray[stage - 1] += 1
	}
	
	for i in 0..<stageArray.count - 1 {
		if stageArray[i] == 0 {
			failRate = 0.0
		} else {
			failRate = Double(stageArray[i] / users)
		}
		users -= stageArray[i]
		failArray.append(failRate)
	}
	
	for i in failArray.sorted(by: >) {
		var index = failArray.firstIndex(where: { $0 == i })! + 1
		if result.contains(index) {
			for j in index..<failArray.count {
				if failArray[j] == i && !result.contains(j+1) {
					index = j + 1
					break
				}
			}
		}
		result.append(index)
	}
	
	return result
}
