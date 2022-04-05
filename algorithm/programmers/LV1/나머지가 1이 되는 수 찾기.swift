//
//  나머지가 1이 되는 수 찾기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/31.
//

import Foundation

func solution(_ n:Int) -> Int {
	var result = 0
	for i in 2..<n {
		if n % i == 1 {
			result = i
			break
		}
	}

	return result
}
