//
//  콜라츠 추측.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/28.
//

func solution(_ num:Int) -> Int {
	var num = num
	var count = 0

	while (num != 1 && count < 500) {
		if odd(num) {
			num = num * 3 + 1
		} else {
			num = num / 2
		}
		count += 1
	}
	return num == 1 ? count : -1
}

func odd(_ num: Int) -> Bool {
	return num % 2 == 0 ? false : true
}
