## Voice assistant
### Installation
Required python v3.11 to run

Ubuntu
```sh
sudo apt install install sox ffmpeg libcairo2 libcairo2-dev python3-dev
```
Fedora
```sh
sudo dnf install gobject-introspection-devel cairo-gobject-devel python3-devel
```
Create venv
```sh
python3 -m venv /path/to/venv
source /path/to/venv/bin/activate
```
Install dependencies
```sh
pip3 install -r requirements.txt
```
Change microphone config in config.py

Microphone id:
```sh
python3 -m sounddevice
```
Download stt vosk model

https://alphacephei.com/vosk/models

Create src/api_tokens.json and paste your api tokens
### Run
```sh
cd src
python3 main.py
```
