
import requests
from datetime import date,datetime
from pathlib import Path
import time
import systemd.daemon
import pendulum


def daemon_logic():
    try:
        print("Fetching data")
        response = requests.get("https://www.google.com/")
        text_response = response.text
        print("configuring output file")

        now = pendulum.now()
        dt_time = now.to_iso8601_string()

        filename = "/var/log/test-{}.log".format(dt_time)

        print(f"writing output file to {filename}")

        with open(filename, "w+") as results_file:
            results_file.write(text_response)



    except Exception as e:
        print("something went wrong", e)

if __name__ == "__main__":
    print('Starting up ...')
    time.sleep(10)
    print('Startup complete')
    systemd.daemon.notify('READY=1')

    while True:
        print('Hello from the Python Demo Service')
        daemon_logic()
        time.sleep(5)






    


# while True:
#     try:
#         with daemon.DaemonContext():
#             response = requests.get("https://www.google.com/")
#             text_response = response.text
   


#         now = datetime.now()
#         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")



#         with open(f"/root/pydeamon/test.log{dt_string}","w+") as results_file:
#             results_file.write(text_response)
        
    
#         daemon.DaemonRunner.start()
#         time.sleep(300)
#     except Exception as e:
#         print("something went wrong", e )

    
        
    

    
# in order to create a timestamp 
# use this line form the date time module
# >>> from datetime import date
# >>> date(2002, 12, 4).ctime()
# 'Wed Dec  4 00:00:00 2002'

# and use this function from the pathlib module
# >>> from pathlib import Path
# >>> data_file = Path('data_01.txt')
# >>> data_file.rename('data.txt')

# NExt look at puting all these together under systemd
# 
# https://opensource.com/article/20/4/systemd
# https://opensource.com/article/20/5/manage-startup-systemd


    # # consolidate this into omne ufnction as opposed to creating a new file from and over written file , just create a brand new one
        # # use a try catch block for all this logic
        # data_file = Path("test.log")
        # data_file.rename(f"test{dt_string}.log")






