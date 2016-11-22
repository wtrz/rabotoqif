#!/usr/bin/env python
#Python 3.5 script 20161101 V3
#Author: Wouter Dunnes
#Purpose: Convert Rabobank's  "transactions.txt" into Homebank qif format
#reference QIF format: https://en.wikipedia.org/wiki/Quicken_Interchange_Format
#---------||

def convert(ifile):
    import time
    
    #variables
    current_date = time.strftime("%Y%m%d")
    afilename = "accounts.txt" #filename with accounts
    #ifilename = "transactions.txt" #input filename
    ofilename = "transactions" + current_date + ".qif"
    fh_account = open(afilename,'r')
    fh_input = open(ifile,'r')
    fh_output = open(ofilename,'w')
    
    
    
    #accountlist
    
    
    
    account_list = []
    for line in fh_account:
        line = line.split(',') 
        
        account_list.append(tuple(line))
        
        account_dict = {}
    for account in account_list:
        account_dict[account[0]] = []
            
            
            
            
    for line in fh_input:
        words_list = line.replace('"','').split(',')
        
        trans_type = '!Type:Bank'    
        #trans_fromaccount = str('N' + words_list[0])
        trans_date = str('D' + (words_list[2][6:8]) + '/' + (words_list[2][4:6]) + '/' + (words_list[2][0:4]))
        
        if words_list[3] == 'D': 
            sign = '-' 
        else: 
            sign = '+'
            
        trans_amount = str('T' + sign + words_list[4])
    
        if not words_list[6] == '':
            payee = words_list[6]            
        else:
            payee = words_list[10]
            
            
        trans_payee = str('P' + payee)
        trans_memo = str('M' + words_list[10])
        trans_list = [trans_type,trans_date,trans_amount,trans_payee,trans_memo]
    
        try:        
            account_dict[words_list[0]].append(trans_list)
        except:
            continue



    for account in account_list:
        account_name = str('N' + account[1])
        fh_output.write('!Account\n' + account_name + '\nTBank\n')
        
    
        for trans_list in account_dict[account[0]]:
            for item in trans_list:
                fh_output.write(item + '\n')
            fh_output.write('^\n')
        



    fh_account.close()
    fh_input.close()
    fh_output.close()

convert('transactions.txt')
