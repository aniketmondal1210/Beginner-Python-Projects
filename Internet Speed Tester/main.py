from speedtest import Speedtest

print("Please wait Speed is being Calculated")

def check_speed():
    speed_test = Speedtest()
    speed_test.get_best_server()

    download = speed_test.download()/1000000 #Speed in Mbps
    upload = speed_test.upload()/1000000 #Speed in Mbps
    ping = speed_test.results.ping

    print(f"Download Speed: {download:.2f} Mbps")
    print(f"Upload Speed: {upload:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

check_speed()
