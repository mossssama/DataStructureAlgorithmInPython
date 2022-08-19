def countSort(unsorted):
    tempP=[]; tempN=[];  sortedP=unsorted.copy(); sortedN=unsorted.copy();  n=p=0

    for i in range(max(unsorted)+1):        # temp=[0,0,0,0] size=max+1
        tempP.append(0)                     
    for i in range(-min(unsorted)+1):
        tempN.append(0)                   

    for i in unsorted:                      # calculating duplication number
        if i>=0:
            tempP[i]+=1              
        else:
            tempN[-i]+=1  

    for i in range(1,max(unsorted)+1):      # calculating progressive duplication
        tempP[i]+=tempP[i-1]
    for i in range(1,-min(unsorted)+1): 
        tempN[i]+=tempN[i-1]

    for i in unsorted:                      # building sorted lists
        if i>=0:
            sortedP[tempP[i]-1]=i;    tempP[i]-=1;   p+=1
        else:               
            sortedN[tempN[-i]-1]=i;   tempN[-i]-=1;   n+=1
    
    for i in range(len(unsorted)-p):        # deleting unwanted items
        sortedP.pop()
    for i in range(len(unsorted)-n):
        sortedN.pop()

    sortedN.reverse();    sortedN.extend(sortedP);  del unsorted,sortedP,tempP,tempN;  return sortedN;


#driver program
arr=[-4,6,-7,10,5,-11,3,21,-6,15,9]
print("The unsorted list: ",arr)
print("The sorted list: ",countSort(arr))
