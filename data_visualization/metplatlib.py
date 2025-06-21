import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[10,30,20,15]
# plt.plot(x,y)
# plt.show()

# x=['Mon','Tues','Wed','Thus','Fri']
# y=[10,21,5,6,12]
# plt.title('Bakery Sales')
# plt.xlabel('Days of Week')
# plt.ylabel('Sales per day')
# plt.plot(x,y)
# plt.show()

# months=[1,2,3,4]
# sales=[1000,1500,1200,1890]
# plt.plot(months,sales,color='red',linestyle='--',linewidth=2 , marker='o',label='Sales Of Months')
# plt.xlabel("Months")
# plt.ylabel("Sales Per Month")
# plt.title("Monthly Sales Data Report")
# plt.legend(loc="lower right" , fontsize=22)
# plt.grid(color="blue",linestyle=":",linewidth="1")
# plt.xlim(1,4)
# plt.ylim(0,2000)
# plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
# plt.show()

# products=['A','B','C','D']
# sales=[1000,1200,800,1230]
# plt.bar(products,sales,color='orange',label='Sales of products')
# plt.xlabel('Products')
# plt.ylabel('Sales of products')
# plt.title('Sales of products')
# plt.legend()
# plt.show()




# products=['A','B','C','D']
# sales=[1000,1200,800,1230]
# plt.barh(products,sales,color='orange',label='Sales of products')
# plt.xlabel('Products')
# plt.ylabel('Sales of products')
# plt.title('Sales of products')
# plt.legend()
# plt.show()

# regions=['North','East','West','South']
# revenue=[1000,1200,399,2001]
# plt.pie(revenue,labels=regions,colors=['red','blue','green','purple'], autopct='%1.1f%%')
# plt.title('Revenue Contribution By Region')
# plt.legend()
# plt.show()

# scores=[73, 58, 41, 67, 85, 39, 76, 62, 49, 88,
# 33, 70, 45, 53, 60, 81, 36, 66, 90, 47,
# 55, 37, 78, 72, 40, 84, 63, 59, 35, 68

# ]

# plt.hist(scores,bins=5,color='purple',edgecolor='black', label='Scores Of Students')
# plt.xlabel('Scores')
# plt.ylabel('Number Of Students')
# plt.legend()
# plt.show()

# hours=[1,2,3,4,5,6,7,8]
# marks=[10,20,30,40,50,60,70,80]
# plt.scatter(hours,marks,color='green',marker='o', label='Marks Obtained')
# plt.xlabel('Hours Studied')
# plt.ylabel('Marks Obtained')
# plt.legend()
# plt.grid(True)
# plt.title('Hours Studied RelationShip To Marks ')
# plt.show()

# plt.scatter([1,2,3],[50,55,60],color='orange',label='Class A')
# plt.scatter([1,2,3],[45,55,65],color='red',label='Class B')
# plt.xlabel('Hours Studied')
# plt.ylabel('Marks Obtained')
# plt.legend()
# plt.grid(True)
# plt.title('Hours Studied RelationShip To Marks ')
# plt.show()

# x=[1,2,3,4]
# y=[10,20,15,30]
# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.title('Line Chart')

# plt.subplot(1,2,2)
# plt.bar(x,y)
# plt.title('Bar Chart')
# plt.tight_layout()
# plt.show()

# x=[1,2,3,4]
# y=[10,20,15,30]
# fig, ax=plt.subplots(1,2 , figsize=(10,5))

# ax[0].plot(x,y)
# ax[0].set_title('Line Chart')

# ax[1].bar(x,y)
# ax[1].set_title('Bar Chart')
# fig.suptitle('Comparision Of Line And Bar Charts')
# plt.tight_layout()
# plt.show()

x=[1,2,3,4]
y=[10,20,30,40]

plt.plot(x,y,color='orange',marker='o')
plt.xlabel('X-Axis')
plt.ylabel('Y_Axis')
plt.title('Graphs')
plt.savefig('graph.jpg',dpi=300,bbox_inches='tight')
plt.show()