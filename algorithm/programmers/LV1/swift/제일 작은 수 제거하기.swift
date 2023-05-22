//
//  제일 작은 수 제거하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/26.
//

func solution(_ arr:[Int]) -> [Int] {
	var result = arr
	result.remove(at: arr.firstIndex(of: arr.min()!)!)

	return result.isEmpty ? [-1] : result
}

