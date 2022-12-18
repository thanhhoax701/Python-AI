def check_prefix(wi: str, wj: str):
    if len(wi) <= len(wj):
        return None

    pos = wi.find(wj)
    if pos != 0:
        return None
    
    res = wi[pos+len(wj):]
    if not res:
        return None
    return res

def check_indecipherable(S: list, k: int) -> bool:
    tmp = S[k] & S[0]
    if len(tmp) > 0:
        print("\n\tS{} & S0 = {}".format(k, tmp))
        return True
    return False

def check_decipherable(S: list, k: int) -> bool:
    if len(S[k]) == 0:
        return True
    for i in range(k):
        if S[k] == S[i]:
            print("\n\tS{} == S{}".format(k, i))
            return True
    return False

def find_Sk(S: list, k: int) -> set:
    res = set()
    for w in S[0]:
        for C in S[k-1]:
            if len(w) > len(C):
                wi, wj = w, C
            else:
                wi, wj = C, w

            tmp = check_prefix(wi, wj)
            
            if tmp != None and tmp not in res:
                print("\t{}\t= {}\t{}".format(wi, wj, tmp))
                res.add(tmp)
    return res

def main() -> None:
    W = {"a", "c", "ad", "abb", "bad", "deb", "bbcde"}
    # W = {"010", "0001", "0110", "1100", "00011", "00110", "11110", "101011"}
    S = list()

    print("W: {}".format(W))

    S.append(W.copy())
    k = 1
    while k < 10:
        print()
        S.append(find_Sk(S, k))
        print("S{}: {}".format(k, S[k]))

        if check_indecipherable(S, k):
            print("Indecipherable")
            break
        elif check_decipherable(S, k):
            print("Decipherable")
            break

        k = k+1

if __name__ == "__main__":
    main()