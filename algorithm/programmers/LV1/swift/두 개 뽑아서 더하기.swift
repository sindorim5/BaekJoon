//
//  두 개 뽑아서 더하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/19.
//

import Foundation

func solution(_ numbers:[Int]) -> [Int] {
	var result = Set<Int>()

	for i in 0..<numbers.count {
		for j in i+1..<numbers.count {
			var sum = numbers[i] + numbers[j]
			result.insert(sum)
		}
	}

	return Array(result).sorted(by: <)
}
