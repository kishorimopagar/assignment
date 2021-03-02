def fun1(S):
    for i in range(len(S)):
        if (S[i].isalnum()):
            return True;
            break;
    return False;


def fun2(S):
    for i in range(len(S)):
        if (S[i].isalpha()):
            return True;
            break;
    return False;


def fun3(S):
    for i in range(len(S)):
        if (S[i].isdigit()):
            return True;
            break;
    return False;


def fun4(S):
    for i in range(len(S)):
        if (S[i].islower()):
            return True;
            break;
    return False;


def fun5(S):
    for i in range(len(S)):
        if (S[i].isupper()):
            return True;
            break;
    return False;


if __name__ == '__main__':
    S = "Kishori"

    flagalphanum = fun1(S)
    alphabetical = fun2(S)
    digits = fun3(S)
    lowercase = fun4(S)
    uppercase = fun5(S)
    print(flagalphanum)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)


    