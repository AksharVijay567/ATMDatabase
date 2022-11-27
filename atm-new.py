import string
import os
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="G00dK3y5",
  database="atmdatabase"
)

mycursor = mydb.cursor() # equivalent to use database command in mysql AND CURSOR() IS a fn belonging to connect module
count = 0 # this variable checks valid user pin ( no of times user can attend for wrong pins
# while loop checks existence of the entered username
print("****************************************************************************")
print("*                                                                          *")
print("*                   WELCOME TO WESTERN UNION BANK ATM SYSTEM               *")
print("*                                                                          *")
print("****************************************************************************")
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	query = "SELECT * FROM customers WHERE customername = " + "'" + user + "'"
	mycursor.execute(query)
	result = mycursor.fetchall() # result is an array which holds one row( record) from the table
	row_count = mycursor.rowcount # rowcount is mysql variable
	if row_count > 0:
		pins=result[0][1] # for the customer pin
		amounts=result[0][2] # for customer available amount in the bank
		n=result[0][3] # for customerid
		break
	else:
		print('----------------')
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		print('----------------')

# comparing pin
while count < 3:
    print('------------------')
    print('******************')
    pin1 = input('PLEASE ENTER PIN: ')
    print('******************')
    print('------------------')
    pin = int(pin1) # we can use also int(input()) method also
    if pin == pins:
        break
    else:
        count += 1
        print('-----------')
        print('***********')
        print('INVALID PIN')
        print('***********')
        print('-----------')
        print()

# in case of a valid pin- continuing, or exiting
if count == 3:
	print('-----------------------------------')
	print('***********************************')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	print('***********************************')
	print('-----------------------------------')
	exit() # completely exiting the program as somebody to trying to hack the account

print('-------------------------') # execution starts from this statement for successful login
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(str.capitalize(user), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('cls')
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \nType The Letter Of Your Choices: ').lower()
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(user), 'YOU HAVE ', amounts,'RUPEES ON YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('*********************************************')
		print('---------------------------------------------')
		if cash_out%10 != 0:
			print('------------------------------------------------------')
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEE NOTES')
			print('******************************************************')
			print('------------------------------------------------------')
		elif cash_out > amounts:
			print('-----------------------------')
			print('*****************************')
			print('YOU HAVE INSUFFICIENT BALANCE')
			print('*****************************')
			print('-----------------------------')
		else:
			amounts = amounts - cash_out
			tmp = str(amounts)
			query = "UPDATE customers SET customeramount = " + tmp + " WHERE customername = " + "'" + user + "'"
			print(query)
			mycursor.execute(query)
			mydb.commit()
			print('-----------------------------------')
			print('***********************************')
			print('YOUR NEW BALANCE IS: ', amounts, 'RUPEES')
			print('***********************************')
			print('-----------------------------------')
			
	elif response == 'l': # for depositing money
		print()
		print('---------------------------------------------')
		print('*********************************************')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
		print('*********************************************')
		print('---------------------------------------------')
		print()
		if cash_in%10 != 0: # user cannot deposit 22 Rs but in the multiples of 10
			print('----------------------------------------------------')
			print('****************************************************')
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 RUPEE NOTES')
			print('****************************************************')
			print('----------------------------------------------------')
		else:
			amounts = amounts + cash_in
			tmp = str(amounts)
			query = "UPDATE customers SET customeramount = " + tmp + " WHERE customername =" + "'" + user + "'"
			mycursor.execute(query)
			mydb.commit()
			print('----------------------------------------')
			print('****************************************')
			print('YOUR NEW BALANCE IS: ', amounts, 'RUPEE')
			print('****************************************')
			print('----------------------------------------')
	elif response == 'p':
		print('-----------------------------')
		print('*****************************')
		new_pin = str(input('ENTER A NEW PIN: '))
		print('*****************************')
		print('-----------------------------')
		if new_pin.isdigit() and new_pin != pins and len(new_pin) == 4:
			print('------------------')
			print('******************')
			new_ppin = str(input('CONFIRM NEW PIN: '))
			print('*******************')
			print('-------------------')
			if new_ppin != new_pin:
				print('------------')
				print('************')
				print('PIN MISMATCH')
				print('************')
				print('------------')
			else:
				# Make change in the database
				pins = new_pin
				tmp = str(pins)
				query = "UPDATE customers SET customerpin = " + tmp + " WHERE customername =" + "'" + user + "'"
				mycursor.execute(query)
				mydb.commit()
				print('NEW PIN SAVED')
		else:
			print('-------------------------------------')
			print('*************************************')
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('*************************************')
			print('user1-------------------------------------')
	elif response == 'q':
		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')
mycursor.close()
mydb.close()