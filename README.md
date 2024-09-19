# Project-VIVA---Personal-Desktop-Assistant   
This is a personal desktop assistant which will do few tasks for you. It is currently in <b>LEVEL - 1</b> development process where the tasks which can be performed are limited and need manual coding for it instead of any automation.

### What can you do with VIVA : 

* Ask time and day
* Ask to open google,brave,youtube,stack overflow
* take screenshot of current screen
* record your voice
* Open calender and look into the calender of any year you desire
* Generate a new password for you

The current code is very rigid and has fixed to perform particular task. Looking forward to improve the effectiveness of the assistant and automate it.

## What are the requirements of workspace to run the program 

<p>
    <h3>Installing libraries</h3>
- To give commands to <strong> VIVA </strong> and perform tasks.</br>
    
```
pip install speechRecognition 
```

- This module is used to access camera for capturing images.</br>

```
pip install opencv-python 
```

- This library helps <strong>VIVA</strong> to speak ask which task to perform from the user.</br> 

```
pip install PyAudio 
```

- To make <strong>ASHWATHAMA</strong> take screenshots and save easily

```
pip install Pillow
```

</p>

## Some extra information about VIVA you can explore and experiment with.
<p>In <strong>takeCommand()</strong> function <i>r.pause_threshold</i> is parameter to increase the time to wait for assistant so that if u take a small pause wantedly or unwantedly, the assistant should not stop listening and execute incomplete tasks. In short, the more the pause_threshold, the more time you can pause after a command is given.</p>
<p>Also, along with it another parameter is also used which is called <i>r.energy_threshold</i>, which decreases the sensitivity of its input with increase in its value. The more the energy_threshold the more you need to shout for giving the commands to USHVATHAMA.</p>

## Future work to be done : 
* Automating VIVA as much as possible, training a model and integrating it with the code so that the rigidness in the commands can be eliminated and the assistant can respond to the commands accordingly even if phrased differently.
* Making the code understandable to any individual, make it robust in nature.

### For complaints or compliments 
### Do email me - vamsidhard2002@gmail.com

<h1 align="center">Also you can find me on :-</h1>
<p align="center">
  <a href="https://twitter.com/ImVamsi2002">
    <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=plastic&logo=twitter&logoColor=white" height=20></a>
  <a href="https://www.instagram.com/thevamsi2395/">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?&style=plastic&logo=instagram&logoColor=white" height=20></a>
  <a href="https://www.facebook.com/dvamsidhar">
    <img src="https://img.shields.io/badge/Facebook-%234267B2.svg?&style=plastic&logo=facebook&logoColor=white" height=20></a>
  <a href="https://stackoverflow.com/users/19970419/d-vamsidhar">
    <img src="https://img.shields.io/badge/Stack Overflow-%23F48024.svg?&style=plastic&logo=stackoverflow&logoColor=white" height=20></a>
  <a href="https://www.hackerrank.com/dvamsidhar">
    <img src="https://img.shields.io/badge/-Hackerrank-2EC866?&style=plastic&logo=HackerRank&logoColor=white" height=20></a>
  <a href="https://www.linkedin.com/in/dvamsidhar5932200802/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?&style=plastic&logo=linkedin&logoColor=white" height=20></a>
</p>
