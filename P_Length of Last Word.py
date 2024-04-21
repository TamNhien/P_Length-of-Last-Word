def length_of_last_word(s):
    return len(s.strip().split()[-1]) if s.strip() else 0

s = input("Nhap chuoi: ")
result = length_of_last_word(s)

print("Độ dài của từ cuối cùng trong chuỗi là: ", result)