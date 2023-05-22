//
//  예산.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/18.
//

import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
	let dSort = d.sorted(by: <)
	var budgetSum = 0
	var result = 0
	
	for i in dSort {
		budgetSum += i
		if budgetSum > budget {
			break
		}
		result += 1
	}
	
	return result
}
