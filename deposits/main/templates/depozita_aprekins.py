deposit= float(input('Input deposit:'))
term= int(input('Term:'))
interest=float(input('Input interest:'))

interest_in_period=0
sum=0


for i in range(1,term+1):
    interest_in_period=deposit*interest
    deposit=deposit+interest_in_period
    sum=sum+interest_in_period
print('Interest:',sum)




