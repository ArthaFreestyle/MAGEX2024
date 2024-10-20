def match(kata1,kata2):
    for i in range(1,len(kata2)):
        if kata1[-i:] == kata2[:i]:
            if len(kata2[:i]) >= len(kata2):
                return False
            return True
    return False


N = int(input())

Juan = (input().split())
Hana = (input().split())
Amelia = input().split()

for i in range(N):
    if(not match(Juan[i],Hana[i])):
        print(f"Hana: {Hana[i]}")
        break
    if(not match(Hana[i],Amelia[i])):
        print(f"Amelia: {Amelia[i]}")
        break
    if i < len(Juan) - 1:
        if(not match(Amelia[i],Juan[i+1])):
            print(f"Juan: {Juan[i+1]}")
            break



