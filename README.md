```
sudo apt-get install git  unzip python3-pip vim mariadb-server
```

```
sudo apt install iptables
```

```
sudo pip3 install flask pymysql requests psutil python-dotenv aiohttp schedule numpy
```

```
sudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 5654 -j ACCEPT
```

```
git clone https://github.com/Russ481-k/vtekLoggerMon2.git
```

```
cd vtekLoggerMon2
```

```
sudo vi .env
```

(insert) key click

```
envhost="0.0.0.0"
envhostlocal="localhost"
envuser="root"
envpassword='root'
envdb="logger"
envcharset="utf8"
```
envhost 및 envpassword 설정 필요

(esc)

:wq!

```
sudo mysql
```

```
CREATE DATABASE logger;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
ALTER user 'root'@'localhost' identified by 'root';
EXIT;
```

```
sudo mysql -u root -p logger<./sql/userAccount.sql
sudo mysql -u root -p logger<./sql/menuCustom.sql
```

```
sh -c "$(curl -fsSL https://docs.machbase.com/install.sh)"
```
#################################################
# Download complete machbase-neo-v8.0.21-linux-amd64.zip #  => 버전 정보와 환경과 주소를 이후 코드에 맞춰줘야함
#################################################

```
unzip machbase-neo-v8.0.21-linux-amd64.zip
```

```
./machbase-neo-v8.0.21-linux-amd64/machbase-neo serve --host 192.168.1.47 --daemon --pid ./machbase-neo.pid
```

```
sudo python3 ./iniTable.py
```

```
nohup python3 udpDaemonMachbase.py & echo $! > ./udpDaemonMachbase.pid
```

```
sudo python3 stopLogger.py
sudo python3 startLogger.py
sudo python3 stopWeb.py
sudo python3 startWeb.py
```
