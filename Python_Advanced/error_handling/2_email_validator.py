class MustContainAtSymbolError(Exception):
    """Raised when missing @"""
    pass


class NameTooShortError(Exception):
    """Raised when name length is less or equal to 4"""
    pass


class InvalidDomainError(Exception):
    """Raised when domain not in domain lists"""
    pass


def split_verification():
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        valid["split_verification"] = True


def length_verification():
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    else:
        valid["length_verification"] = True


def domain_verification():
    if domain not in domain_list:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        valid["domain_verification"] = True


def split(word, by_sign):
    return word.split(by_sign)


valid = {
    "split_verification": False,
    "length_verification": False,
    "domain_verification": False
}

domain_list = ["com", "bg", "net", "org"]

email = input()
while email != "End":
    split_verification()

    email = split(email, "@")
    name = email[0]
    full_domain = split(email[1], ".")
    domain = full_domain[1]

    length_verification()
    domain_verification()

    if all(valid):
        print("Email is valid")

    email = input()


