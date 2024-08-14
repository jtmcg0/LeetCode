# 412. Fizz Buzz

### Instructions, Examples & Constraints

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.  
answer[i] == "Fizz" if i is divisible by 3.  
answer[i] == "Buzz" if i is divisible by 5.  
answer[i] == i (as a string) if none of the above conditions are true.
 

#### Example 1:

Input: n = 3  
Output: ["1","2","Fizz"]

#### Example 2:

Input: n = 5  
Output: ["1","2","Fizz","4","Buzz"]

#### Example 3:

Input: n = 15  
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

### Constraints:
- 1 <= n <= 104

## My Solution:

- Initialize counter variable i to 1
- Loop while i is less than n + 1
- If modulus of i = 0 for 3 and 5, append "FizzBuzz" to list
- Else if i%3 = 0 append "Fizz" to list
- Else if i%5 = 0 append "Buzz" to list
- Else append the value of i as a string to list
- Increase i by 1 until while loop breaks
- return the generated list

### Time Complexity:

$O(n)$

### Space Complexity:

$O(n)$
