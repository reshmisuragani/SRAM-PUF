#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os 
import numpy as np
import matplotlib.pyplot as plt
cwd = os.getcwd()

#hextobin function converts 32 bit hexa decimal numbers from "/hex" folder to 32 bit binary in "/binOutput" folder
def hextobin():    
    name = []
    for file in os.listdir(cwd+"/hex/"):
        if file.endswith(".txt"):
            name.append(file)
    scale = 16
    num_of_bits = 32
    counter = 0
    for v in name:
        f = open(cwd+"/hex/"+v, "r")
        f = [x.strip() for x in f]
        convert = []
        for a in f:
            convert.append(bin(int(a, scale))[2:].zfill(num_of_bits))
        result = ""
        i = 1;
        for a in convert:
            for b in a:
                result += b + ""
            if i % 1 == 0:
                result += "\n"
            i += 1
        print(result)
        counter +=1
    
        f3=open(cwd+"/binOutput/%s" %v, 'w')
        f3.write("%s" %result)
        f3.close()   
    print("%d files have been converted" %counter)
    #with open(cwd+"/binOutput/%s" %v, 'w') as f1:
        #print("%s" %result, file=f1)

        


#Calculates Hamming weight and shannon entropy for all the files in "/binOutput" folder and stores in "Output/hammingweight_shannonentropy.txt"
def Hamming_shannon():    
    name = []
    hammingweight = []
    shannonentropy = []
    for file in os.listdir(cwd+"/hex/"):
        if file.endswith(".txt"):
            name.append(file)
    #bits=1200*32
    f1=open("Output/hammingweight_shannonentropy.txt", "w")
    for v in name:
        bits=sum(1 for line in open(cwd+"/binOutput/%s" %v))*32
        f = open(cwd+"/binOutput/"+v, "r")
        f = [x.strip() for x in f]
        result = []

        i = 1;
        for a in f:
           for b in a:
               result += b + ""
           if i % 1 == 0:
               result += ""
           i += 1
    
        #calculation of Hamming weight
        x = result.count("0")
        y = result.count("1")
        hw=(y/bits)*100
        print("number of zero:",x)
        print("number of ones:",y)
        z = x/(x+y)
        print("Hamming weight of %s : %.2f" %(v,hw)+" %")
        f1.write("Hamming weight of %s \t: %.2f" %(v,hw)+" %\n")
        hammingweight.append(hw)
        
        #calculation of shannon entropy

        a = np.array([z, 1-z])
        #print("Original array:")
        #print(a)
        b = a*(np.log2(a))
        #print(b)
        print("Shannon entropy of %s : %f \n" %(v,-np.sum(b)))    
        f1.write("Shannon entropy of %s \t: %f \n\n" %(v,-np.sum(b)))
        shannonentropy.append(-np.sum(b))
    
    
    plt.scatter(hammingweight,name)
    plt.xlim(40, 58)
    plt.ylabel('Device Name')
    plt.xlabel('Hamming weight in %')
    plt.title('Hamming weight of %d devices' %(len(name)))
    plt.savefig('Output/Hamming weight.png')
    plt.show()
    
    plt.gcf().clear()
    
    plt.scatter(shannonentropy,name)
    plt.xlim(.99, 1.003)
    plt.ylabel('Device Name')
    plt.xlabel('Shannon Entropy (max=1)')
    plt.title('Shannon Entropy of %d devices' %(len(name)))
    plt.savefig('Output/Shannon Entropy.png')
    plt.show()
    
    f1.close()


# Calculates Inter and Intra hamming distance for all the files in "/binOutput" and stores in "/Output/Inter_Intra_HammingDistance.txt"

def Hamming_distance():    
    name = []
    Inter = []
    Intra = []
    Intra_name =[]
    Inter_name = []
    for file in os.listdir(cwd+"/binOutput/"):
        if file.endswith(".txt"):
            name.append(file)
        
    #q = len(name)
    #h = int(q/2)
    #bits=1200*32
    #w=0
    f3=open("Output/Inter_HammingDistance.txt", "w")
    f3.write("Inter Hamming distance between\n")
    f4=open("Output/Intra_HammingDistance.txt", "w")
    f4.write("Intra Hamming distance between\n")
    print("Hamming distance between\n")
    for v in name:
        bits=sum(1 for line in open(cwd+"/binOutput/%s" %v))*32
        f1 = open(cwd+"/binOutput/"+v,"r")
        f1 = [x.strip() for x in f1]
        result1 = []
        i = 1;
        for a in f1:
            for b in a:
                result1 += b + ""
            if i % 1 == 0:
                result1 += ""
            i += 1
        
        for g in name:
            f2 = open(cwd+"/binOutput/"+g, "r")
            f2 = [x.strip() for x in f2]
            result2 = []
            i = 1;
            for a in f2:
                for b in a:
                    result2 += b + ""
                if i % 1 == 0:
                    result2 += ""
                i += 1
            
            len1,len2 = len(result1),len(result2)
        
            if len1 != len2:
                print("array count does not match")
                #print(len1,len2)
            
            else:        
                d=0
                for j in range(len1):
                    if result1[j] != result2[j]:
                        d+=1
                
                if ((d/bits*100)<10):
                    
                    #if((v == g) & (Intra[w] == (d/bits*100))):
                    if(v == g):
                        f4.write("%s vs %s\t:\t%.2f" %(v,g,d/bits*100)+" %\tBoth files are identical\n")
                        print("%s vs %s\t:\t%.2f" %(v,g,d/bits*100)+" %\tBoth files are identical")
                                            
                    else:
                        Intra.append(d/bits*100)
                        Intra_name.append("%s vs %s" %(v,g))
                        print("%s vs %s\t:\t%.2f" %(v,g,d/bits*100)+" %\t<--Intra Hamming Distance")
                        f4.write("%s vs %s\t:\t%.2f" %(v,g,d/bits*100)+" %\n")
                    
                else:
                    Inter.append(d/bits*100)
                    Inter_name.append("%s vs %s" %(v,g))
                    print("%s vs %s\t:\t%.2f" %(v,g,d/bits*100)+" %\t<--Inter Hamming Distance")
                    f3.write("%s vs %s\t:\t%.2f" %(v,g,d/bits*100)+" %\n")
                
                
        
    print("\nInter and Intra Hamming distance of %d files are stored in %s/Output/Inter_Intra_HammingDistance.txt" %(len(name),cwd))
    

    #Intra = list(dict.fromkeys(Intra))
    #Intra_name = list(dict.fromkeys(Intra_name))
    f3.close()
    f4.close()
    
    _1 = plt.scatter(Intra,Intra_name)
    #plt.xlim(40, 58)
    _1 = plt.ylabel('Device Name')
    _1 = plt.xlabel('Intra Hamming distance in %')
    _1 = plt.title('Intra Hamming distance of %d devices' %(len(Intra_name)))
    _1 = plt.savefig('Output/Intra Hamming distance.png')
    _1 = plt.show()
    
    _2 = plt.scatter(Inter,Inter_name)
    #plt.xlim(40, 58)
    _2 = plt.ylabel('Device Name')
    _2 = plt.xlabel('Inter Hamming distance in %')
    _2 = plt.title('Inter Hamming distance of %d devices' %(len(Inter_name)))
    _2 = plt.gca()
    #_2.axes.get_xaxis().set_visible(False)
    _2.axes.get_yaxis().set_visible(False)
    _2 = plt.savefig('Output/Inter Hamming distance.png')
    _2 = plt.show()


#hextobin()
#Hamming_shannon()
#Hamming_distance()


# In[ ]:




