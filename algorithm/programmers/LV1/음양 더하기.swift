//
//  음양 더하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/11.
//

import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
	var sign = 1
	var result = 0
	
	for i in 0..<absolutes.count {
		if signs[i] == true {
			sign = 1
		} else {
			sign = -1
		}
		result = result + absolutes[i] * sign
	}
	
	return result
}
