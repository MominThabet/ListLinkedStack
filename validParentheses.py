#1. Exercise 1: Valid Parentheses
  # Input: "{[()]}"
  # Output: true if balanced; false otherwise
  # Real-world: Compilers, syntax checkers

from linkedListStack import LinkedListStack
def isValidParentheses(expression):
  
  stack = LinkedListStack()

  mapping = {')':'(', '}':'{', ']':'[' }

  for char in expression:
    if char in mapping.values():
      # open brackets
      stack.push(char) # we add at the end (top) of the stack
    elif char in mapping:
      # close brackets 
      if stack.isEmpty() or stack.peek() != mapping[char]:
        # if the stack is empty or the last element is not the corresponding open bracket
        return False
      stack.pop() # we remove the top parenthesis from the stack
    else :
      # pass other characters 
      continue
  return stack.isEmpty()  # True if empty


def testIsValidParentheses():
  test_cases = [
        ("{[()]}", True),
        ("{[(])}", False),
        ("((()))", True),
        ("({[)]}", False),
        ("", True),        
        ("[", False),
        (" (a + (b * c)",False),
        ("{a:[(5+{a})*5]}",True)
    ]
  passed = 0
  for i , (input_str , expected) in enumerate(test_cases , 1):
    result = isValidParentheses(input_str)
    if result == expected :
      print(f"✅ Test {i}: Passed")
      passed += 1
    else:
      print(f"❌ Test {i}: Failed")
      print(f"   Input:    {input_str}")
      print(f"   Expected: {expected}, Got: {result}")
  total = len(test_cases)
  print(f"\nSummary: {passed}/{total} tests passed.")
if __name__ == '__main__':
  testIsValidParentheses()