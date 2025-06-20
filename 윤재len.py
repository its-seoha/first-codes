text = "족보세트는 맛있어"
print("문자 하나씩 출력해볼게!|n")
for i in range(len(text)):
    print(f"{i+1}번째 문자: '{text[i]}'")
print(f"|n총 글자 수는 {len(text)}개야!")
text = "족보세트는 맛있어"

print("🌀 문자 역순으로 출력해볼게!\n")

for i in range(len(text)):
    print(f"{i+1}번째 뒤에서부터 문자: '{text[::-1][i]}'")

print(f"\n✨ 총 글자 수는 {len(text)}개야!")
text = "족보세트는 맛있어"

colors = ["\033[91m", "\033[93m", "\033[92m", "\033[94m", "\033[95m", "\033[96m"]
reset = "\033[0m"

print("🌈 문자 하나씩 색깔 입혀서 출력해볼게!\n")

for i in range(len(text)):
    color = colors[i % len(colors)]  # 색상 반복
    print(f"{color}{i+1}번째 문자: '{text[i]}'{reset}")