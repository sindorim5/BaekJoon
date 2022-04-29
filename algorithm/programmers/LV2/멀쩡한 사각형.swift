//
//  멀쩡한 사각형.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/29.
//

import Foundation

import Foundation

func solution(_ w:Int, _ h:Int) -> Int64{
	var answer: Int64 = 0
	let x = Double(w)
	let y = Double(h)

	for i in 1..<w {
		let j = ceil(y / x * Double(i))
		answer += Int64(y - j)
	}

	return answer * 2
}

// func solution(_ w:Int, _ h:Int) -> Int64{
//     var answer: Int64 = 0

// 	answer = Int64(w * h) - Int64(w + h - gcd(w, h))

//     return answer
// }

// func gcd(_ a: Int, _ b: Int) -> Int {
// 	let maxNum = max(a, b)
// 	let minNum = min(a, b)

// 	if minNum == 0 {
// 		return Int(maxNum)
// 	} else {
// 		return gcd(minNum, maxNum % minNum)
// 	}
// }
