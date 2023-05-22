//
//  두 정수 사이의 합.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/04.
//

func solution(_ a:Int, _ b:Int) -> Int64 {
	if a == b {
		return Int64(a)
	}
	let maxNum = max(a, b)
	let minNum = min(a, b)
	var result: Int = 0

	for i in minNum...maxNum {
		result += i
	}

	return Int64(result)
}
