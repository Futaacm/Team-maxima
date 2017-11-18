N= raw_input('Enter the list of Players >> ')
N_list= N.split(' ')
finalist=[]
for player in N_list:
    i_list= N_list[:]
    i_list.remove(player)
    join_i =''.join(i_list)
    c=list(player)
    new_i=[]
    for j in player:
        if j in join_i:
            new_i.append(j)
    
    if new_i== c:
        x=''.join(new_i)
        finalist.append(x)

if len(finalist)==0:
    print 'No Match'
else:
    for i in finalist:
        print i
    
        

