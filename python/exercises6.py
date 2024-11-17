import speedtest
import datetime
import time
def st_fun():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    return download_speed, upload_speed

with open("internet_speed.csv", "w") as file:
    file.write("Timestamp,Download Speed (Mbps),Upload Speed (Mbps)\n")

while True:        
    download_speed, upload_speed = st_fun()
    current_time = datetime.datetime.now().strftime("%x %X")

    with open("internet_speed.csv", "a") as file:
        file.write(f"{current_time},{download_speed:.2f},{upload_speed:.2f}\n")
    print(f"Data saved: {current_time}, Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")
    time.sleep(5)
    




