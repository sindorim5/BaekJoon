//
//  문자열 압축.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/29.
//

import Foundation

func solution(_ s:String) -> Int {
	if s.count < 3 {
		return s.count
	}
	var result: Int = s.count

	for i in 1...s.count / 2 {
		let slicedStr = slice(s, i)
		let compressedStr = compress(slicedStr)
		let length = compressedStr.count
		if length < result {
			result = length
		}
	}
	return result
}

func slice(_ s: String, _ length: Int) -> [String] {
	var result: [String] = []
	var temp: String = ""

	for char in s {
		temp += String(char)
		if temp.count == length {
			result.append(temp)
			temp = ""
		}
	}
	if !temp.isEmpty {
		result.append(temp)
	}
	return result
}

func compress(_ strArray: [String]) -> String {
	var result: String = ""
	var temp: String = ""
	var count: Int = 1

	for str in strArray {
		if temp == str {
			count += 1
		} else {
			if !temp.isEmpty {
				result += count > 1 ? "\(count)\(temp)" : temp
			}
			temp = str
			count = 1
		}
	}
	if !temp.isEmpty {
		result += count > 1 ? "\(count)\(temp)" : temp
	}
	return result
}
