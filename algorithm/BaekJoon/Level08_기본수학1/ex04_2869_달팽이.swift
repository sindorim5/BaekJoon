//
//  ex04_2869_달팽이.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

import Foundation

var array: [Double] = []
array = readLine()!.split(separator: " ").map{ Double(String($0))! }
let A = array[0]; let B = array[1]; let V = array[2]

var day = ceil((V-B) / (A-B))

print(Int(day))
