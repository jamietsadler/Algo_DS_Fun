class Solution:
    def simplifyPath(self, path: str) -> str:


        stack = []

        for word in path.split('/'):
            if word == "" or word == '.':
                continue
            elif word == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(word)

        return '/' + '/'.join(stack)