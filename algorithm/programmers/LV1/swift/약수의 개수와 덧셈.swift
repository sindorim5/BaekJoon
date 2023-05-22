//
//  약수의 개수와 덧셈.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/18.
//

import Foundation

func submultipleCount(_ num: Int) -> Int {
	var i: Int = 1
	var count: Int = 0
	
	while i <= num / i {
		if num % i == 0 {
			count += 1
		}
		i += 1
	}
	
	i -= 1
	
	if i * i == num {
		count = count * 2 - 1
	} else {
		count = count * 2
	}
	
	return count
}

func solution(_ left:Int, _ right:Int) -> Int {
	var result: Int = 0
	
	for i in left...right {
		if submultipleCount(i) % 2 == 0 {
			result += i
		} else {
			result -= i
		}
	}
	return result
}
