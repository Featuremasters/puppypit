print(''' .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
| |  ________    | || |      __      | || |  ____  ____  | || |    _______   | | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | |_   ___ `.  | || |     /  \     | || | |_  _||_  _| | || |   /  ___  |  | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |   | |   `. \ | || |    / /\ \    | || |   \ \  / /   | || |  |  (__ \_|  | | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| |   | |    | | | || |   / ____ \   | || |    \ \/ /    | || |   '.___`-.   | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |  _| |___.' / | || | _/ /    \ \_ | || |    _|  |_    | || |  |`\____) |  | | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | |________.'  | || ||____|  |____|| || |   |______|   | || |  |_______.'  | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'    ''')
def leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
def day(year):
    month=int(input("Enter the month\n"))
    if month in range(1,13):
     month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
     if month==2 and leap(year):
        print(29)
     else:
         print(f"The days in {month} has {month_days[month-1]} days")
    
    else:
        print("Enter the right month")
        day(year)
year=int(input("Enter the year\n"))
day(year)