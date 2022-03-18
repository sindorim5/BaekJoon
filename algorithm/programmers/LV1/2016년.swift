//
//  2016년.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/03/19.
//

func solution(_ a:Int, _ b:Int) -> String {
	let week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
	let year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	var sum = 0
	var month = 1
	var day = 1
	var result: String = ""
	
	month = a - month
	day = b - day
	
	if month == 0 {
		day = day % 7
	} else {
		for i in 0..<month {
			sum += year[i]
		}
		day = (sum + day) % 7
	}
	result = week[day]

	return result
}
