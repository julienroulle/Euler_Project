import os, ast

with open(os.path.dirname(__file__) + "/names.txt", "r") as f:
    content = ast.literal_eval(f.readline())
    content = sorted(content)

name_score = 0
for i, name in enumerate(content):
    score = 0
    for letter in name:
        score += ord(letter) - 64
    name_score += (i+1) * score

print(name_score)