//
//  자릿수 더하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/26.
//

import Foundation

func solution(_ n:Int) -> Int
{
	var answer:Int = 0
	var n: Int = n
	while (n > 0) {
		var i = n % 10
		n = n / 10
		answer += i
	}

	return answer
}
