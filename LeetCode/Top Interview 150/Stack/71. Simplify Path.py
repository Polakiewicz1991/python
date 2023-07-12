# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given a string path, which is an absolute path (starting with a slash '/') to a file or directory               ║
# ║ in a Unix-style file system, convert it to the simplified canonical path.                                       ║
# ║                                                                                                                 ║
# ║ In a Unix-style file system, a period '.' refers to the current directory, a double period '..'                 ║
# ║ refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single    ║
# ║ slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.     ║
# ║                                                                                                                 ║
# ║ The canonical path should have the following format:                                                            ║
# ║                                                                                                                 ║
# ║   The path starts with a single slash '/'.                                                                      ║
# ║    Any two directories are separated by a single slash '/'.                                                     ║
# ║   The path does not end with a trailing '/'.                                                                    ║
# ║   The path only contains the directories on the path from the root directory to the target                      ║
# ║ file or directory (i.e., no period '.' or double period '..')                                                   ║
# ║                                                                                                                 ║
# ║ Return the simplified canonical path.                                                                           ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

class Solution:
    def simplifyPath(self, path: str) -> str:

        while '//' in path:
            path = path.replace('//', '/')
        print("after //  :", path)
        while '/./' in path:
            path = path.replace('/./', '/')

        print("after /./  :", path)

        while '/../' in path:
            index = path.find('/../')
            # print(index)

            while path[index - 1] != '/' and index != 0:
                print(index, path[index - 1])
                index -= 1
            print("last index", index)

            print("to delete: ", path[index:path.find('/../') + 4])

            #            path = path.replace('/../','/')
            if index != 0:
                path = path.replace(path[index:path.find('/../') + 4], '', 1)
            else:
                path = path.replace(path[index + 1:path.find('/../') + 4], '', 1)
            print("path", path)

        if path.endswith('/..') and len(path) > 1:
            index = path.find('/..')
            # print(index)

            while path[index - 1] != '/' and index != 0:
                print(index, path[index - 1])
                index -= 1
            print("last index", index)

            print("to delete: ", path[index:path.find('/..') + 3])

            #            path = path.replace('/../','/')
            if index != 0:
                path = path.replace(path[index:path.find('/..') + 3], '', 1)
            else:
                path = path.replace(path[index + 1:path.find('/..') + 3], '', 1)
            print("path", path)

        if path.endswith('/.') and len(path) > 1:
            path = path.removesuffix('.')

        if path.endswith('/') and len(path) > 1:
            path = path.removesuffix('/')

        return path

Wynik = Solution()

path = "/home/"
Wynik1 = Wynik.simplifyPath(path=path)
print("******\nWynik1", Wynik1, "\n******")


path = "../../"
Wynik1 = Wynik.simplifyPath(path=path)
print("******\nWynik1", Wynik1, "\n******")


path = "/home//foo/"
Wynik1 = Wynik.simplifyPath(path=path)
print("******\nWynik1", Wynik1, "\n******")

path = "/a/./abC/../../c/" #"/c"
Wynik1 = Wynik.simplifyPath(path=path)
print("******\nWynik1", Wynik1, "\n******")

path ="/a/../../b/../c//.//" #"/c"
Wynik1 = Wynik.simplifyPath(path=path)
print("******\nWynik1", Wynik1, "\n******")

path = "/a//b////c/d//././/.."
Wynik1 = Wynik.simplifyPath(path=path)
print("******\nWynik1", Wynik1, "\n******")

path = "/..hidden" #"/..hidden"
Wynik1 = Wynik.simplifyPath(path=path)
print("******\nWynik1", Wynik1, "\n******")