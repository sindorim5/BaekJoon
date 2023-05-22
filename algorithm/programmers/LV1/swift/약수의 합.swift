//
//  약수의 합.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/25.
//

import Foundation

func solution(_ n:Int) -> Int {
	var i: Double = 1
	let doubleN: Double = Double(n)
	var result = 0

	while (i <= sqrt(doubleN)) {
		if (n % Int(i) == 0) {
			result += Int(i) + n / Int(i)
			print(result)
		}
		i += 1
	}

	i = i - 1

	if (i * i == Double(n)) {
		result -= Int(i)
	}

	return result
}
