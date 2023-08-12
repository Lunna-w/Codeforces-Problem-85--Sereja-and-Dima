n = int(input())
cards = list(map(int, input().split()))

sereja_score = 0
dima_score = 0

left, right = 0, n-1  

is_sereja_turn = True

while left <= right:

    if cards[left] >= cards[right]:
        if is_sereja_turn:
            sereja_score += cards[left]
        else:
            dima_score += cards[left]
        left += 1
    else:
        if is_sereja_turn:
            sereja_score += cards[right]
        else:
            dima_score += cards[right]
        right -= 1

    is_sereja_turn = not is_sereja_turn

print(sereja_score, dima_score)