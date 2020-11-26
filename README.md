:black_heart: Simple setup of the Raspberry Pi 4

### Format your SD card 
Download [SD Memory Card Formatter](https://www.sdcard.org/downloads/formatter/eula_mac/index.html) and format your SD card.
<div>
<img width="418" alt="01_SDcard_format" src="https://user-images.githubusercontent.com/40614421/100288068-2d71a100-2f76-11eb-907b-50c5cce93dc0.png">
</div>

### Download Raspberry Pi OS manually 
Classic way: download [Raspberry os](https://www.raspberrypi.org/software/operating-systems/) and install it manually. 
<div>
<img width="1211" alt="Rasberry_pi_OS" src="https://user-images.githubusercontent.com/40614421/100364060-e0391200-2ffd-11eb-92f5-277aca79d131.png">
</div>

Easy way: download [Raspberry Pi Imager](https://www.raspberrypi.org/software/) (please, check the OS of your PC when you download it). Detailed processes are explained on [Raspberry Pi blog](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2).
<div>
<img width="996" alt="Raspberry_pi_image" src="https://user-images.githubusercontent.com/40614421/100363908-ae27b000-2ffd-11eb-9ff0-75b2742c9539.png">
</div>
  
### Download Etcher (if you select the classic way)
[Etcher](https://www.balena.io/etcher/) flashes the OS images to SD cards or USB drives, safely and easily. 

### Write the Raspberry Pi OS image to the SD card
* Run Etcher and select the Raspberry Pi OS image and SD card drive. Then, click burn.
* Unmount the SD card.

### Problem... 
 When I mount Raspberry's SD card, I got the message...
```
Kernel panic-not syncing:
VFS: unable to mount root fs on unknown- block(179,2)
```
There are many reasons to generate this problem. You can find some solutions on [Raspberry pi forum](https://raspberrypi.stackexchange.com/questions/40854/kernel-panic-not-syncing-vfs-unable-to-mount-root-fs-on-unknown-block179-6). If you can understand Korean, please check here: [커널 패닉 동기화되지 않음 : VFS : NOOBS 위에서 Raspbian을 실행중인 알 수없는 블록 (179,6)에 루트 fs를 마운트 할 수 없음](https://qastack.kr/raspberrypi/40854/kernel-panic-not-syncing-vfs-unable-to-mount-root-fs-on-unknown-block179-6) or [라즈베리파이 커널 패닉](https://stupid86.tistory.com/entry/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-%EC%BB%A4%EB%84%90-%ED%8C%A8%EB%8B%89)
In my case, I just formatted the SD card again and then reinstalled Raspberry OS using [Raspberry Pi Imager](https://www.raspberrypi.org/software/). It is a much easier way personally. 

### Rapberry camera 
* Mount your Raspberry camera properly
* Go to `Preferences`→`Raspberry Pi Configuration` `Interfaces`, then make enabled camera and reboot your Raspberry Pi [details in Korean, 한국어 설명](https://blog.naver.com/ljy9378/221430169621).
<div>
![raspberry_pi_configuration_camera](https://user-images.githubusercontent.com/40614421/100364227-1ececc80-2ffe-11eb-8d3c-16ebfaa926ca.png)
</div>

* To test your camera, please run attached files in the repository [ref, 라즈베리파이 CCTV](https://m.blog.naver.com/PostView.nhn?blogId=einsbon&logNo=221215848541&proxyReferer=https:%2F%2Fwww.google.com%2F). The blog(written in only Korean) explains well. 
#### take a photo
clone pythons codes on your folder.
```
pi@raspberrypi: ~ $ git clone https://github.com/soyounson/Raspberry_Pi_setup.git
``` 
open your terminal, 
```
pi@raspberrypi: ~ $ python test_photo.py
``` 
#### record a video
open your terminal, 
```
pi@raspberrypi: ~ $ python test_video.py
``` 
### Setup of 3.5 inch RPi LCD monitor (C)
> ...coming soon

### Shutdown Raspberry Pi 4
* Type command in terminal, 
```
sudo shutdown -h now
```
or 
```
sudo halt
```
* Wait for the LED to stop flashing on the Raspberry Pi (additionally 5 secs). 
* Turn off the power strip (Raspberry Pi power supply).

Enjoy :)
