def solution(phone_book):
    phone_book.sort()
    for idx in range(1, len(phone_book) - 1):
        if phone_book[idx].startswith(phone_book[idx - 1]) or phone_book[idx + 1].startswith(phone_book[idx]):
            return False

    return True


solution(["119", "97674223", "1195524421"])
solution(["123", "456", "789"])
print(solution(["123", "4565", "456"]))
