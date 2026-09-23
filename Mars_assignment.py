def visit_fee(visit_type):
 if visit_type=="General":
  return 15000
 elif visit_type=="Emergency":
  return 40000
 elif visit_type=="Follow-up":
  return 10000
 else:
  return -1

def eligibility_check(visit_type,age):
  if age>=60 and visit_type=="Follow-up":
   return True
  elif age>0 and (visit_type=="General" or visit_type=="Emergency"):
   return True
  else:
   return False
  


successful_patients=0
total_fees=0
while True:
 try:
  patientss=int(input("How many patients will be registered today?"))
  if patientss>0:
   break
  else:
   print("Patient count cannot be a negative number")
 except ValueError:
  print("Enter a valid number for number of patients")

for i in range(1,patientss+1):
 print(f"\n Welcome to small clinic customer {i}")
 name=input("Enter patient name: ")

 while True:
  try:
   age=int(input("Enter patient age: "))
   if age>0:
    break
   else:
    print("Invalid number entered for age")
  except ValueError:
   print("Enter a valid number for patient's age")

 visit_type=input("Enter visit type(General, Emergency, Follow-up): ")

 if eligibility_check(visit_type,age)==False:
  if age<60 and visit_type=="Follow-up":
   print(f"Sorry {name}, Follow-up visits are only for patients aged 60 years and above")
  else:
   print("Please enter a valid visit type")
 else:
  payment=visit_fee(visit_type)

  fee_deposit=int(input("How much will you pay for your respective visit: "))
  if payment==-1:
   print("You have entered an invalid visit type")

  elif fee_deposit<payment:
   debt=payment-fee_deposit
   print(f"Unfortunately,{visit_type} costs {payment} UGX. You will need to deposit {debt} UGX more")
  elif fee_deposit>payment:
   balance=fee_deposit-payment
   print(f"{visit_type} costs {payment} UGX. You have a balance {balance} UGX")
   print(f"Congratulations {name}, you have been registered as a successful patient. Kindly wait to be called upon")
   successful_patients+=1
   total_fees+=payment
  else:
   print(f"Congratulations {name}, you have been registered as a successful patient. Kindly wait to be called upon")
   successful_patients+= 1
   total_fees+= payment   ##i added what they felt like depositing instead of required consultation fee
print("\n---PATIENT SUMMARY FOR THE DAY---")
print(f"Total number of successful patients: {successful_patients}")
print(f"Total fees collected: {total_fees}")
