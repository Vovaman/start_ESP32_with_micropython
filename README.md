[Rus](README.ru.md)
# start_ESP32_with_micropython

## Introduction
This project contains all steps to start to work with [ESP32](https://www.espressif.com/en/products/socs/esp32)
using [Micropython](https://micropython.org/).
Besides this description project contains code for LED blinking. We will run this code on cotroller.

**Our goal** is to run project on controller to understand all the process.

**Perspective** is to create [standard "connector"](https://github.com/Vovaman/connectorESP). This connector will realize some
control algorithm, acquire data from plugged devices and send it to [platform](https://github.com/Vovaman/peresvet).

First practical project is ["anti-caisson"](https://github.com/Vovaman/wellCabin), which is coffer over well.
Controller will switch on/off heating and ventilation and will acquire water pressure data. More perspective - switch on/off the pump.

**Why micropython?** All other referenced above projects are in Python. So, this is why micropython is the better choice.

## For whom
Firstly, for myself to not forget all the sequence.
Secondly, for programmers wishing to automate some things around.
Thirdly, for all handy guys.
Due to possible programming weakness among fans, description will be some redundant. But these redundancies will be under spoilers.
However, it is necessary to have some basic skills with computer: run terminal, work with commands in console, download files in browser and save them into appropriate places and so on...

## Starting point
So, we have:

1. ESP32 controller.
   Will work with [ESP32S-WROOM-32](https://aliexpress.ru/item/1005002611857804.html?item_id=1005002611857804&sku_id=12000021386518349&spm=a2g2w.productlist.0.0.28c767f2tgjXEB) (approx $5):
   ![ESP32](/img/ESP.png)
   *Picture from http://developer.alexanderklimov.ru/arduino/esp32/*
   There is wide range of ESP32 implementations. This project is applicable to many of them, but another firmware version has to be downloaded.
2. OS is Ubuntu 22.04 LTS.
   > :warning: Windows only by demands...
3. USB - microUSB cable.
   > :warning: **Warning:** There are cables without data wire. They are used only for recharging. We need cable with data wire!

## Go on

### 1. Node.js
It is necessary install [Node.js](https://nodejs.org/ru/). `Pymakr` extension for `VSCode` needs it.
<details>
   <summary>Installation of Node.js</summary>

   Open terminal and run:
   ```bash
   $ sudo snap install --classic node
   ```
   Check the result:
   ```bash
   $ node --version
   ```
   This command will return the current version of `Node.js`.

</details>

### 2. VSCode
Next step. We have to install [VSCode](https://code.visualstudio.com/).
> :warning: **Warning!** If you've installed VSCode by snap, you have to delete it and install it again by deb-package.
> `Pymakr`-extension for VSCode does not work in snap-version.

<details>
   <summary>VSCode installation</summary>

   1. Open https://code.visualstudio.com/ in your browser and press `deb`-button:
      ![VSpage](/img/vs0.png)
   2. Run terminal, go to directory with package you just downloaded (`code_1.63.2-1639562499_amd64.deb` at the moment). Run the command:
      ```bash
      sudo dpkg -i code_163.2-1639562499_amd64.deb
      ```

</details>

### 3. Pymakr
[Pymakr](https://pycom.io/products/supported-networks/pymakr/) is the VSCode's extension to work with `micropython`.

<details>
   <summary>Install Pymakr</summary>

   Run VSCode and press `Extensions`:
   ![Extensions](/img/vs1.png)
   Insert `Pymakr` in search field, choose `Pymakr` and press `install` button:
   ![Pymakr](/img/vs2.png)

</details>

The settings window and terminal will be opened after installation:
![PymakrEnd](/img/vs3.png)
Close it.

### 4. Copy this project
Suppose the parent directory is `~/work/projects`.

<details>
   <summary>Clone from github</summary>

   It is the better choice to get your own [github](https://github.com) account and clone this project.
   In such case you have to install `git` - repository management tool:
   ```bash
   $ sudo apt install git
   ```

   So, just clone this project after git installation:
   ```bash
   $ cd ~/work/projects
   $ git clone git@github.com:Vovaman/start_ESP32_with_micropython.git
   ```

</details>

<details>
   <summary>...or download the source archive</summary>

   Another way is to download the archive with source codes from
   `https://github.com/Vovaman/start_ESP32_with_micropython/archive/refs/heads/master.zip`.
   Download this archive and save it in `~/work/projects`.
   Extract files from archive to `start_ESP32_with_micropython` folder.

</details>

### 5. Initialize project
Open terminal and got to `~/work/projects/start_ESP32_with_micropython` with project source code.

Run this command inside the folder:
```bash
$ pipenv install
```
<details>
   <summary>Why?</summary>

   `Pipenv` is the tool to create python environment for projects. Each project may have its own environment with specific Python version and
   packages installed. Thus projects do not intersect each other and operational Python environment.

</details>

These packages will be installed during environment initialization:
- `esptool`, tool to flash our controller
- `micropy-cli` - just useful tool.

### 6. Flash the controller

**Download firmware**
Download appropriate firmware from https://micropython.org/download/.
If your controller model is the same as in picture above, you may use `esp32-20220117-v1.18.bin` from the project.
Or download the newer version from https://micropython.org/download/esp32/.

**Check the port**
<details>
   <summary>It is ttyUSB0 more often</summary>

   So, let's define the created port name when you connect controller to computer.
   Go to `/dev` folder and list all devices:
   ```bash
   $ cd /dev
   $ ls
   ```
   Then connect controller to computer and list devices again:
   ```bash
   $ ls
   ```
   Find new string in the list. This string is the port name we need.
   Suppose it is `ttyUSB0`.

</details>

**Set rights to write**
<details>
   <summary>sudo adduser user_name dialout</summary>

   Our working account needs rights for write to upgrade the controller.
   We have to run two commands in terminal to do so:
   ```bash
   # add yourself to appropriate group
   $ sudo adduser $USER dialout
   # activate chages
   $ su - $USER
   ```

</details>

**Flash the controller**
<details>
   <summary>Open this project in VSCode</summary>

   Run VSCode. Choose command `File --> Open folder...` and open `~/work/projects/start_ESP32_with_micropython`.
</details>

<details>
   <summary>Open terminal inside VSCode...</summary>

   Run VSCode and choose `Terminal --> New terminal`.
   New termianl windows will be opened at the bottom of the main VSCode's window.
   Project's environment would be initialized automatically.
   You will see the `(start_ESP32_with_micropython)` before prompt in terminal:
   ![Env](/img/term01.png)
   ...or run
   ```bash
   $ pipenv shell
   ```
   otherwise.

</details>

...be sure the project's environment is activated and clean the controller:
```bash
$ esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```
Write new firmware with micropython:
```bash
$ esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin
```
> :warning: If your got other controller model, copy the commands from page your downloaded the firmware file!
> Change port name and file name to correct values!

Use `Pymakr` in `VSCode` to check the result:
1. Open file `pymakr.conf` and change `address` field to correct port name.
2. Click `Pymakr Console`:
   ![Pymakr](/img/pymakr.png)
3. Terminal's window will be opened:
   ![Pymakr2](/img/pymakr02.png)
   It means we are inside controller and use Python's REPL.

   Run the code:
   ```python
   >>> from machine import Pin
   >>> p2 = Pin(2, Pin.OUT)
   >>> p2.on()
   ```
   Blue LED will light up (this example is actual only for controllers with built-in LED).

### 7. Flash the project
You have to connect to your controller: open `Pymakr` console or run `Pymakr --> Connect`.
Press right button of mouse inside file list of project and chhose the command `Pymakr --> Upload project`,
or choose this command in VSCode's status bar:
![Pymakr](/img/pymakr.png)
<details>
   <summary>Pay attention to...</summary>

   Key `sync_folder` in `pymakr.conf` set to `src`.
   It means all the uploaded files are in `src` folder.
   Each project in micropython has two main files:
   1. `boot.py`. It runs when controller resets.
   2. `main.py`. Main file with code.
   `boot.py` may be absent.

</details>
So, after project is uploaded, blue LED will flash to send SOS-signal and `SOS` will be printed in REPL.
Project will work after controller reset too.

> :warning: You have to press Ctrl+C while connect to working controller to stop working cycle and get REPL prompt.

## Conclusion
We prepare work tools and upload our first micropython project to ESP32 controller.

> :warning: Install the `picocom` useful tool:
>  ```bash
>  sudo apt install picocom
>  ```
It is more stable tool to connect to REPL:
>  ```bash
>  $ picocom /dev/ttyUSB0 -b115200
>  ```
