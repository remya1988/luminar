class Editor:
    def functionalities(self):
        self.func = ["a1","a2","a3"]
        return self.func
class Pycharm(Editor):
    def functionalities(self):
        func = super().functionalities()
        func.append(["a4","a5"])
        return func
class Vscode(Editor):
    def functionalities(self):
        func = super().functionalities()
        func.append(["a6","a7"])
        return func
py = Pycharm()
print(py.functionalities())
vs = Vscode()
print(vs.functionalities())