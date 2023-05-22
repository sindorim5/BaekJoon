//
//  시저 암호.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/25.
//

func solution(_ s:String, _ n:Int) -> String {
	let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	var result = ""

	for char in s {
		let isUppercase = char.isUppercase

		if alphabet.contains(char.lowercased()) {
			let firstIndex = alphabet.firstIndex(where: { $0 == char.lowercased()}) ?? 0
			let index = (firstIndex + n) % 26
			if isUppercase {
				result += alphabet[index].uppercased()
			} else {
				result += alphabet[index]
			}
		} else {
			result += " "
		}
	}
	return result
}
