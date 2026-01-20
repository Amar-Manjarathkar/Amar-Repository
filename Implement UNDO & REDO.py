class Solution:
    def __init__(self):
        # Initialize two stacks
        self.doc = []          # Stores current characters
        self.redo_stack = []   # Stores undone characters for potential redo

    def append(self, x):
        # Add character to the document
        self.doc.append(x)
        # Once a new append happens, the redo history is invalidated
        self.redo_stack.clear()

    def undo(self):
        # If document is not empty, move the last char to redo stack
        if self.doc:
            char = self.doc.pop()
            self.redo_stack.append(char)

    def redo(self):
        # If there are items to redo, move the last undone char back to doc
        if self.redo_stack:
            char = self.redo_stack.pop()
            self.doc.append(char)

    def read(self):
        # Join the list into a single string
        return "".join(self.doc)
