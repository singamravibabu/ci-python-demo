from utils import welcome_user
from math_ops import add, subtract

def main():
    print(welcome_user("Anand"))
    print("Sum:", add(10, 5))
    print("Diff:", subtract(10, 5))

if __name__ == "__main__":
    main()
