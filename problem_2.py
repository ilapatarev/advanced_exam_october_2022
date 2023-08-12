size=int(input())
car_num=input()

matrix=[]

for _ in range(size):
	p=input().split()
	matrix.append(p)

pos_r=0
pos_c=0
found=False
for y in range(size):
	if found:
		break
	for u in range(size):
		if matrix[y][u]=='T':
			matrix[y][u]='E'
			found=True
			break

e_r=0
e_c=0
t_r=0
t_c=0
for r in range(size):
	for c in range(size):
		if matrix[r][c]=='E':
			e_r=r
			e_c=c
		elif matrix[r][c]=='T':
			t_r=r
			t_c=c

passed_km=0
tunnel=False
command=input()
finish=False
while command!='End':
	if command=='left':
		pos_c-=1
	elif command=='right':
		pos_c+=1
	elif command=='up':
		pos_r-=1
	elif command=='down':
		pos_r+=1

	current_pos=matrix[pos_r][pos_c]
	if current_pos=='E':
		pos_r=t_r
		pos_c=t_c
		matrix[e_r][e_c]='.'
		matrix[t_r][t_c]='.'
		passed_km+=30
		tunnel=True
	elif current_pos=='T':
		pos_r=e_r
		pos_c=e_c
		matrix[e_r][e_c]='.'
		matrix[t_r][t_c]='.'
		passed_km+=30
		tunnel=True
	elif current_pos=='F':
		finish=True
		passed_km+=10
		break
	elif current_pos=='.':
		passed_km+=10

	command=input()
if not tunnel:
	matrix[e_r][e_c]='T'

if finish:
	print(f"Racing car {car_num} finished the stage!")
else:
	print(f"Racing car {car_num} DNF.")
print(f"Distance covered {passed_km} km.")
matrix[pos_r][pos_c]='C'
for row in matrix:
	print(''.join(row))

print(matrix[20][20])

