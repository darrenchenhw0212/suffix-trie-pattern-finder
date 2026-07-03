from src import PatternFinder

finder = PatternFinder("AAABBBCCC")

print(finder.find("AAA", "BB"))
print(finder.find("AA", "BC"))
print(finder.find("A", "B"))
print(finder.find("AA", "A"))

