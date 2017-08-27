def main():
    code = raw_input("str to number?")
    nums = [ord(c) for c in code]
    print(nums)

if __name__ == "__main__":
    main()
