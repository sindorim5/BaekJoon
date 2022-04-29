//
//  행렬의 덧셈.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/29.
//

func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
	var result = arr1

	for i in 0..<arr1.count {
		for j in 0..<arr1[i].count {
			result[i][j] += arr2[i][j]
		}
	}
	return result
}
