//
//  다트 게임.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/04.
//

func solution(_ dartResult:String) -> Int {
	var num: [Int] = [0, 0, 0]
	var bonus: [Int] = [1, 1, 1]
	var result: Int = 0
	var index: Int = 0
	var temp: Character = " "

	for c in dartResult {
		switch c {
			case "0"..."9":
				if temp == "1" && c == "0" {
					num[index - 1] = 10
				} else {
					num[index] = Int(String(c)) ?? 0
					index += 1
				}
			case "S":
				num[index - 1] = num[index - 1]
			case "D":
				num[index - 1] = num[index - 1] * num[index - 1]
			case "T":
				num[index - 1] = num[index - 1] * num[index - 1] * num[index - 1]
			case "*":
				bonus[index - 1] *= 2
				if index > 1 {
					bonus[index - 2] *= 2
				}
			case "#":
				bonus[index - 1] *= -1
			default:
				break
		}
		temp = c
	}

	for i in 0..<3 {
		let add = num[i] * bonus[i]
		result += add
	}
	return result
}
