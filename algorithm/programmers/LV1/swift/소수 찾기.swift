//
//  소수 찾기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/23.
//

import Foundation

func solution(_ n: Int) -> Int {
	var count = 0

	for i in 2...n {
		if isPrimeNumber(Double(i)) {
			count += 1
		}
	}
	return count
}

func isPrimeNumber(_ num: Double) -> Bool {
	var i: Double = 2
	if (num < 2) {
		return true
	}
	while (i <= sqrt(num)) {
		if (Int(num) % Int(i) == 0) {
			return false
		}
		i += 1
	}
	return true
}
