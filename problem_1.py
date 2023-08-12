from collections import deque

caffeine=list(map(int, input().split(', ')))
en_drink=deque(map(int, input().split(', ')))

total_caffeine=0

while caffeine and en_drink:
	last_caff=caffeine.pop()
	first_drink=en_drink.popleft()
	su=last_caff*first_drink
	if total_caffeine+su<=300:
		total_caffeine+=su
		continue
	else:
		en_drink.append(first_drink)
		if total_caffeine>=30:
			total_caffeine-=30
		else:
			total_caffeine=0

if en_drink:
	print(f"Drinks left: {', '.join(str(x) for x in en_drink)}")
else:
	print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")