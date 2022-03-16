//
//  모의고사.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/16.
//

import Foundation

func solution(_ answers:[Int]) -> [Int] {
	let array1 = [1, 2, 3, 4 ,5]
	let array2 = [2, 1, 2, 3, 2, 4, 2, 5]
	let array3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	
	var count = Array(repeating: 0, count: 3)
	var result: [Int] = []
	
	for i in 0..<answers.count {
		if answers[i] == array1[i % array1.count] {
			count[0] += 1
		}
		if answers[i] == array2[i % array2.count] {
			count[1] += 1
		}
		if answers[i] == array3[i % array3.count] {
			count[2] += 1
		}
	}
	let maxValue = count.max()
	
	result = count.indices.filter { count[$0] == maxValue }.map { $0 + 1 }
		
	return result
}
