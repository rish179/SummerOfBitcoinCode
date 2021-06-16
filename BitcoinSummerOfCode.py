import csv
path ="C:\\Users\\rishabh\\Downloads\\summerofbitcoin_challenge\\mempool.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
data=[]
for row in reader:
    tx_id = row[0]
    fee = int(row[1])
    weight1 = int(row[2])
    parent = row[3]
    data.append([tx_id,fee,weight1,parent])
fee=[]
weight=[]
tx_id = []
parent = []
for f in data:
    for j in f:
        c=f[1]
        d=f[2]
        e=f[0]
        pp=f[3]
    fee.append(c)
    weight.append(d)
    tx_id.append(e)
    parent.append(pp)
limit = 4000000
sum_w = 0
sum_f = 0
list_tx = []

def tx_search(txn,direc):
    for i in  direc:
        if(txn == i):
            flag = 1
        else:
            flag = 0
        return flag

limit = 4000000
def max_func(n,fee1,weigh):
    sum1=0
    sum2=0
    ans=0
    wei=0
    p1=0
    p2=0
    while (p2<n):
        if(parent[p2] == ''):
            sum1 = sum1 + fee1[p2]
            sum2 = sum2 + weigh[p2]
            list_tx.append(tx_id[p2])
            p2=p2+1
            
        else:
            transaction = parent[p2]
            if(tx_search(transaction, list_tx) == 1):
                sum1 = sum1 + fee1[p2]
                sum2 = sum2 + weigh[p2]
                list_tx.append(tx_id[p2])
                p2=p2+1
            else:
                p2=p2+1        
        
        while (sum2>limit and p1<p2):
            if(parent[p1] == ''):
                sum1-=fee[p1]
                sum2-=weigh[p1]
                if(ans < sum1):
                    list_tx.remove(tx_id[p1])
                p1=p1+1
            else:
                if(tx_search(tx_id[p1], list_tx) == 1):
                    sum1-=fee[p1]
                    sum2-=weigh[p1]
                    if(ans < sum1):
                        list_tx.remove(tx_id[p1])
                    p1=p1+1
                else:
                    p1=p1+1
        ans=max(ans,sum1)
        wei=max(wei,sum2)

    while (p1<n):
        if(parent[p1] == ''):
            sum1-=fee[p1]
            sum2-=weigh[p1]
            if(ans < sum1):
                list_tx.remove(tx_id[p1])
            p1=p1+1
        else:
            if(tx_search(tx_id[p1], list_tx) == 1):
                sum1-=fee[p1]
                sum2-=weigh[p1]
                if(ans < sum1):
                    list_tx.remove(tx_id[p1])
                p1=p1+1
            else:
                p1=p1+1
        
        if (sum2<=limit):
            ans=max(ans,sum1)
            wei = max(wei,sum2)

    return ans,wei
a,b=max_func(len(fee),fee,weight)
print(a,b)
fil =  open('block.txt','w') 
for items in list_tx:
    fil.writelines([items])
    fil.write('\n')
file.close()
