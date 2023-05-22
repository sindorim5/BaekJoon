//
//  최소직사각형.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/31.
//

import Foundation

func solution(_ sizes:[[Int]]) -> Int {
	var newSizes: [[Int]] = []
	var maxWidth: Int = 0
	var maxHeight: Int = 0
	for size in sizes {
		newSizes.append(swapSize(size))
	}
	for size in newSizes {
		if size[0] > maxWidth {
			maxWidth = size[0]
		}
		if size[1] > maxHeight {
			maxHeight = size[1]
		}
	}
	return (maxWidth * maxHeight)
}

func swapSize(_ numbers:[Int]) -> [Int] {
	var result = numbers
	if numbers[0] < numbers[1] {
		result[0] = numbers[1]
		result[1] = numbers[0]
	}
	return result
}
