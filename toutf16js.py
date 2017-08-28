def main():
    code = raw_input("code to utf16js?")
    print ''.join(["\\x00\\x%02x" % ord(c) for c in code])

if __name__ == "__main__":
    main()
