import os, sys
from re import T
from typing import Dict
from dataclasses import dataclass
from collections import namedtuple, defaultdict

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
    skills = []
    for r in range(R):
        skill, level = input().split()
        skills.append([skill, int(level)])

    Projects[name] = Project(name, D, S, B, R, skills)
    avg_skills_needed.append(len(skills))

# print(f'Num contributors: {len(Contribs)}, avg skills per contributor: {sum(avg_skills_num) / len(avg_skills_num)}')
# print(f'Num projects: {len(Projects)}, avg num skills required: {sum(avg_skills_needed) / len(avg_skills_needed)}')

gain = lambda p: p.B
all_projects = list(Projects.values())
not_allocated_projects = set(Projects.keys())

project_solutions = []
current_day = 0
something_allocated = True

while something_allocated:
    all_projects = [p for name, p in Projects.items() if name in not_allocated_projects]
    something_allocated = False

    projects_order = sorted(all_projects, key=lambda p: max(0, p.S + min(0, p.B - current_day - p.D)))
    for project in projects_order:
        role_assigmnents = []
        impossible = False

        taken_contribs = set()
        requires_mentoring = {}

        for skill, level in project.skills:
            ok = False
            for contrib_name, contrib_skills in Contribs.items():
                if contrib_skills.get(skill, -1) >= level:
                    ok = True
                    break

            if not ok:
                if skill in requires_mentoring:
                    requires_mentoring[skill] = max(requires_mentoring[skill], level)
                else:
                    requires_mentoring[skill] = level

        change = True
        job_id_to_person = {}
        bump_skill = []
        
        while change:
            max_mentor_skills = []
            max_mentor_name = None
            job_allocation = None
            skill_diff = None
            change = False

            for contrib_name, contrib_skills in Contribs.items():
                skills_can_mentor = [skill for skill, level in contrib_skills.items()
                                    if skill in requires_mentoring and requires_mentoring[skill] <= level]
                min_skill_diff = float("inf")
                min_skill = None
                for idx, (skill, level) in enumerate(project.skills):
                    skill_diff = contrib_skills.get(skill, -1) - level
                    if (
                        idx not in job_id_to_person and 
                        contrib_skills.get(skill, -1) >= level and
                        skill_diff < min_skill_diff
                    ):
                        min_skill_diff = skill_diff
                        min_skill = idx

                if min_skill is None:
                    continue

                if len(skills_can_mentor) > len(max_mentor_skills):
                    max_mentor_skills = skills_can_mentor
                    max_mentor_name = contrib_name
                    skill_diff = min_skill_diff
                    job_allocation = idx

            if len(max_mentor_skills):
                change = True
                    
                for mentor_skill in max_mentor_skills:
                    requires_mentoring.pop(skill)
                    for project_skill_idx in range(len(project.skills)):
                        if project.skills[project_skill_idx][0] == skill:
                            project.skills[project_skill_idx][1] -= 1
                
                job_id_to_person[job_allocation] = max_mentor_name
                if skill_diff == 0:
                    bump_skill.append([max_mentor_name, idx])
                taken_contribs.add(max_mentor_name)
                
        if requires_mentoring:
            continue

        for idx, (skill, level) in enumerate(project.skills):
            if idx in job_id_to_person:
                continue

            min_contributor_skill = float("inf")
            min_contributor = None
            min_skill_diff = None

            for contrib_name, contrib_skills in Contribs.items():
                skill_diff = contrib_skills.get(skill, -1) - level
                if (
                    skill_diff >= 0 and
                    min_contributor_skill > contrib_skills.get(skill, -1) and 
                    contrib_name not in taken_contribs
                ):
                    min_contributor = contrib_name
                    min_contributor_skill = contrib_skills.get(skill, -1)
                    min_skill_diff = skill_diff

            if min_contributor is None:
                impossible = True
                break

            taken_contribs.add(min_contributor)
            job_id_to_person[idx] = min_contributor
            if min_skill_diff == 0:
                bump_skill.append([min_contributor, idx])

        if not impossible:
            something_allocated = True
            project_solutions.append([project.name, job_id_to_person])
            not_allocated_projects.remove(project.name)
            current_day += project.D

            for person, skill_idx in bump_skill:
                Contribs[person][project.skills[skill_idx][0]] += 1

            break
            

print(len(project_solutions))
for name, assignments in project_solutions:
    print(name)
    print(" ".join(assignments[idx] for idx in range(len(assignments))))
    
    



        

