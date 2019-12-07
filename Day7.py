import intcode
f = open("Day7", "r")
cells = [int(i) for i in f.read().split(',')]
inputs = [5]
outputs = []
code = intcode.intcode(cells)

w = 0
# for i in range(5):
#     code = intcode.intcode(cells)
#     out1 = code.run([i,0])
#     for j in range(5):
#         if i == j:
#             continue
#         code = intcode.intcode(cells)
#         out2 = code.run([j,out1[0]])
#         for k in range(5):
#             if i == k or j == k:
#                 continue
#             code = intcode.intcode(cells)
#             out3 = code.run([k,out2[0]])
#             for l in range(5):
#                 if i == l or j == l or k == l:
#                     continue
#                 code = intcode.intcode(cells)
#                 out4 = code.run([l, out3[0]])
#                 for m in range(5):
#                     if i == m or j == m or k == m or l == m:
#                         continue
#                     code = intcode.intcode(cells)
#                     out5 = code.run([m, out4[0]])
#                     print out5
#                     if out5[0] > w:
#                         w = out5[0]
x = range(5, 10)
for i in x:
    for j in [a for a in x if a not in [i]]:
        for k in [a for a in x if a not in [i, j]]:
            for l in [a for a in x if a not in [i,j,k]]:
                m = 35 - i - j-k-l
                out = [[0], 3]
                a1 = intcode.intcode(cells)
                a2 = intcode.intcode(cells)
                a3 = intcode.intcode(cells)
                a4 = intcode.intcode(cells)
                a5 = intcode.intcode(cells)
                a1.addinputs([i])
                a2.addinputs([j])
                a3.addinputs([k])
                a4.addinputs([l])
                a5.addinputs([m])
                while out[1] ==3 :
                    a1.addinputs(out[0])
                    out = a1.run()
                    a2.addinputs(out[0])
                    out = a2.run()
                    a3.addinputs(out[0])
                    out = a3.run()
                    a4.addinputs(out[0])
                    out = a4.run()
                    a5.addinputs(out[0])
                    out = a5.run()
                    print out
                if out[0] > w:
                    w = out[0]
print w
