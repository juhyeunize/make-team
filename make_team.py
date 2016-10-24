# -*- coding: utf-8 -*- 
import random

def make_team(member_list, num_team):
	num_member_of_team = len(member_list) / num_team
	remainder = len(member_list) % num_team
	random.shuffle(people)
	teams = []
	for i in range(num_team):
		team = people[i * num_member_of_team : i * num_member_of_team + num_member_of_team]
		teams.append(team)
	if not remainder == 0:
		for i in range(remainder):
			teams[i].append(people[num_member_of_team * num_team + i])
	for i in range(len(teams)):
		random.shuffle(teams[i])

	return teams

people = ['김상훈', '김세영', '김하윤', '김한샘', '나상일', '박지민', '이경옥', '이수빈', '이지민', '장언동', '장정운', '최찬규', '최호열', '한주현']
teams = make_team(people, 4)
for i in range(len(teams)):
	print " ".join(teams[i])