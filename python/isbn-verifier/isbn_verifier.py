def verify(isbn):
    isbn = isbn.replace('-', '')
    if not isbn.strip('1234567890X') and isbn.find('X') in [9, -1] and len(isbn) == 10:
        isbn = list(isbn)
        if isbn[9] == 'X':
            isbn[9] = '10'
        return sum(int(x)*y for x, y in zip(isbn, range(1, 11))) % 11 == 0
    else:
        return False
