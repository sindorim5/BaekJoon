//
//  메뉴 리뉴얼.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/05/30.
//

import Foundation

func combi(_ order: String, _ targetNum: Int) -> [String] {
	var result = [String]()

	func combination(_ index: Int, _ nowCombi: String) {
		if nowCombi.count == targetNum {
			result.append(nowCombi)
			return
		}
		for i in index..<order.count {
			let index = order.index(order.startIndex, offsetBy: i)
			combination(i + 1, nowCombi + order[index...index])
		}
	}

	combination(0, "")

	return result
}

func solution(_ orders:[String], _ course:[Int]) -> [String] {

	var answer : Set<String> = []
	var dict: [String : Int] = [:]
	var orderCombinations: [String] = []

	// orders의 원소들을 알파벳 순으로 정렬
	let orders = orders.map { order in
		order.sorted(by: <)
	}

	// orders 배열을 돌며 course 수만큼 조합
	for order in orders {
		for i in course {
			orderCombinations += combi(String(order), i)
		}
	}

	// 조합배열을 딕셔너리에 기록
	for comb in orderCombinations {
		if dict.keys.contains(comb) {
			dict[comb]! += 1
		} else {
			dict[comb] = 1
		}
	}

	// 각 course별로 최대 주문량 조합을 찾아내고 answer 세트에 추가
	for num in course {
		let sortedDict = dict.filter { $0.key.count == num }
		let maxCount = sortedDict.values.max()
		if maxCount == 1 { continue }
		sortedDict.keys.filter { sortedDict[$0] == maxCount }.forEach {
			answer.insert($0)
		}
	}

	return Array(answer.sorted())
}
