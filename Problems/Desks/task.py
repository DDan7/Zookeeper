#  Posted from EduTools plugin
cls_1, cls_2, cls_3 = [abs(int(input())),
                       abs(int(input())),
                       abs(int(input()))]

cls1 = ((cls_1 % 2) + cls_1)
cls2 = ((cls_2 % 2) + cls_2)
cls3 = ((cls_3 % 2) + cls_3)

print((cls1 // 2) + (cls2 // 2) + (cls3 // 2))
