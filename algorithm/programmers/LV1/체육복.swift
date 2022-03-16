//
//  체육복.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/16.
//

import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
	var array = Array(1...n)
	var newReserve = Array(Set(reserve).subtracting(Set(lost)).sorted())
	let newLost = Array(Set(lost).subtracting(Set(reserve)).sorted())
	array = Array(Set(array).subtracting(newLost).sorted())
	
	for i in 0..<newLost.count {
		if newReserve.contains ( where: { newLost[i] - 1 == $0 } ) {
			newReserve.removeAll(where: { newLost[i] - 1 == $0 })
			array.append(newLost[i])
		} else if newReserve.contains(where: { newLost[i] + 1 == $0 } ) {
			newReserve.removeAll(where: { newLost[i] + 1 == $0 })
			array.append(newLost[i])
		}
	}
	
	return array.count
}
