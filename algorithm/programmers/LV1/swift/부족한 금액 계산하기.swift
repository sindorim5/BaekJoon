//
//  부족한 금액 계산하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/31.
//

import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
	var answer: Int64 = -1
	var sum = 0
	for i in 1...count {
		sum += price * i
	}

	answer = Int64(money - sum)

	if answer < 0 {
		answer *= -1
	} else {
		answer = 0
	}

	return answer
}
