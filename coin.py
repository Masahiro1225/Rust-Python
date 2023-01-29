price = 3950

for i500 in range(11):
    for i100 in range(4):
        for i50 in range(11):
            total = i500*500 + i100*100 + i50*50
            if total == price:
                print(f"500円：{i500}枚、100円：{i100}枚、50円：{i50}枚")