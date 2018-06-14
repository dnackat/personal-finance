# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Dileep Nackathaya

This script has a function to generate plots for the two investment 
options in 'finance.py'. This script is imported as a module in that script. 

Terminology used in this script is as follows:

C_x = Starting account balance in account x
P_x = Initial amount for FD account x
A_x = Current account balance in account x (Calculated)
m_x = Recurring monthly payment of account x 
r_x = Interest rate of account x
n_d = Number of times interest is compunded for deposit accounts in a year
N_x = Number of instalments for deposit account (or number of months)
FD1 = 4,00,000 fixed deposit account
FD2 = 2,00,000 fixed deposit account
RD = Recurring deposit

"""
import numpy as np, matplotlib.pyplot as plt

#Function to generate plots
def finplots(option):
#%%Option 1
    if (option == '1'):
    
    #Initialize some parameters
        #RD inputs
        A_rd = 0.0
        i_rd = 0.0
        m_rd = 75000.0
        r_rd = 8.5/100.0
        A_nre = 11326.0
        N_rd = 36
        #FD1 inputs
        P_fd1 = 400000.0
        r_fd1 = 7.75/100.0
        N_fd1 = 15
        #FD2 inputs
        P_fd2 = 200000.0
        r_fd2 = 7.5/100.0
        N_fd2 = 15
        #NRE inputs
        N_nre = 9
        r_nre = 4.0/100.0
        i_nre = 0.0
        #Quarterly compounding
        n_d = 4
    
    #Start loop for RD
        i_rd_plot = []
        A_rd_plot = []
        for i in range(N_rd):
            
            if (((i+1) > 3 and ((i+1) % 3 == 1)) or ((i+1) == N_rd)):
                A_rd += m_rd + i_rd
                i_rd = A_rd*r_rd*(1.0/12.0)
                if ((i+1) == N_rd):
                    A_rd += i_rd
            else:
                A_rd += m_rd
                i_rd += A_rd*r_rd*(1.0/12.0)
                
            if (i >= 27):
                i_rd_plot += [i-26]
                A_rd_plot += [A_rd/1e5]
    
    #Start loop for FD1 - To be closed in July
        for j in range(N_fd1):
            j1 = j+1
            A_fd1 = P_fd1*(1+(r_fd1/n_d))**(n_d*(j1/12.0))
        
    #Start loop for FD2 - To be closed end of November
        i_fd2_plot = []
        A_fd2_plot = []
        for k in range(N_fd2):
            k1 = k+1
            A_fd2 = P_fd2*(1+(r_fd2/n_d))**(n_d*(k1/12.0))
            
            if (k >= 9):
                i_fd2_plot += [k-8]
                A_fd2_plot += [A_fd2/1e5]
        
    #Start loop to track NRE account balance - July, 2017 through March, 2018
        i_nre_plot = []
        A_nre_plot = []
        for m in range(N_nre):
            
            m1 = m+1
        
            if(m == 0):        #Add FD1 amount to NRE account in July
                A_nre += A_fd1

            if(m == 6):        #Add FD2 amount to NRE account in December
                A_nre += A_fd2
            
            if (m < 9):    
                A_nre -= m_rd
        
            if ((m1 > 3) and (m1 % 3 == 1)):
                A_nre += i_nre
                i_nre = A_nre*r_nre*(1.0/12.0)
            else:
                i_nre += A_nre*r_nre*(1.0/12.0)
            
            i_nre_plot += [m+1]
            A_nre_plot += [A_nre/1e5]
        
    #Start loop for total balance  
        A_total = []
        for n in range(9):
            if (n < 6):
                A_total += [A_rd_plot[n] + A_fd2_plot[n] + A_nre_plot[n]]
            else:
                A_total += [A_rd_plot[n] + A_nre_plot[n]]
    
    #Convert lists into arrays     
        i_nre_plot = np.array(i_nre_plot)
        A_nre_plot = np.array(A_nre_plot)    
        i_fd2_plot = np.array(i_fd2_plot)
        A_fd2_plot = np.array(A_fd2_plot)
        i_rd_plot = np.array(i_rd_plot)
        A_rd_plot = np.array(A_rd_plot)        
        A_total = np.array(A_total)
        
    #Generate plot
        plt.figure('Option 1 Plot')
        plt.plot(i_rd_plot,A_rd_plot,'g-o',linewidth=1,label='RD Balance')
        plt.plot(i_fd2_plot,A_fd2_plot,'b-o',linewidth=1,label='FD2 Balance')
        plt.plot(i_nre_plot,A_nre_plot,'k--o',linewidth=1,label='SB Balance')
        plt.plot(i_nre_plot,A_total,'r-o',linewidth=2,label='Total Amount')
        plt.xlabel('Month',weight='bold',size=12)
        plt.ylabel('Account Balance (lakhs)',weight='bold',size=12)
        plt.title('Option 1 (July, 17 through March, 18)',\
                  weight='bold', size=16)
        plt.xticks(np.arange(0,10,3))
        plt.legend(loc='best')
        #plt.savefig('Plot-Option1.pdf')
        
#%% Option 2
    elif (option == '2'):
    
    #Initialize some parameters
        #RD inputs
        A_rd = 0.0
        i_rd = 0.0
        m_rd = 75000.0
        r_rd = 8.5/100.0
        A_nre = 11326.0
        N_rd = 33
        N_rd1 = 2
        #FD1 inputs
        P_fd1 = 400000.0
        r_fd1 = 7.75/100.0
        N_fd1 = 15
        #FD2 inputs
        P_fd2 = 200000.0
        r_fd2 = 7.5/100.0
        N_fd2 = 18
        #NRE inputs
        N_nre = 9
        r_nre = 4.0/100.0
        i_nre = 0.0
        #Quarterly compounding
        n_d = 4
    
    #Start loop for RD - Last payment in december, 2017
        i_rd_plot = []
        A_rd_plot = []
        for i in range(N_rd):
            
            if (((i+1) > 3 and ((i+1) % 3 == 1)) or ((i+1) == N_rd)):
                A_rd += m_rd + i_rd
                i_rd = A_rd*r_rd*(1.0/12.0)
                if ((i+1) == N_rd):
                    A_rd += i_rd
            else:
                A_rd += m_rd
                i_rd += A_rd*r_rd*(1.0/12.0)
                
            if (i >= 27):
                i_rd_plot += [i-26]
                A_rd_plot += [A_rd/1e5]
        
        for i2 in range(N_rd1):
            A_rd1 = A_rd*(1+(r_rd/n_d))**(n_d*((i2+1)/12.0))
            i_rd_plot += [i2+7]
            A_rd_plot += [A_rd1/1e5]
    
    #Start loop for FD1 - To be closed in July
        for j in range(N_fd1):
            j1 = j+1
            A_fd1 = P_fd1*(1+(r_fd1/n_d))**(n_d*(j1/12.0))
        
    #Start loop for FD2 - Until March, 2018
        i_fd2_plot = []
        A_fd2_plot = []
        for k in range(N_fd2):
            k1 = k+1
            A_fd2 = P_fd2*(1+(r_fd2/n_d))**(n_d*(k1/12.0))
            
            if (k >= 9):
                i_fd2_plot += [k-8]
                A_fd2_plot += [A_fd2/1e5]
        
    #Start loop to track NRE account balance - July, 2017 through March, 2018
        i_nre_plot = []
        A_nre_plot = []
        for m in range(N_nre):
            
            m1 = m+1
        
            if(m == 0):        #Add FD1 amount to NRE account in July
                A_nre += A_fd1
            elif(m == 8):
                A_nre += A_rd1
        
            if(m <= 5):  #Deduct RD monthly payment from NRE account until December
                A_nre -= m_rd
        
            if ((m1 > 3) and (m1 % 3 == 1)):
                A_nre += i_nre
                i_nre = A_nre*r_nre*(1.0/12.0)
            else:
                i_nre += A_nre*r_nre*(1.0/12.0)
            
            i_nre_plot += [m+1]
            A_nre_plot += [A_nre/1e5]
            
    #Start loop for total balance  
        A_total = []
        for n in range(9):
            if (n < 8):
                A_total += [A_rd_plot[n] + A_fd2_plot[n] + A_nre_plot[n]]
            else:
                A_total += [A_fd2_plot[n] + A_nre_plot[n]]
            
    #Convert lists into arrays     
        i_nre_plot = np.array(i_nre_plot)
        A_nre_plot = np.array(A_nre_plot)    
        i_fd2_plot = np.array(i_fd2_plot)
        A_fd2_plot = np.array(A_fd2_plot)
        i_rd_plot = np.array(i_rd_plot)
        A_rd_plot = np.array(A_rd_plot)        
        A_total = np.array(A_total)
        
    #Generate plot
        plt.figure('Option 2 Plot')
        plt.plot(i_rd_plot,A_rd_plot,'g-o',linewidth=1,label='RD Balance')
        plt.plot(i_fd2_plot,A_fd2_plot,'b-o',linewidth=1,label='FD2 Balance')
        plt.plot(i_nre_plot,A_nre_plot,'k--o',linewidth=1,label='SB Balance')
        plt.plot(i_nre_plot,A_total,'r-o',linewidth=2,label='Total Amount')
        plt.xlabel('Month',weight='bold',size=12)
        plt.ylabel('Account Balance (lakhs)',weight='bold',size=12)
        plt.title('Option 2 (July, 17 through March, 18)',\
                  weight='bold', size=16)
        plt.xticks(np.arange(0,10,3))
        plt.legend(loc='best')
        #plt.savefig('Plot-Option2.pdf')
    
#**************************************************************************# 