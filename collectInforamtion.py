import time
import subprocess
from subprocess import Popen

#if __name__ == "__main__":

def main():
    site_name = 'google.com'
    how_much_ping = '4'
    is_true,get_ping = do_ping(site_name,how_much_ping)
    if (is_true):
        localtime = time.localtime(time.time()) 
        list_of_ping_speed,packet_loss = make_correct(get_ping)
        save_important_data(list_of_ping_speed,time)
        save_all_data(get_ping,localtime)
        print(packet_loss)
        print('\n\n\n\n\n\n')
        print(list_of_ping_speed)
        print(get_ping)
        print('\n\n\n\n\n')
        the_important_information = list_of_ping_speed
        print('min_speed = '+str(the_important_information[0]) +'\n'+str(the_important_information[1])+'\n'+'max speed ping',str(the_important_information[2]))
    else :
        print('error')
        
def make_correct(str_ping):

    first_list = str_ping.split(', ') # we splite our string to use twe end line 
    string_of_packet_loss = first_list[2] #the string in list that usefule for us
    packet_loss = int(string_of_packet_loss.split('%')[0]) #the number of packet lass usefule 
    string_of_ping_speed = first_list[-1]
    if (packet_loss == 100):
        raise "can't ping asked server"
    else:
        print('packet loss is :' , packet_loss)
    secent_list = string_of_ping_speed.split('/')
    min_speed_ping = float(secent_list[4])
    ave_speed_ping = float(secent_list[5])
    max_speed_ping = float(secent_list[6].split(" m")[0])
    return [min_speed_ping,ave_speed_ping,max_speed_ping],packet_loss


def do_ping(name_of_server,how_much_ping):
    result = Popen(args=['ping','-w',how_much_ping,'-i','1',name_of_server],stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out_put,error = result.communicate()
    if (error == ''):
        return 1,out_put
    else :
        return 0,''




def save_all_data(get_data,time):
    try :
        file = open(str(time[0]) +  '||' + str(time[1]) +'||' + str(time[2])+'.txt','r')
        input = file.read()
        file.close()
        file = open(str(time[0]) +'||' +str(time[1]) +'||' + str(time[2])+'.txt','w')
        input = input +'\n'+ get_data
        file.write(input+ '\n' +'tm_hour = '+str(time[3]) +' tm_min = '+str(time[4]) +' tm_sec = '+str(time[5]))  
    except :
        file = open(str(time[0]) +'||' +str(time[1]) +'||' +str(time[2])+'.txt','w')
        file.write(get_data + '\n' +'tm_hour = '+str(time[3]) +' tm_min = '+str(time[4]) +' tm_sec = '+str(time[5]))  
        file.close()
main()
