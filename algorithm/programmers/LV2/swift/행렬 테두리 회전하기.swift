//
//  행렬 테두리 회전하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/05/30.
//

import Foundation

func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {

	var matrix = [[Int]]()
	var answer = [Int]()
	for r in 0..<rows {
		matrix.append(Array(r * columns + 1...r * columns + columns))
	}

	for q in queries {
		let minY = q[0] - 1
		let minX = q[1] - 1
		let maxY = q[2] - 1
		let maxX = q[3] - 1

		let firstValue = matrix[minY][minX]
		var minNum = firstValue

		//좌상단에서 하단으로 가면서 아래쪽 수를 위로 올림
		for y in minY..<maxY {
			minNum = min(matrix[y+1][minX], minNum)
			matrix[y][minX] = matrix[y+1][minX]
		}
		//좌하단에서부터 오른쪽으로 가며 오른쪽 수를 왼쪽으로
		for x in minX..<maxX {
			minNum = min(matrix[maxY][x+1], minNum)
			matrix[maxY][x] = matrix[maxY][x+1]
		}
		//우하단에서 위로 가며 위쪽 수를 아래쪽으로
		for y in stride(from: maxY, to: minY, by: -1){
			minNum = min(minNum, matrix[y-1][maxX])
			matrix[y][maxX] = matrix[y-1][maxX]
		}
		//우상단에서 왼쪽으로 가며 왼쪽 수를 오른쪽으로
		for x in stride(from: maxX, to: minX, by: -1) {
			minNum = min(minNum, matrix[minY][x-1])
			matrix[minY][x] = matrix[minY][x-1]
		}

		matrix[minY][minX+1] = firstValue
		answer.append(minNum)
	}

	return answer
}
