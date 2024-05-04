#The following equation estimates the average calories burned for a person when exercising, which is based on a scientific journal article (source): https://www.tandfonline.com/doi/abs/10.1080/02640410470001730089

#Calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368

#Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output the average calories burned for a person.

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
#print('Calories: {:.2f} calories'.format(calories))

#Removed discription within the input statements in order for lab to submit
Age = int(input())
Weight = int(input())
Heart_Rate = int(input())
Time = int(input())

Calories = ((Age * 0.2757) + (Weight * 0.03295) + (Heart_Rate * 1.0781) - 75.4991) * Time / 8.368

print('Calories: {:.2f} calories'.format(Calories))