//
//  ex02_4673_셀프넘버.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/08.
//

var result: Set<Int> = []
var original: Set<Int> = []

func d(num: Int) -> Int {
    var sum = num
    var tmp = num
    while (tmp > 0) {
        sum += tmp % 10
        tmp /= 10
    }
    return sum
}

for i in 1...10000 {
    original.insert(i)
}

for i in 1...10000 {
    var j: Int = i
    while (j < 10000) {
        let add = d(num: j)
        if (add > 10000) { break }
        result.insert(add)
        j = add
    }
}

original.subtracting(result).sorted().forEach{print($0)}

/*
 var result: Set<Int> = []

 func d(num: Int) -> Int {
     var sum = num
     var tmp = num
     while (tmp > 0) {
         sum += tmp % 10
         tmp /= 10
     }
     return sum
 }

 for i in 1...10000 {
     var j: Int = i
     while (j < 10000) {
         let add = d(num: j)
         if (add > 10000) { break }
         result.insert(add)
         j = add
     }
 }

 for i in 1...10000 {
     if result.contains(i) == false {
         print(i)
     }
 }
*/
