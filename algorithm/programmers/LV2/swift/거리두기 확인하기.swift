//
//  거리두기 확인하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/06/01.
//

import Foundation

typealias Tuple = (Int, Int)
typealias distance = (Tuple, Tuple, Int)

// 맨하튼 거리 구하기
func getDistance(_ a: Tuple, _ b: Tuple) -> Int {
	return abs(a.0 - b.0) + abs(a.1 - b.1)
}

// 각 좌표들의 조합과 좌표간의 거리를 구하는 함수
func combi(_ location: [Tuple]) -> [distance] {
	var result = [distance]()

	func combination(_ index: Int, _ nowCombi: [Tuple]) {
		if nowCombi.count == 2 {
			let a = nowCombi.first!
			let b = nowCombi.last!
			let dis = getDistance(a, b)
			result.append((a, b, dis))
			return
		}
		for i in index..<location.count {
			combination(i + 1, nowCombi + [location[i]])
		}
	}

	combination(0, [])

	return result
}

// 좌표간의 거리를 확인하여 참거짓을 판별하는 함수
func checkDistance(_ matrix: [[String]], _ x: Int) -> Bool {
	var location = [Tuple]()
	var distanceArray = [distance]()
	for i in x..<5 {
		for j in 0..<5 {
			if matrix[i][j] == "P" {
				location.append((i, j))
			}
		}
	}
	distanceArray = combi(location)
	for element in distanceArray {
		if element.2 == 1 { return false }
		else if element.2 == 2 {
			if element.0.0 == element.1.0 {
				if matrix[element.0.0][(element.0.1 + element.1.1) / 2] != "X" { return false }
			}
			else if element.0.1 == element.1.1 {
				if matrix[(element.0.0 + element.1.0) / 2][element.0.1] != "X" { return false }
			}
			else {
				if matrix[element.0.0][element.1.1] != "X" || matrix[element.1.0][element.0.1] != "X" { return false }
			}
		}
	}
	return true
}

func solution(_ places:[[String]]) -> [Int] {
	var result: [Int] = []
	for place in places {
		let matrix = place.map { $0.map { String($0) }}
		var exitForLoop = 0

		for x in 0..<5 {
			for y in 0..<5 {
				// 사람이 앉은 것으로 판명되면 거리두기 확인
				if matrix[x][y] == "P" {
					if checkDistance(matrix, x) { result.append(1) }
					else { result.append(0) }
					exitForLoop = 1
				}
				if exitForLoop == 1 { break }
			}
			if exitForLoop == 1 { break }
		}
		// 사람이 앉지 않은 경우
		if exitForLoop == 0 {
			result.append(1)
		}
	}
	return result
}
