# Using Walrus operator " := "
if (n := len([1,2,3,4,5]))>3:
    print(f"List is too long ({n} Elements, but allowed only <=3 ) ")
# Means by suing 'Walrus operator := ' you can compare and assign a value in a single line