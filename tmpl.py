import os, sys
from typing import Dict
from dataclasses import dataclass
from collections import namedtuple

# an integer C (1 ≤ C≤ 105) – the number of contributors,
# an integer P (1 ≤ P ≤ 105) – the number of projects.
C, P = map(int, input().split())

avg_skills_num = []
avg_skills_needed = []

# the first line contains:
# the contributor's name (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, or numbers 0-9),
# an integer N (1≤ N ≤ 100) - the number of skills of the contributor.
# the next N lines describe individual skills of the contributor. Each such line contains:
# the name of the skill (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, numbers 0-9, dashes '-' or pluses '+'),
# an integer Li (1≤ Li ≤ 10) - skill level.
Contribs = {}
for c in range(C):
    name, nskills = input().split()
    nskills = int(nskills)

    skills = {}
    for ns in range(nskills):
        skill, level = input().split()
        level = int(level)
        skills[skill] = level

    Contribs[name] = skills
    avg_skills_num.append(len(skills))

# the first line contains:
# the name of the project (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z or numbers 0-9),
# an integer Di (1 ≤Di ≤ 105) – the number of days it takes to complete the project,
# an integer Si (1 ≤ Si ≤ 105) – the score awarded for project’s completion,
# an integer Bi (1 ≤ Bi ≤ 105) – the “best before” day for the project,
# an integer Ri (1 ≤ Ri ≤ 100) – the number of roles in the project.
# the next Ri lines describe the skills in the project:
# a string Xk – the name of the skill (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, numbers 0-9, dashes '-' or pluses '+'),
# an integer Lk (1≤Lk≤100) – the required skill level.

@dataclass
class Project:
    name: str
    D: int
    S: int
    B: int
    R: int
    skills: Dict[str, int]

Projects = {}
for p in range(P):
    name, *constr = input().split()
    D, S, B, R = map(int, constr)
    skills = {}
    for r in range(R):
        skill, level = input().split()
        skills[skill] = int(level)

    Projects[name] = Project(name, D, S, B, R, skills)
    avg_skills_needed.append(len(skills))

print(f'Num contributors: {len(Contribs)}, avg skills per contributor: {sum(avg_skills_num) / len(avg_skills_num)}')
print(f'Num projects: {len(Projects)}, avg num skills required: {sum(avg_skills_needed) / len(avg_skills_needed)}')


