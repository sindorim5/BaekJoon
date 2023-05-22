//
//  정수 내림차순으로 배치하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/26.
//

func solution(_ n:Int64) -> Int64 {
	var array: [Int64] = []
	var result: Int64 = 0
	var n: Int64 = n

	while (n > 0) {
		var i = n % 10
		n = n / 10
		array.append(i)
	}

	result = array.sorted(by: >).reduce(0) { $0 * 10 + $1 }
	return result
}

// func solution(_ n:Int64) -> Int64 {
//     return Int64(String(Array(String(n)).sorted { $0 > $1 }))!
// }
