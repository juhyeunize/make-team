# -*- coding: utf-8 -*- 
import random

def make_team(member_list, num_team):
	num_member_of_team = len(member_list) / num_team
	remainder = len(member_list) % num_team
	random.shuffle(member_list)
	teams = []
	for i in range(num_team):
		team = member_list[i * num_member_of_team : i * num_member_of_team + num_member_of_team]
		teams.append(team)
	if not remainder == 0:
		for i in range(remainder):
			teams[i].append(member_list[num_member_of_team * num_team + i])
	return teams

people1 = ['김상훈', '김세영', '김하윤', '김한샘', '나상일', '박지민', '이경옥', '이수빈', '이지민', '장언동', '장정운', '최찬규', '최호열', '한주현']
people2 = ['김혜선', '오종민', '이선명', '이지아', '이현균', '이화옥', '정유진', '주슬기', '진달래', '최기정', '최유정']
num_teams = 4
teams1 = make_team(people1, num_teams)
teams2 = make_team(people2, num_teams)
teams = []
for i in range(len(teams1)):
	teams.append(teams1[i] + teams2[len(teams2) - i - 1])
	# To select team leader
	random.shuffle(teams[i])
	print " ".join(teams[i])