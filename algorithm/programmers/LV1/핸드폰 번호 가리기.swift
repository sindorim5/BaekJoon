//
//  핸드폰 번호 가리기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/29.
//

func solution(_ phone_number:String) -> String {
  return String(repeating: "*", count: phone_number.count - 4) + phone_number.suffix(4)
}

// func solution(_ phone_number:String) -> String {
// 	guard phone_number.count > 4 else {
// 		return phone_number
// 	}
// 	var star: String = ""
// 	var number: String = ""

// 	for _ in 1...phone_number.count - 4 {
// 		star += "*"
// 	}
// 	let index = phone_number.index(phone_number.endIndex, offsetBy: -4)
// 	number = String(phone_number[index..<phone_number.endIndex])

// 	return star + number
// }
