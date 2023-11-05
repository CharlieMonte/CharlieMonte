#Toll Road Calculator
#Variables
import string
total = 0
total_post_ev = 0
toll = 0
truck_surcharge = 0
state_surcharge = 0
apply_truck_surcharge = False
apply_ev_discount = False
toll_printed = False
total_printed = False
mi_check = False
state_valid = False
state = "x"
vehicle_type = "x"
zone1 = False
zone2 = False
zone3 = False
zone4 = False
zone5 = False


#Input Prompts
print("Enter Toll information")
hour = int(float(input("Hour: ")))


#Checks if hour is valid
if hour < 0 or hour > 23:
   print("\nOops! Hour must be 0 - 23.")
   exit()
weekend = input("Weekend (Y/N)? ")
state = input("State: ")
vehicle_type = input("Vehicle type (Car, Truck, EV): ")


#Assigns each cluster of hours to a "zone"
if hour > -1 and hour < 7:
   zone1 = True
if hour > 6 and hour < 10:
   zone2 = True
if hour > 9 and hour < 15:
   zone3 = True
if hour > 14 and hour < 20:
   zone4 = True
if hour > 19 and hour < 24:
   zone5 = True


#Checks if it is a weekend
if weekend == 'Y' or weekend == 'y':
   weekend = True
if weekend == 'N' or weekend == 'n':
   weekend = False


#Applies the correct toll for the "zone" on a weekday
if weekend == False:
   if zone1 == True:
       toll = 1.05
   if zone2 == True:
       toll = 3.25
   if zone3 == True:
       toll = 2.50
   if zone4 == True:
       toll = 3.45
   if zone5 == True:
       toll = 1.15


#Applies the correct toll for the "zone" on a weekend
if weekend == True:
   if zone1 == True:
       toll = 0.95
   if zone2 == True or zone3 == True or zone4 == True:
       toll = 1.75
   if zone5 == True:
       toll = 1.15


vehicle_type = vehicle_type.lower()


#If vehicle type is a truck, takes note to apply a surcharge later if required
if vehicle_type == "truck":
   apply_truck_surcharge = True


#if vehicle type is an ev, takes note to apply a discount later if required
if vehicle_type == "ev":
   apply_ev_discount = True


#Ensures the vehicle type is a valid entry
if vehicle_type != "car" and vehicle_type != "truck" and vehicle_type != "ev":
   print("\nOops! Vehicle type must be Car, Truck or EV.")
   exit()


#Applies surcharges for all states except IL
state = state.upper()
if state.upper() != "IL":
   state_surcharge = 1.50
   state_valid = True


#Checks if they're from michigan to ensure they only get charged 0.05 dollars later.
if state.upper() == "MI":
   state_surcharge = 0.05
   mi_check = True
if state.upper() == "IN" or state.upper() == "WI" or state.upper() == "OH" or state.upper() == "IL" or state.upper() == "MI":
   state_valid = True
else:
   state_valid = False
   print("\nOops! State must be IL, OH, IN, WI or MI.")
   exit()


#applies truck surcharge
if apply_truck_surcharge == True:
   truck_surcharge = 2.50


#Total (Pre Ev Discount)
total = toll + state_surcharge + truck_surcharge
total_pre_ev = total


#Total (Post EV Discount
if apply_ev_discount == True:
   total = (toll * 0.75) + (state_surcharge * 0.75)
   total_post_ev = total
   total_post_ev -= total_pre_ev
   total_post_ev = abs(total_post_ev)


#Return statements
print("Toll Charge Summary")
print (f'Info: {hour} {weekend} {state} {vehicle_type}')
if mi_check == False:
   print(f'Toll: ${toll:.2F}')
   toll_printed = True
else:
   print(f'Toll: ${state_surcharge:.2F}')
   toll_printed = True
if state_surcharge > 0 and mi_check == False:
   print(f'{state} surcharge: ${state_surcharge:.2f}')
if apply_truck_surcharge == True and mi_check == False:
   print(f'Truck surcharge: ${truck_surcharge:.2f}')
if apply_ev_discount == True and mi_check == False:
   print(f'EV discount: ${total_post_ev:.2f}')
if mi_check == False and total != toll:
   print(f'Total: ${total:.2f}')
   total_printed = True
if state_surcharge > 0 and total_printed == False and toll_printed == False:
   print(f'Total: ${state_surcharge:.2f}')
