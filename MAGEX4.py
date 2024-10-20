def hitung_titik_diterangi(N, menara):

    interval = []

    for x, r in menara:
        interval.append((x - r, x + r))

    interval.sort()

    total_terang = 0
    start, end = interval[0]
    

    for i in range(1, N):
        curr_start, curr_end = interval[i]
        if curr_start <= end:

            end = max(end, curr_end)
        else:
           
            total_terang += end - start + 1

            start, end = curr_start, curr_end
    
 
    total_terang += end - start + 1
    
    return total_terang


N = int(input().strip())  
menara = [tuple(map(int, input().split())) for _ in range(N)] 


print(hitung_titik_diterangi(N, menara))