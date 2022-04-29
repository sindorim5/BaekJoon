//
//  하샤드 수.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/28.
//

func solution(_ x:Int) -> Bool {
	let sum = String(x).map { String($0) }.reduce(0) { Int($0) + Int($1)! }
	return x % sum == 0 ? true : false
}
