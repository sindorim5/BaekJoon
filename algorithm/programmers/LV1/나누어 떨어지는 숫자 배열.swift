//
//  나누어 떨어지는 숫자 배열.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/04.
//

func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
	var result: [Int] = []

	for i in arr {
		if i % divisor == 0 {
			result.append(i)
		}
	}

	if result.isEmpty {
		result.append(-1)
	}

	return result.sorted()
}
