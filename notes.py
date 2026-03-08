def main():
    time_1 = input("enter time: ")
    time = convert(time_1)
    print (time)
    if time>=7.00 and time<=8.00:
        print("breakfast time")
    elif time >=12.00 and time <=13.00:
        print("lunch time")
    elif time >=18.00 and time <=19.00:
        print("dinner time")
   

    


def convert(time):
    conv_time = time.split(":")
    hour = float(conv_time[0])
    mins = float(conv_time[1])
    final = float(((hour*60)+mins)/60)
    return final
    
run = main()
print(run)