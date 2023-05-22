//
//  최대공약수와 최소공배수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/26.
//

func solution(_ n:Int, _ m:Int) -> [Int] {
	let GCD_NUM = GCD(n, m)
	let LCM_NUM = n * m / GCD_NUM

	return [GCD_NUM, LCM_NUM]
}

func GCD(_ a:Int, _ b:Int) -> Int {
	let maxNum = max(a, b)
	let minNum = min(a, b)

	if (maxNum % minNum == 0) {
		return minNum
	} else {
		return GCD(minNum, maxNum % minNum)
	}
}
