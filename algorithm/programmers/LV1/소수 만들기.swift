//
//  소수 만들기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/16.
//

import Foundation

func solution(_ nums:[Int]) -> Int {
	var answer = 0
	var sum = 0
		
	// 3개 뽑아 더하기
	for i in 0..<nums.count-2 {
		for j in i+1..<nums.count-1 {
			for k in j+1..<nums.count {
				sum = nums[i] + nums[j] + nums[k]
				if isPrimeNumber(sum) == true {
					answer += 1
				}
			}
		}
	}
	return answer
}

func isPrimeNumber(_ num: Int) -> Bool {
	var i: Int = 2
	if (num < 2) {
		return true
	}
	while (i <= (num / i)) {
		if (num % i == 0) {
			return false
		}
		i += 1
	}
	return true
}
