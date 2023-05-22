//
//  오픈채팅방.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/29.
//

import Foundation

func solution(_ record:[String]) -> [String] {
	var userId = [String : String]()
	var message: [String] = []

	// read record, update changed nickname
	for line in record {
		let data = line.components(separatedBy: " ")
		let command = data[0]
		let uid = data[1]

		if command != "Leave" {
			let nickname = data[2]
			userId.updateValue(nickname, forKey: uid)
		}
		if command != "Change" {
			message.append("\(command) \(uid)")
		}
	}

	return messageToResult(message, userId)
}

func messageToResult(_ message: [String], _ userId: [String : String]) -> [String] {
	var result: [String] = []

	for line in message {
		let data = line.components(separatedBy: " ")
		let command = data[0]
		let uid = data[1]

		if command == "Enter" {
			result.append("\(userId[uid]!)님이 들어왔습니다.")
		} else if command == "Leave" {
			result.append("\(userId[uid]!)님이 나갔습니다.")
		}
	}

	return result
}
