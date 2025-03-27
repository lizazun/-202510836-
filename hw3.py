def get_fixed_price(discounted_price):
    return discounted_price / (1 - discount / 100)

discount = int(input("할인율은? ")) 

a_price = int(input("A 상품의 할인된 가격은? "))
b_price = int(input("B 상품의 할인된 가격은? "))

a_fixed = get_fixed_price(a_price)
b_fixed = get_fixed_price(b_price)

print(f"A 상품의 정가는 {int(a_fixed)} 원")
print(f"B 상품의 정가는 {int(b_fixed)} 원")
