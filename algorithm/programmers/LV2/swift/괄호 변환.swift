//
//  괄호 변환.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/05/31.
//

import Foundation

// 균형잡힌 괄호 문자열 체크
func checkBalanced(_ word: String) -> Bool {
	var count = 0
	for i in word {
		i == "(" ? (count += 1) : (count -= 1)
	}

	return count == 0 ? true : false
}

// 올바른 괄호 문자열 체크
func checkRight(_ word: String) -> Bool {
	var count = 0
	for i in word {
		if i == "(" {
			count += 1
		} else {
			if count > 0 {
				count -= 1
			} else {
				return false
			}
		}
	}
	return count == 0 ? true : false
}

// u와 v를 가르는 문자열 인덱스 구하기
func detachUVindex(_ word: String) -> Int {
	var count = 0
	var index = 0

	for i in word {
		if i == "(" {
			count += 1
		} else if i == ")" {
			count -= 1
		}
		if count == 0 { break }
		index += 1
	}

	return index + 1
}

// 올바른 괄호 문자열 만들기
func makeRight(_ word: String) -> String {
	var result = ""

	if checkRight(word) {
		return word
	}

	//2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
	let index = detachUVindex(word)
	var u = String(word[..<word.index(word.startIndex, offsetBy: index)])
	let v = String(word[word.index(word.startIndex, offsetBy: index)...])

	//3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
	//  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
	if checkRight(u) {
		return u + makeRight(v)
	} else {
		//4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
		//  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
		//  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
		//  4-3. ')'를 다시 붙입니다.
		result = "(" + makeRight(v) + ")"

		//  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
		u.removeFirst()
		u.removeLast()
		for i in u {
			if i == "(" {
				result += ")"
			} else {
				result += "("
			}
		}
	}
	//  4-5. 생성된 문자열을 반환합니다.
	return result
}

func solution(_ p:String) -> String {
	//1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
	if p.count == 0 { return "" }

	return makeRight(p)
}




// func solution(_ p:String) -> String {
//     if p.count < 1 {return ""}

//     var count = 0, index = p.startIndex
//     repeat{
//         count += String(p[index]) == "(" ? 1 : -1
//         index = p.index(after: index)
//     } while count != 0

//     var u = String(p[..<index]), v = String(p[index...])
//     if String(u.first!) == "("{
//         return u + solution(v)
//     }else{
//         u.removeLast()
//         u.removeFirst()
//         return "(\(solution(v)))\(u.map{String($0) == "(" ? ")" : "("}.joined())"
//     }
// }
