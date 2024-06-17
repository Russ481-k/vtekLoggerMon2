

##############################################
## 실행 명령어
##############################################

## .env 환경변수 설정
#주소 및 폴더 디렉토리 설정 필요

## mariaDB 확인
$ mariadb

## Machbase 확인
$ machbase

## 로거 실행 udpDaemonMachbase.py
sudo python3 /home/vision/vtekLoggerMon2/stopLogger.py
sudo python3 /home/vision/vtekLoggerMon2/startLogger.py
	
## 어플리케이션 및 일간 주간 합계 스케줄러 실행 chedule_sum.py app.py
sudo python3 /home/vision/vtekLoggerMon2/stopWeb.py
sudo python3 /home/vision/vtekLoggerMon2/startWeb.py
