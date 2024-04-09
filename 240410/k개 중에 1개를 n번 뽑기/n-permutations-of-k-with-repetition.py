k , n = map(int, input().split())
answer = []
cnt = 0
def print_answer():
    for num in answer:
        print(num, end=" ")
    print()
def Choose(cnt):
    if cnt==n:
        print_answer()
        return
    for i in range(1, k+1):
        answer.append(i)
        Choose(cnt+1)
        answer.pop()

    return

Choose(cnt)