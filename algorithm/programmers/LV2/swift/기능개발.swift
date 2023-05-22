//
//  기능개발.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/05/26.
//

import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
	var progress = progresses
	var result: [Int] = []
	var count: Int = 0
	var num = Int(ceil( Double(100 - progress[0]) / Double(speeds[0]) ))

	for i in 0..<progress.count {
		progress[i] = Int(ceil( Double(100 - progress[i]) / Double(speeds[i]) ))
		if num >= progress[i] {
			count += 1
		} else {
			num = progress[i]
			result.append(count)
			count = 1
		}
	}

	result.append(count)

	return result
}
