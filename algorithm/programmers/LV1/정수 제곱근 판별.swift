//
//  정수 제곱근 판별.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/26.
//

import Foundation

func solution(_ n:Int64) -> Int64 {
	let sqrtN = sqrt(Double(n))
	let temp = Int64(sqrtN)

	return temp * temp == n ? (temp + 1) * (temp + 1) : -1
}
