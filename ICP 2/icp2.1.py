def main():
    s=input("enter a string")
    k=string_alternative(s)
    return k


def string_alternative(s):
    var=s[::2]
    return var

print(main())
