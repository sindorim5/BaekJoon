//
//  이상한 문자 만들기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/25.
//

import Foundation

func solution(_ s:String) -> String {
	var array: [String] = []
	var result = ""
	var index = 0
	for char in s {
		if index % 2 == 0 {
			array.append(String(char.uppercased()))
		} else {
			array.append(String(char.lowercased()))
		}
		index += 1
		if char == " " {
			index = 0
		}
	}
	result = array.joined()
	return result
}
