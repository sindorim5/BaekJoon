//
//  ex11_2588_곱셈.swift
//  algorithm
//
//  Created by Kihun SONG on 2022/01/05.
//

import Foundation

var input1 = readLine()
var input2 = readLine()
var num1, num2: Int
var num2Array = Array<Int>()

if (input1 != nil && input1 != "") && (input2 != nil && input2 != ""){
    num1 = Int(input1!)!
    num2 = Int(input2!)!
}
else {
    print("NO INPUT")
    exit(1)
}
func numDigit(number: Int) -> Int{
    var digit: Int
    var num = number
    digit = 0
    while(num != 0){
        num /= 10
        digit += 1
    }
    return digit
}
func numArray(number: Int) -> Array<Int> {
    var array = Array<Int>()
    var num: Int = number
    var digit: Int = numDigit(number: number)
    while(digit != 0){
        array.append(num % 10)
        num /= 10
        digit -= 1
    }
    return array
}
func showResult(number1: Int, number2: Int, numberArray: Array<Int>){
    var i: Int = 0
    while(i < numberArray.count){
        print(number1 * numberArray[i])
        i += 1
    }
    print(number1 * number2)
}

num2Array = numArray(number: num2)
showResult(number1: num1, number2: num2, numberArray: num2Array)
exit(0)
