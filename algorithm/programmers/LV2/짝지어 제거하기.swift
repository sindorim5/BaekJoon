//
//  짝지어 제거하기.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/05/27.
//

import Foundation

func solution(_ s:String) -> Int{

	if s.count % 2 != 0 {
		return 0
	}

	let array = Array(s)
	var check: [Character] = []

	for i in array {
        if check.isEmpty {
            check.append(i)
        } else {
            if check.last == i {
	    		check.removeLast()
	    	} else {
	    		check.append(i)
		    }
        }
	}

	return check.isEmpty ? 1 : 0
}


// s.map { String(s) } 느림

// 조건문 A && B : 하나의 expression. 양쪽의 A && B 를 논리연산자로 계산해 참, 거짓의 결과를 가져온다.
// 조건문 , : expression, expression 으로 이루어진 condition-list. 순차적으로 실행하여 모두 참이 되어야 한다.
