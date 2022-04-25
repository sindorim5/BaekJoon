//
//  문자열 내 p와 y의 개수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/23.
//

import Foundation

func solution(_ s:String) -> Bool
{
	var ans:Bool = false
	var countP: Int = 0
	var countY: Int = 0

	for char in s {
		if char == "p" || char == "P" { countP += 1 }
		else if char == "y" || char == "Y" { countY += 1 }
	}

	ans = countP == countY

	return ans
}
