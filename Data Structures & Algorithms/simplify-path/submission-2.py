class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # path_list = path.split('/')
        # ["", "home", "", "foo", "..", "bar", ""]
        for i in path.split('/'):
            if stack and i == '..':
                stack.pop()
            if i not in ['.', '..', '']:
                stack.append(i)
        return '/'+'/'.join(stack)