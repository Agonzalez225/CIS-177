
"""
Created on Mon Aug 22 20:05:40 2022


@author: be
name = Alberto Gonzalez
22 August 2022
"""

def payment(pv, rAPR, nMonths):
    '''
    

    Parameters
    ----------
    pv : TYPE floating point number
        DESCRIPTION. amount money being borrowed
    rAPR : TYPE Float
        DESCRIPTION. annual percentage interest rate
    nMonths : TYPE Integer
        DESCRIPTION. term - Length of loan

    Returns
    -------
    
    Pmt : TYPE float
        DESCRIPTION. Monthly payment 


    '''
    pmt =  rAPR/1200*pv/(1-(1+(rAPR/1200))**(-nMonths))  
    return pmt

'''
write a loop!
input pv, n, rAPR
print out the input variables 
print out the payment
and loop back to get a new case

if pv is put in a '0', exist the loop
'''

while (1):
    pv = input('Please entered amount borrowed :')
    pv = float(pv)
    if pv == 0:
        break
    print(pv)
    interest = input('Please type in annual percentage interest rate ')
    interest = float(interest)
    nMonths = input('Enter the number of months :')
    nMonths = float(nMonths)
    paymentDollars = payment (pv = pv, rAPR = interest, nMonths = nMonths )
  
    print(f"The payment value is : {pv:.2f} . The interest Rate is : {interest:.2f} %. Total months is : {nMonths} Payment Dollars is : {paymentDollars:.2f}")
print("Out of the loop")

