//
//  ex06_2775_부녀회장.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/11.
//

let testCase = Int(readLine()!)!

for _ in 1...testCase {
    let k = Int(readLine()!)!
    let n = Int(readLine()!)!

    var array = Array(repeating: (Array(repeating: 1, count: n)), count: k + 1)
    
    for x in 0...k {
        for y in 0..<n {
            if (x == 0) {
                array[x][y] = y + 1
            }
            else {
                if (y == 0) {
                    array[x][y] = 1
                }
                else {
                    array[x][y] = array[x-1][y] + array[x][y-1]
                }
            }
        }
    }
    print(array[k][n-1])
}

/* timeout
 let testCase = Int(readLine()!)!
 var i: Int = 0

 func bansang(num1: Int, num2: Int) -> Int{
     
     if (num1 == 0) {
         i = num2
     }
     else if (num2 == 1) {
         i = 1
     }
     else {
         i = bansang(num1: num1, num2: (num2 - 1) ) + bansang(num1: (num1 - 1), num2: num2)
     }
     return (i)
 }

 for _ in 1...testCase {
     let k = Int(readLine()!)!
     let n = Int(readLine()!)!
     
     print(bansang(num1: k, num2: n))
 }

*/
