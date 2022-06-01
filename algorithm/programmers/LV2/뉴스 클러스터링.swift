//
//  뉴스 클러스터링.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/05/31.
//

func makeJaccardArray(_ str: String) -> [String] {
	let str = str.uppercased()
	let array = Array(str)
	var jaccardArray: [String] = []

	for i in 0..<array.count - 1 {
		if array[i].isLetter && array[i+1].isLetter {
			jaccardArray.append("\(array[i])\(array[i+1])")
		}
	}

	return jaccardArray
}

func solution(_ str1:String, _ str2:String) -> Int {

	var jaccardStr1 = makeJaccardArray(str1)
	var jaccardStr2 = makeJaccardArray(str2)

	var all = jaccardStr1.count + jaccardStr2.count
	print(all)
	var union = 0
	var intersection = 0

	if all == 0 {
		return 65536
	}
	if jaccardStr1.isEmpty || jaccardStr2.isEmpty {
		return 0
	}

	for i in 0..<jaccardStr1.count {
		for j in 0..<jaccardStr2.count {
			if jaccardStr1[i] == jaccardStr2[j] {
				jaccardStr2.remove(at: j)
				intersection += 1
				break
			}
		}
	}
	union = all - intersection

	if union == 0 {
		return 65536
	}

	return Int(Double(intersection) / Double(union) * 65536)
}
