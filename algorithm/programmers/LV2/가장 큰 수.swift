//
//  가장 큰 수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/06/03.
//

import Foundation

func solution(_ numbers:[Int]) -> String {

	let sorted = numbers.sorted { Int("\($0)\($1)")! > Int("\($1)\($0)")! }

	if sorted.first == 0 {
		return "0"
	}
	let result = sorted.map { String ($0) }.joined()

	return result
}

// 순열로 푸는 문제가 아니었다.
