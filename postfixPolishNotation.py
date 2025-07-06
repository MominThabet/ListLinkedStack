# 2. Exercise 2: Evaluate Reverse Polish Notation (Postfix)
# Input: ["2", "1", "+", "3", "*"] → Output: 9
# Use a stack to process operands and operators
# Application: Calculator design


from linkedListStack import LinkedListStack
def evaluatePostfix(expression):

  stack = LinkedListStack()
  operators = {"+", "-", "*", "/"}

  for token in expression:
    if token not in operators:
      stack.push(float(token)) 
    else:
      num2 = stack.pop()
      num1 = stack.pop()
      if token == "+":
        stack.push(num1 + num2)
      elif token == "-":
        stack.push(num1 - num2)
      elif token == "*":
        stack.push(num1 * num2)
      elif token == "/":
        stack.push((num1 / num2))

  return round(stack.peek(), 2)

    
    


def testEvaluatePostfix():
  test_cases = [
    (["3","2","+"] ,5),
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6.6), 
    # 4 + (13 / 5) = 4 + 2 = 6.6
    (["10", "6", "9", "3", "/", "-", "*"], 30),
    (["6" , "9", "3" , "/" , "-", "10", "*"], 30), 
    # 10 * ( 6 - ( 9 / 3 ) ) = 10 * ( 6 - 3 ) = 30
  ]
  passed = 0
  for i , (input_str , expected) in enumerate(test_cases , 1):
    result = evaluatePostfix(input_str)
    if result == expected :
      print(f"✅ Test {i}: Passed")
      print('result: ', result)
      passed += 1
    else:
      print(f"❌ Test {i}: Failed")
      print(f"   Input:    {input_str}")
      print(f"   Expected: {expected}, Got: {result}")
  total = len(test_cases)
  print(f"\nSummary: {passed}/{total} tests passed.")
if __name__ == '__main__':
  testEvaluatePostfix()