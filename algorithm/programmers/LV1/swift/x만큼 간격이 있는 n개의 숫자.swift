//
//  x만큼 간격이 있는 n개의 숫자.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/29.
//

func solution(_ x:Int, _ n:Int) -> [Int64] {
	var result: [Int64] = []

	for i in 1...n {
		result.append(Int64(x * i))
	}

	return result
}
