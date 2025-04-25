def print_gugudan(start, end):
    for i in range(1, 10): 
        for dan in range(start, end + 1):  
            print(f"{dan}x{i}={dan*i:2}", end="\t") 
        print() 

print_gugudan(2, 5)
print()  

print_gugudan(6, 9)
