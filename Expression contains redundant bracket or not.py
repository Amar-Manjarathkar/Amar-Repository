class Solution():
    def checkRedundancy(self, s):
        stack = []
        for char in s:
            if char == ')':
                # Pop elements until the matching opening bracket is found
                # and check if any operator exists inside
                has_operator = False
                while stack and stack[-1] != '(':
                    if stack[-1] in ('+', '-', '*', '/'):
                        has_operator = True
                    stack.pop()
                
                # If no operator was found between the matching brackets, they are redundant
                if not has_operator:
                    return True
                
                # Pop the matching '('
                if stack:
                    stack.pop()
            else:
                # Push opening brackets, operators, and operands onto the stack
                stack.append(char)
                
        return False       
            
                    
           
                
        
        
