//
//  수식 최대화.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/06/01.
//

import Foundation

// 연산 순서를 순열 배열로 생성하는 함수
func permute(_ op: [String]) -> [[String]] {
	var result: [[String]] = []
	var visited = [Bool](repeating: false, count: 3)

	func permutation(_ nowPermute : [String]) {
		if nowPermute.count == 3 {
			result.append(nowPermute)
			return
		}
		for i in 0..<3 {
			if visited[i] == true {
				continue
			}
			else {
				visited[i] = true
				permutation(nowPermute + [op[i]])
				visited[i] = false
			}
		}
	}
	permutation([])
	return result
}

// String 배열을 연산 순서에 맞게 계산하는 함수
func calculate(_ numbers: [String], _ op: [String]) -> Int64 {
	var numbers = numbers

	for element in op {
		while (numbers.contains(element)) {
			// 연산 기호의 인덱스를 구하고 앞뒤의 수를 연산
			let index = numbers.firstIndex(of: element)!
			switch element {
				case "+":
					numbers[index - 1] = String(Int(numbers[index - 1])! + Int(numbers[index + 1])!)
				case "-":
					numbers[index - 1] = String(Int(numbers[index - 1])! - Int(numbers[index + 1])!)
				case "*":
					numbers[index - 1] = String(Int(numbers[index - 1])! * Int(numbers[index + 1])!)
				default:
					return 0
			}
			// 연산 결과는 앞의 인덱스로. 연산 기호와 그 다음 인덱스는 삭제
			numbers.remove(at: index + 1)
			numbers.remove(at: index)
		}
	}
	// 연산 결과의 절대값을 리턴
	return abs(Int64(numbers.first!)!)
}

func solution(_ expression:String) -> Int64 {
	let array = Array(expression)
	let opArray = ["*", "+", "-"]
	var numbers: [String] = []
	var temp = ""
	var result: [Int64] = []

	// 배열의 값을 숫자와 연산 기호의 배열로 바꾸기
	// temp를 [String]으로 했더니 시간 초과
	for i in array {
		if i >= "0" && i <= "9" {
			temp += String(i)
		} else {
			if !temp.isEmpty {
				numbers.append(temp)
				temp = ""
			}
			numbers.append(String(i))
		}
	}
	numbers.append(temp)
	let priority = permute(opArray)

	for op in priority {
		result.append(calculate(numbers, op))
	}

	// 우선순위에 맞게 계산된 결과값의 최대값을 리턴
	return result.max()!
}
