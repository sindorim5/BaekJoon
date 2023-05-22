//
//  ex02_10951_A+B - 4.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

var array: [Int] = []

while let line = readLine() {
    array = line.split(separator: " ").map{ Int(($0))! }
    print(array[0]+array[1])
}
