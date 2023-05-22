//
//  3진법 뒤집기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/18.
//

import Foundation

func solution(_ n:Int) -> Int {
	var nCopy = n
	var array: [Int] = []
	var result = 0
	var i = 1
	
	while nCopy > 0 {
		let num = nCopy % 3
		array.insert(num, at: 0)
		nCopy /= 3
	}
	
	for element in array {
		result += element * i
		i *= 3
	}

	return result
}
