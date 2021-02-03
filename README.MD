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

 run `python ./note_seq.py`
-You will be prompt for a hex code and your desired scale.
-The script will export a midi file that needs to brought into a DAW or audio software


## Plans

- Automatically pull hash from github (or make it less manual)
- Make muliple rule sets
- Make a bit more modular (code base not sythesis)
- Play notes in a key/mode based on the hash (the same hash should generate the same audio months later)
- Multi-hash (generation)
- Note Triggers then note dictation (binary seq)

### Code Basics
"**note_seq.py**" is the only file that is currently generating midi files



