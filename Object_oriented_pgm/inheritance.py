class Parent:
    def properties(self):
        self.prop = {"name":"Rem","age":23,"place":"kollam"}
        return self.prop
class Child(Parent):
    def properties(self):
        prop = super().properties()
        prop["car"] = "swift"
        # prop["ch"] = {"hus": "Jyo", "age_hus": 33, "place_hus": "tvm"}
        return self.prop

ch = Child()
print(ch.properties())

