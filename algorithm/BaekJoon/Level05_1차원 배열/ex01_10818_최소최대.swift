//
//  ex01_10818_최소최대.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/07.
//

import Foundation

let count = readLine()
var line = readLine()!.split(separator: " ").map{ Int($0)! }

print("\(line.min()!) \(line.max()!)")
