import random, numpy, math, copy, matplotlib.pyplot as plt
cities = [random.sample(range(100), 2) for x in range(15)];
n=15
tour = random.sample(range(n),n);
d=1
v=1
a=2
while d >0: 
    
    [i,j] = sorted(random.sample(range(n),2))
    [z,w] = sorted(random.sample(range(n),2))

        
        #i
        #j =i+1
        #z=i+2
        #w=i+3

    newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];    
    x=cities[tour[j]][0] - cities[tour[z]][0]
    p=cities[tour[i]][0] - cities[tour[w]][0]
    x1=cities[tour[j]][1] - cities[tour[w]][1]
    p1=cities[tour[i]][1] - cities[tour[z]][1]
    
    if x<0 and p<0:
        if ( sum([ math.sqrt(sum([(cities[tour[(k+1) % n]][d] - cities[tour[k % n]][d])**2 for d in [0,1] ])) 
        for k in [j,j-1,i,i-1]]) - sum([ math.sqrt(sum([(cities[newTour[(k+1) % n]][d] - cities[newTour[k % n]][d])**2 
                 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) > 0:
             tour=copy.copy(newTour)
             plt.plot([cities[tour[i % 15]][0] for i in range(16)], [cities[tour[i % 15]][1] for i in range(16)], 'xb-');
             plt.show()
    
    if x1<0 and p1<0:
        if ( sum([ math.sqrt(sum([(cities[tour[(k+1) % n]][d] - cities[tour[k % n]][d])**2 for d in [0,1] ])) 
        for k in [j,j-1,i,i-1]]) - sum([ math.sqrt(sum([(cities[newTour[(k+1) % n]][d] - cities[newTour[k % n]][d])**2 
                 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) > 0:
             tour=copy.copy(newTour)
             plt.plot([cities[tour[i % 15]][0] for i in range(16)], [cities[tour[i % 15]][1] for i in range(16)], 'xb-');
             plt.show()
   
    if a ==15:
        a=2
    else:
        a = a+1
     #print(tour)
        #d=0
#    if x<0:
#        if y<0:
#            tour=newTour
#    else:
#        d=1
#    for k in [j,j-1,i,i-1]]
#for temperature in numpy.logspace(0,5,num=100000)[::-1]:
#    
#	[i,j] = sorted(random.sample(range(15),2));
#	newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];
#	if math.exp( ( sum([ math.sqrt(sum([(cities[tour[(k+1) % 15]][d] - cities[tour[k % 15]][d])**2 for d in [0,1] ])) 
#    for k in [j,j-1,i,i-1]]) - sum([ math.sqrt(sum([(cities[newTour[(k+1) % 15]][d] - cities[newTour[k % 15]][d])**2 for d in [0,1] ])) 
#    for k in [j,j-1,i,i-1]])) / temperature) > random.random():
#		tour = copy.copy(newTour);
#plt.plot([cities[tour[i % 15]][0] for i in range(16)], [cities[tour[i % 15]][1] for i in range(16)], 'xb-');
#plt.show()