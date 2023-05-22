//
//  소수 찾기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/06/03.
//

import Foundation

// 순열로 숫자 조합 후 중복 제거를 위해 세트로 저장
func permute(_ array: [String], _ targetNumber: Int) -> Set<Int> {
	var result = Set<Int>()
	var visited = [Bool](repeating: false, count: array.count)

	func permutation(_ nowPermute: [String]) {
		if nowPermute.count == targetNumber {
			let temp = Int(nowPermute.joined())!
			result.insert(temp)
			return
		}
		for i in 0..<array.count {
			if visited[i] == true {
				continue
			} else {
				visited[i] = true
				permutation(nowPermute  + [array[i]])
				visited[i] = false
			}
		}
	}

	permutation([])

	return result
}

// 소수 판별
func isPrimeNumber(_ a: Int) -> Bool {
	if a <= 1 {
		return false
	}
	if a == 2 {
		return true
	}
	var i = 2
	while i <= (a / i) {
		if a % i == 0 {
			return false
		}
		i += 1
	}
	return true
}

func solution(_ numbers:String) -> Int {
	var count = 0
	let array = Array(numbers).map { String($0) }
	let arrayInt = array.map { Int($0)! }
	var setA = Set(arrayInt)

	// i 자리 수의 숫자세트를 만들고 합집합
	for i in 2...array.count {
		let tempSet = permute(array, i)
		setA = tempSet.union(setA)
	}

	for i in setA {
		if isPrimeNumber(i) {
			count += 1
		}
	}

	return count
}
