# 3. Exercise 3: Palindrome String Check
# Problem: Given a string, determine if it is a palindrome. A palindrome reads the same forward and
# backward (e.g., "radar", "level").
# Input: "madam"

# W4_Stack.md 2025-07-03

# 5 / 5
# Output: True because "madam" is the same backward.
from linkedListStack import LinkedListStack
def checkPalindrome(input):
  stack = LinkedListStack()
  for char in input:
    stack.push(char) # we add at the end (top) of the stack
  for char in input:
    if char != stack.pop():
      return False
  return True
  ## or just 
  ## return stack == stack[::-1] ## just reverse and compare

def testCheckPalindrome():
  test_cases = [
        ("madam", True),
        ("level", True),
        ("radar", True),
        ("hello", False),
        ("", True),
    ]
  passed = 0
  for i , (input_str , expected) in enumerate(test_cases , 1):
    result = checkPalindrome(input_str)
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
  testCheckPalindrome()