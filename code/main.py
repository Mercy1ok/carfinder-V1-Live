AllowedVehiclesList =  [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500' ]

Authorized_Cars = AllowedVehiclesList[0] + ', ' + AllowedVehiclesList[1] + ', ' + AllowedVehiclesList[3] + ', ' + AllowedVehiclesList[4]  + ', ' + AllowedVehiclesList[5]

UnAuthorized_Cars = AllowedVehiclesList[2]

while True:
    menu = """********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for an Authorized Vehicle
3. ADD an Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
********************************"""
    print(menu)
    option = int(input("Enter your choice: "))

    if option == 1:
        print("********************************")
        responce = ("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        print("                ") 
        print(f"\033[1m{responce}\033[0m")
        with open("data/text.txt", 'r') as db:
          reading = db.read()
          print(reading)
        print("                ") 

    elif option == 2:
      print('*******************************')
      selected_car = "Please Enter the full Vehicle name: "
      selected_caro = input(f"\033[1m{selected_car}\033[0m")


      if selected_caro in Authorized_Cars:
          print('                                      ')
          selecteddd = f"{selected_caro} is an authorized vehicle."
          print(f"\033[1m{selecteddd}\033[0m")
          print(menu)
      elif selected_caro in UnAuthorized_Cars:
          print('                                      ')
          unselected = (f"{selected_caro} is not an authorized vehicle, if you received this in error please check the spelling and try again.")
          print(f"\033[1m{unselected}\033[0m")
      else:
          print("Invalid car selection.")

    elif option == 3:
      print('*******************************')
      pink = ("Please Enter the full Vehicle name you would like to add: ")
      sales_rep_selection=input(f"\033[1m{pink}\033[0m")
      AllowedVehiclesList.append(sales_rep_selection)
      with open("data/text.txt" , mode ='a') as db:
        db.write(f"\n{sales_rep_selection}")
      chosen = (f"You have added {sales_rep_selection} as an authorized vehicle.")
      print("                 ")
      print(f"\033[1m{chosen}\033[0m")

    elif option == 4:
        print('*******************************')
        sales_rep_removal = input("\033[1mPlease Enter the full Vehicle name you would like to remove: \033[0m")
      
        with open("data/text.txt", "r") as file:
          lines = file.readlines()

        lines = [line for line in lines if line.strip() != sales_rep_removal]

        with open("data/text.txt", "w") as file:
          file.writelines(lines)
          
        print("*******************************")
        are_you_sure = (f"Are you sure you want to remove {sales_rep_removal} from the Authorized Vehicles List?")
        yes_or_no = input(f"\033[1m{are_you_sure} (Y/N): \033[0m")
        if yes_or_no.upper() == "Y":
            if sales_rep_removal in AllowedVehiclesList:
                AllowedVehiclesList.remove(sales_rep_removal)
                removed = (f"You have removed {sales_rep_removal} as an Authorized Vehicle.")
                print(f"\033[1m{removed}\033[0m")
            else:
                print(f"{sales_rep_removal} is not in the Authorized Vehicles List.")
        elif yes_or_no.upper() == "N":
            print("You have not removed the vehicle.")
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    elif option == 5:
        print("********************************")
        print("Thank you for using the AutoCountry Vehicle Finder, goodbye!")
        break

    else:
        print("Invalid option")


