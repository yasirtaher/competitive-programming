def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')


if __name__ == '__main__':
    print(defangIPaddr("1.1.1.1"))
