//
//  빛의 경로 사이클.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/06/02.
//

import Foundation

struct Location: Equatable {
	var x: Int
	var y: Int
	var d: String
}


func solution(_ grid:[String]) -> [Int] {
	var result: [Int] = []
	let g = grid.map{ $0.map { String($0) }}
	let dValue = ["up":(0,-1), "down":(0,1), "right":(1,0), "left":(-1,0)]
	let next: [String:[String:String]] = ["L":["down":"right","right":"up","up":"left","left":"down"],
										  "R":["down":"left","right":"down","up":"right","left":"up"],
										  "S":["down":"down","right":"right","up":"up","left":"left"]]
	var visited = Array(repeating: Array(repeating: ["up": false, "down": false, "left": false, "right": false], count: g[0].count), count: g.count)

	for y in 0..<g.count {
		for x in 0..<g[0].count {
			for d in dValue.keys {
				let start = Location(x: x, y: y, d: d)
				var location = start
				var count = 0
				while (true) {
					if visited[location.y][location.x][location.d]! { break }
					visited[location.y][location.x][location.d] = true
					count += 1
					let direction = g[location.y][location.x]
					location.d = next[direction]![location.d]!
					location.x += dValue[location.d]!.0
					location.y += dValue[location.d]!.1

					location.x = location.x < 0 ? g[0].count-1 : location.x % g[0].count
					location.y = location.y < 0 ? g.count-1 : location.y % g.count

					if location == start && count != 0 {
						result.append(count)
						break
					}

				}
			}
		}
	}
	return result
}

//					    R		up    -> left
//	   U	    L	    ^		down  -> right
//	L ---> R  >>>>>   U | D		right -> up
//	   D			    |		left  -> down
//					    L
//
//					    L		up    -> right
//	   U	    R	    |		down  -> left
//	L ---> R  >>>>>   D | U		right -> down
//	   D			    v		left  -> up
//					    R
//
//					  			up    -> up
//	   U	    S	    U		down  -> down
//	L ---> R  >>>>>  L ---> R	right -> right
//	   D			    D		left  -> left
//
// https://fomaios.tistory.com/entry/Swift-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9B%94%EA%B0%84-%EC%BD%94%EB%93%9C-%EC%B1%8C%EB%A6%B0%EC%A7%80-3-%EB%B9%9B%EC%9D%98-%EA%B2%BD%EB%A1%9C-%EC%82%AC%EC%9D%B4%ED%81%B4
