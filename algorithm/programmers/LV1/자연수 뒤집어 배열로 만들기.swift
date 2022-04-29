//
//  자연수 뒤집어 배열로 만들기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/26.
//

func solution(_ n:Int64) -> [Int] {
	var result: [Int] = []
	var n = Int(n)

	while (n > 0) {
		var i = n % 10
		n = n / 10
		result.append(i)
	}
	return result
}
