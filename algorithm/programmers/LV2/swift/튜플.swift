//
//  튜플.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/06/01.
//

import Foundation

func solution(_ s:String) -> [Int] {
	var result: [Int] = []
	var data: [[Int]] = []
	var temp: [Int] = []
	var tempString = ""
	var sArray = Array(s)

	sArray.removeFirst()
	sArray.removeLast()

	for i in sArray {
		switch i {
			case "{":
				temp = []
				tempString = ""
			case ",":
				temp.append(Int(tempString)!)
				tempString = ""
			case "}":
				temp.append(Int(tempString)!)
				data.append(temp)
			default:
				tempString += String(i)
		}
	}

	data.sort { $0.count < $1.count }

	for array in data {
		for element in array {
			if !result.contains(element) {
				result.append(element)
			}
		}
	}

	return result
}
