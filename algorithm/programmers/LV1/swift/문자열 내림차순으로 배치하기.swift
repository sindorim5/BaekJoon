//
//  문자열 내림차순으로 배치하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/23.
//

func solution(_ s:String) -> String {
	let sortedString = s.sorted(by: >)
	return String(sortedString)
}
