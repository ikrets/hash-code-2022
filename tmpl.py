#!/usr/bin/env python

import os, sys
from typing import Dict, List, Tuple
from dataclasses import dataclass
from collections import namedtuple
import pandas as pd

# an integer C (1 ≤ C≤ 105) – the number of contributors,
# an integer P (1 ≤ P ≤ 105) – the number of projects.
C, P = map(int, input().split())

stat_skills_amount = []
stat_skills_required = []
stat_skills_level = []
projects_scores = []

# the first line contains:
# the contributor's name (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, or numbers 0-9),
# an integer N (1≤ N ≤ 100) - the number of skills of the contributor.
# the next N lines describe individual skills of the contributor. Each such line contains:
# the name of the skill (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, numbers 0-9, dashes '-' or pluses '+'),
# an integer Li (1≤ Li ≤ 10) - skill level.
Contribs = {}
ContribSkills = {}
for c in range(C):
    name, nskills = input().split()
    nskills = int(nskills)

    skills = {}
    for ns in range(nskills):
        skill, level = input().split()
        level = int(level)
        skills[skill] = level
        ContribSkills.setdefault(skill, set()).add(name)
        stat_skills_level.append(level)

    Contribs[name] = skills
    stat_skills_amount.append(len(skills))

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
    skills: List[Tuple[str, int]]

durations = []
scores = []
best_befores = []

Projects = []
for p in range(P):
    name, *constr = input().split()
    D, S, B, R = map(int, constr)
    skills = []
    for r in range(R):
        skill, level = input().split()
        skills.append((skill, int(level)))

    assert len(skills) == R
    Projects.append(Project(name, D, S, B, R, skills))
    stat_skills_required.append(len(skills))
    projects_scores.append(S)
    durations.append(D)
    best_befores.append(B)

print(f'*** Num contributors: {len(Contribs)}, avg skills per contributor:')
print(pd.Series(stat_skills_amount).describe())
print(f'*** Num projects: {len(Projects)}, avg skills required:')
print(pd.Series(stat_skills_required).describe())
print(f'skills level: {pd.Series(stat_skills_level).describe()}')
print(f'project scores: {pd.Series(projects_scores).describe()}')
print(f'project durations: {pd.Series(durations).describe()}')
print(f'project best befores: {pd.Series(best_befores).describe()}')
print(f'*** Score upper bound: {sum(projects_scores)}')
# 800 10000
# c574 1
# s132 10
# c376 1
# s100 10
# c312 1
# s652 10
# c752 1
# s740 10
# c620 1
# s668 10
# c317 1
# p9020 84 349 36349 5
# s200 10
# s780 10
# s606 10
# s781 10
# s315 10
# p2023 50 26 28195 1
# s702 10
# p2329 64 415 39145 5
# s45 10
# s689 10
# s580 10
# s699 10
# s482 10

# Projects.sort(key=lambda p: ( p.))

