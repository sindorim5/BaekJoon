//
//  수박수박수박수박수박수?.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/04/25.
//

func solution(_ n:Int) -> String {
	let subak = "수박"
	let su = "수"
	var result: String = ""
	var temp: Int = n / 2

	if temp >= 1 {
		for _ in 1...temp {
			result += subak
		}
	}

	return n % 2 == 1 ? result + su : result
}
