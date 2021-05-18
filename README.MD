# Music 16
## Idea
The midi files are generated with the 40 character hash from github commits.


Current scripts are using 
- Python 3 
- [MIDIUtil](https://pypi.org/project/MIDIUtil/)

## Install

-Clone repo and cd into the main directory
-install requirements using `pip install -r requirements.txt`


## Usage 

 run `python3 ./note_seq.py`
-You will be prompt for a hex code and your desired scale.
-The script will export a midi file that needs to brought into a DAW or audio software


## Plans

- Automatically pull hash from github (or make it less manual)
- "DRY" Code. Break apart into different files (Math, String Manipulation, Midi file export)
- Add arguments to python scripts to turn off features
- Tie consecutive notes together as one long note
- Hex dictates Tempo
- Hex dictates Note duration
- Make muliple rule sets

### Code Basics
"**note_seq.py**" is the only file that is currently generating midi files



