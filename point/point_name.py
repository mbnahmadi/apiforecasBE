# import os

# items = os.listdir("D:\\api\\api\\None")
# print (items)












# #Specifying the local path
# #open files in the path(read only)
# #ساختن چنتا لیست متناسب با اسم هر سطون در داده هایمان
# #دیتا رو میریزه تو حلقه میخونه
# #دیتا رو اسپلیت میکنه
# #دیتای مربوط به هر ستون رو داخل لیستی که بالا تعریف کرده اپند می کنه یا شایدم داره فضاهایی رو بهشون اختصاص میده(باید اطلاعات بیشتری کسب شه)
# #همه ی لیست هارو داخل یک دیکشنری میریزه
# #نمیدونم چرا دیکشنری رو مساوی یچیز دگه میذاره
# #حلقه ی فور برای  اینه که دیتا رو اپند کنه؟نمیدونم

# # import numpy as np

# # main_data= np.genfromtxt("None/a.mean",dtype=None, delimiter="")

# # a1 = []
# # a2 = []
# # a3 = []
# # a4 = []
# # a5 = []
# # a6 = []
# # a7 = []

# # # print(type(data))

# # data_dic = {'a1':[],'a2':[],'a3':[],'a4':[],'a5':[],'a6':[],'a7':[]}

# # for data in main_data:
# #     data_dic["a1"].append(data[0])
# #     data_dic["a2"].append(data[1])
# #     data_dic["a3"].append(data[2])
# #     data_dic["a4"].append(data[3])
# #     data_dic["a5"].append(data[4])
# #     data_dic["a6"].append(data[5])
# #     data_dic["a7"].append(data[6])


# station_data = open(f'None/a.mean', 'r').readlines()
# # station_data = station_data[7::]

# a1 = []
# a2 = []
# a3 = []
# a4 = []
# a5 = []
# a6 = []
# a7 = []
# Name = []


# # join 
# for data in station_data:
#     datas = data.split()
#     n = len(datas)
#     a1.append(datas[n-1])
#     a2.append(datas[n-2])
#     a3.append(datas[n-3])
#     a4.append(datas[n-4])
#     a5.append(datas[n-5])
#     a6.append(datas[n-6])
#     a7.append(datas[n-7])
#     text = ""
#     for i in range(0,n-7):
#         text+= datas[i] + ' '
#     Name.append(text)


# data_dic = {'Name':[],'a1':[],'a2':[],'a3':[],'a4':[],'a5':[],'a6':[],'a7':[]}


# #data_dics['Name'] = Name


# for a in Name:
#     data_dic['Name'].append(a)

# for a in a1:
#     data_dic['a1'].append(a)

# for a in a2:
#     data_dic['a2'].append(a)

# for a in a3:
#     data_dic['a3'].append(a)

# for a in a4:
#     data_dic['a4'].append(a)

# for a in a5:
#     data_dic['a5'].append(a)

# for a in a6:
#     data_dic['a6'].append(a)

# for a in a7:
#     data_dic['a7'].append(a)