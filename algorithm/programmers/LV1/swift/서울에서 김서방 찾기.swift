//
//  서울에서 김서방 찾기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/25.
//

import Foundation

func solution(_ seoul:[String]) -> String {
	let index = seoul.firstIndex(where: { $0 == "Kim"}) ?? 0

	return "김서방은 \(index)에 있다"
}
