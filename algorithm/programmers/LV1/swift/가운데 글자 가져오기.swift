//
//  가운데 글자 가져오기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/31.
//

func solution(_ s:String) -> String {
	var result: String = ""

	if s.count % 2 == 1 {
		result = String(Array(s)[s.count/2])
	} else {
		result = String(Array(s)[s.count/2 - 1 ... s.count/2])
	}

	return result
}
