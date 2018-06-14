# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Dileep Nackathaya

This script compares two investment options:

1. Option 1 is to close FD1 in July and move it to NRE account, close FD2 in 
December and move it to NRE accont end of December, and continue RD account 
through to maturity.

2. Option 2 is to close FD1 in July and move it to NRE account, 
close RD in December and let it stay in the account until March, 2018 and 
continue FD2 account through to maturity.

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
#**************************************************************************#
# Define inputs                                                            #
#**************************************************************************#

import finance_plot

#RD account
C_rd = 2192134
m_rd = 75000
r_rd = 8.5/100.0

# FD1 account
C_fd1 = 439723
P_fd1 = 400000
r_fd1 = 7.75/100.0

#FD2 account
C_fd2 = 211594
P_fd2 = 200000
r_fd2 = 7.5/100.0

#SB account
C_nre = 11326
r_nre = 4.0/100.0

#Quarterly compounding for deposit accounts
n_d = 4

############################################################################
#                                                                          # 
# Do not edit anything below this line unless you know what you are doing! #
#                                                                          #
############################################################################

#Prompt for investment option and check if input is okay
invalinp = True
while (invalinp == True):
    try:
        option = input("Select investment option (1 or 2): --> ")
        int(option)
    except:
        print("Please input a numeric value (1 or 2)!")
        continue
    if (int(option) == 1 or int(option) == 2):
        invalinp = False
    else:
        print("Please select 1 or 2.")
               
#Prompt for option to generate a plot and check if input is okay
invalinp = True
while (invalinp == True):
    plot = input("Do you wish to generate a plot (y or n)? --> ")
    if (plot == 'y' or plot == 'n'): 
        break
    else: 
        print('\nInvalid input! Please select y or n (lowercase).\n')
      
#Month list for printing    
month = ['January','February','March','April','May','June','July','August'\
         ,'September','October','November','December']

#%% Option 1 

if (option == '1'):
    
    opt1_start_amt = C_rd+C_fd1+C_fd2+C_nre
    
    print("//*************************************************************"\
          "************************************//\n")
    
    print("Option 1 is to close FD1 in July and move it to NRE account, "\
          "close FD2 in December and move it to NRE accont end of December, "\
          "and continue RD account through to maturity.\n")
    
    print("**--------------------------------------------------------------"\
              "---------**\n")
    
    print("Option 1 start amount is: {:.1f}\n".format(opt1_start_amt))
    
    #Initialize some parameters
    A_rd = 0.0
    N_rd = 36
    N_fd1 = 15
    N_fd2 = 15
    A_nre = C_nre
    N_nre = 9
    i_nre = 0.0
    
    #Start loop for RD
    for i in range(N_rd):
        i1 = (N_rd-i)/12.0    #Months remaining 
        A_rd += m_rd*(1+(r_rd/n_d))**(n_d*i1)
    
    #Start loop for FD1 - To be closed in July
    for j in range(N_fd1):
        j1 = j+1
        A_fd1 = P_fd1*(1+(r_fd1/n_d))**(n_d*(j1/12.0))
        
    #Start loop for FD2 - To be closed end of November
    for k in range(N_fd1):
        k1 = k+1
        A_fd2 = P_fd2*(1+(r_fd2/n_d))**(n_d*(k1/12.0))
        
    #Start loop to track NRE account balance - July, 2017 through March, 2018
    for m in range(N_nre):
        
        m1 = m+1
        
        if (m < 6):
            month_sb = month[m+6]     #Define month and year for printing
            year = '2017'
        else:
            month_sb = month[m-6]
            year = '2018'
        
        print("**----------------------------- {}, {} --------------------"\
              "-------------**\n".format(month_sb,year))
        
        if(m == 0):        #Add FD1 amount to NRE account in July
            A_nre += A_fd1
            print("FD1 account balance in {} is: {:.1f}".format(month_sb,\
                  A_fd1))
            print("FD1 is closed and balance is moved to NRE account.\n")
        if(m == 6):        #Add FD2 amount to NRE account in December
            A_nre += A_fd2
            month_sb2 = month[m+5]
            print("FD2 account balance end of {}, {} is: {:.1f}".format(\
                  month_sb2,year,A_fd2))
            print("FD2 is closed and balance is moved to NRE account.\n")
            
        if (m < 9):    
            A_nre -= m_rd
            
        if ((m1 > 3) and (m1 % 3 == 1)):
            A_nre += i_nre
            i_nre = A_nre*r_nre*(1.0/12.0)
            print("Interest earned in {}, {} is: {:.1f}\n".format(month_sb,year\
              ,i_nre))
        else:
            i_nre += A_nre*r_nre*(1.0/12.0)
            print("Interest earned in {}, {} is: {:.1f}\n".format(\
                      month_sb,year,i_nre))
        
        print("SB account balance in {} is "
              "{:.1f}\n".format(month_sb,A_nre))
    
    opt1_end_amt = A_rd+A_nre
        
    print("**--------------------------------------------------------------"\
              "---------**\n")
        
    print("RD account maturity amount is: {:.1f}\n".format(A_rd))
        
    print("SB account balance end of {}, {} is: {:.1f}\n".format(month_sb,year\
          ,A_nre))
    
    print("Option 1 end amount is: {:.1f}\n".format(opt1_end_amt))
    
    print("//*************************************************************"\
          "************************************//")
#%% Option 2
elif (option == '2'):
    
    opt2_start_amt = C_rd+C_fd1+C_fd2+C_nre
    
    print("//*************************************************************"\
          "************************************//\n")
    
    print("Option 2 is to close FD1 in July and move it to NRE account, "\
          "close RD in December and let it stay in the account until March, "\
          "2018 and continue FD2 account through to maturity.\n")
    
    print("**--------------------------------------------------------------"\
              "---------**\n")
    
    print("Option 2 start amount is: {:.1f}\n".format(opt2_start_amt))
    
    #Initialize some parameters
    A_rd = 0.0
    N_rd = 33
    N_rd1 = 2
    N_fd1 = 15
    N_fd2 = 18
    A_nre = C_nre
    N_nre = 9
    i_nre = 0.0
    
    #Start loop for RD - Last payment in december, 2017
    for i in range(N_rd):
        i1 = (N_rd-i)/12.0    #Months remaining 
        A_rd += m_rd*(1+(r_rd/n_d))**(n_d*i1)
        
    for i2 in range(N_rd1):
        A_rd1 = A_rd*(1+(r_rd/n_d))**(n_d*((i2+1)/12.0))
    
    #Start loop for FD1 - To be closed in July
    for j in range(N_fd1):
        j1 = j+1
        A_fd1 = P_fd1*(1+(r_fd1/n_d))**(n_d*(j1/12.0))
        
    #Start loop for FD2 - Until March, 2018
    for k in range(N_fd2):
        k1 = k+1
        A_fd2 = P_fd2*(1+(r_fd2/n_d))**(n_d*(k1/12.0))
        
    #Start loop to track NRE account balance - July, 2017 through March, 2018
    for m in range(N_nre):
        
        m1 = m+1
        
        if (m < 6):                 #Define month and year for printing
            month_sb = month[m+6]
            year = '2017'
        else:
            month_sb = month[m-6]
            year = '2018'
        
        print("**----------------------------- {}, {} --------------------"\
              "-------------**\n".format(month_sb,year))
        
        if(m == 0):        #Add FD1 amount to NRE account in July
            A_nre += A_fd1
            print("FD1 account balance in {} is: {:.1f}".format(month_sb, \
                  A_fd1))
            print("FD1 is closed and balance is moved to NRE account.\n")
        elif(m == 8):
            A_nre += A_rd1
            print("RD closing balance of {:.1f} is moved to SB account on "\
                  "{} 5th, {}\n".format(A_rd1,month_sb,year))
        
        if(m <= 5):  #Deduct RD monthly payment from NRE account until December
            A_nre -= m_rd
        
        if(m==5):
            print("RD account balance in {} (last payment) is"\
                  ": {:.1f}\n".format(month_sb,A_rd))
        
        if ((m1 > 3) and (m1 % 3 == 1)):
            A_nre += i_nre
            i_nre = A_nre*r_nre*(1.0/12.0)
            print("Interest earned in {}, {} is: {:.1f}\n".format(month_sb,year\
              ,i_nre))
        else:
            i_nre += A_nre*r_nre*(1.0/12.0)
            print("Interest earned in {}, {} is: {:.1f}\n".format(\
                      month_sb,year,i_nre))
        
        print("SB account balance in {} is "
              "{:.1f}\n".format(month_sb,A_nre))
        
    opt2_end_amt = A_fd2+A_nre
        
    print("**--------------------------------------------------------------"\
              "---------**\n")
        
    print("RD closing balance in {}, {} is: {:.1f}\n".format(month_sb,year,\
          A_rd1))
    
    print("FD2 account balance end of {}, {} is: {:.1f}\n".format(month_sb,\
          year,A_fd2))
        
    print("SB account balance end of {}, {} is: {:.1f}\n".format(month_sb,\
          year,A_nre))
    
    print("Option 2 end amount is: {:.1f}\n".format(opt2_end_amt))
    
    print("//*************************************************************"\
          "************************************//")
    
#%% Plot option
if (option == '1'):
    if(plot == 'y'):
        print("\nPlot for option 1 is shown below: \n")
        finance_plot.finplots('1')
    else: 
        print("\nYou chose not to generate a plot.\n")
elif (option == '2'):
    if(plot == 'y'):
        print("\nPlot for option 2 is shown below: \n")
        finance_plot.finplots('2')
    else:
        print("\nYou chose not to generate a plot\n.")
        
print("//********************************************************"\
              "*****************************************//\n")
        
#**************************************************************************#
