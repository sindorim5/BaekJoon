//
//  프린터.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/06/03.
//

import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
	var dict: [Int:Int] = [:]
	var priorities = priorities
	var result: [Int] = []

	for i in 0..<priorities.count {
		dict[i] = priorities[i]
	}

	priorities = priorities.sorted(by: >)

	let sortedDict = dict.sorted { $0.0 < $1.0 }

	var index = 0

	while !priorities.isEmpty {
		for i in sortedDict {
			if i.value == priorities.max() {
				result.insert(i.key, at: index)
				index += 1
				priorities.removeFirst()
			}
		}
	}

	return result.firstIndex(of: location)! + 1
}

// var priority: [(Int,Int)] = priorities.enumerated().map {($0.offset, $0.element)}
