def countdown(n):
    if n == 0:
        print("Base case reached, returning")
        return

    print("Entering:", n)
    countdown(n - 1)
    print("Leaving:", n)

if __name__ == "__main__":
    countdown(5000**1000000000)