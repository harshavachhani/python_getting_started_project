# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    deliveries=data['innings'][0]['1st innings']['deliveries']
    count=0
    #for delivery in deliveries:
    for index in range(len(deliveries)):
       delivery=deliveries[index]
       #print 'Current fruit :', delivery
       for delivery_number,delivery_info in delivery.items():
           if delivery_info['batsman'] == 'RT Ponting':
                count +=1


    return count
