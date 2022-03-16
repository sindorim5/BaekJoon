//
//  K번째수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/16.
//

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
	var answer: [Int] = []
	for arr in commands {
		let startIndex = arr[0] - 1
		let endIndex = arr[1] - 1
		let findIndex = arr[2] - 1
		
		let newArray = array[startIndex...endIndex].sorted()
		answer.append(newArray[findIndex])
	}
	
	return answer
}
