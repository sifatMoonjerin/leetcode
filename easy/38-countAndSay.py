def countAndSay(n):
    op = '1'
    for _ in range(1, n):
        prev = list(op)
        count = 1
        cur = prev[0]
        op = ''

        for num in prev[1:]:
            print(num, cur)
            if num != cur:
                op += (str(count)+cur)
                count = 1
                cur = num
            else:
                count += 1
        op += (str(count)+cur)

    return op


#         if n == 1: return str(1)

#         prev = list(countAndSay(n-1))
#         count = 1
#         cur = prev[0]
#         op = ''

#         for num in prev[1:]:
#             if num != cur:
#                 op += (str(count)+cur)
#                 count = 1
#                 cur = num
#             else:
#                 count += 1

#         return op + (str(count)+cur)
