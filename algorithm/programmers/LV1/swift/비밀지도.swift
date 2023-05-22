//
//  비밀지도.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/04.
//

func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
	var binaryArray: [String] = []
	var answer: [String] = []

	for i in 0..<n {
		binaryArray.append(String(arr1[i] | arr2[i], radix: 2))
	}

	for i in binaryArray {
		var temp = ""
		var add = ""
		if i.count != n {
			for _ in 0..<n-i.count {
				temp += "0"
			}
		}
		temp += i
		for j in temp {
			add += j == "1" ? "#" : " "
		}
		answer.append(add)
	}
	return answer
}
