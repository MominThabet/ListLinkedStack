# Assignment for Next Week Task: Convert an infix expression to postfix (Reverse Polish Notation)
# Example: "(1 + 2) * 3" → "1 2 + 3 *"
# Use a stack to store operators based on precedence
from linkedListStack import LinkedListStack
def tokenize(expr):
  tokens = []
  number = ''
  for ch in expr:
    if ch.isdigit():
      number += ch
    else:
      if number:
        tokens.append(number)
        number = ''
      if ch in '+-*/()':
        tokens.append(ch)
  if number:
    tokens.append(number)
  return tokens
def convertInfixToPostfix( expression ):
  stack = LinkedListStack()
  operators = {"+", "-", "*", "/"}
  precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
  postfix = []

  # tokenize the expression
  tokens = tokenize(expression)

  for token in tokens:
    if token.isdigit():
      postfix.append(token)
    elif token in operators:
      while (not stack.isEmpty() and stack.peek() != "(" and
              precedence[token] <= precedence.get(stack.peek(), 0)):
        postfix.append(stack.pop())
      stack.push(token)

    elif token == "(":
      stack.push(token)
      
    elif token ==")":
      while not stack.isEmpty() and stack.peek() != "(":
        postfix.append(stack.pop())
      stack.pop()

    # Step 4: Pop any remaining operators
  while not stack.isEmpty():
    postfix.append(stack.pop())
  
  return " ".join(postfix)

def testInfixToPostfix():
  test_cases = [
   ("(1 + 2) * 3" , "1 2 + 3 *"),
    ("3 + 4 * 2 / ( 1 - 5 )", "3 4 2 * 1 5 - / +"),
    ("10 + 2 * 6", "10 2 6 * +"),
    ("100 * ( 2 + 12 ) / 14", "100 2 12 + * 14 /"),
  ]
  passed = 0
  for i , (input_str , expected) in enumerate(test_cases , 1):
    result = convertInfixToPostfix(input_str)
    if result == expected :
      print(f"✅ Test {i}: Passed")
      passed += 1
    else:
      print(f"❌ Test {i}: Failed")
      print(f"   Input:    {input_str}")
      print(f"   Expected: {expected}, Got: {result}")
  total = len(test_cases)
  print(f"\nSummary: {passed}/{total} tests passed.")

if __name__ == "__main__":
  testInfixToPostfix()