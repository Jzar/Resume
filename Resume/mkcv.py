#mkcv is a command line utility for quickly tailoring a cv to a job posting

#IN DEVELOPMENT

#CONSTANTS
PATH = "/home/jacob/Documents/Resume/resume/"
COLOURS = [ "emerald","skyblue","red","pink","orange","nephritis","concrete","darknight"]
SECTIONS=["summary","projects","experience","education","extracurriculars"]
LANGUAGES = 14
TOOLS = 15
MAN ="""
mkcv is a command line utility for quickly taloring a cv to a job posting.

It is built around the Awesome-CV LaTeX template by Claud D. Park, but can be modified to support the users own document

Main Function:

arg0 mkcv
arg1 company
arg2 title ( with _ for spaces)
arg3-N skills

ex

mkcv Google Software_Engineer python jupyter TensorFlow
Flags:

-p : prebuilt
        - data science
        - general
        - app development
        - security
-b : bolds terms provided

-f : adjust font
        - arg1 : size
-colour : modify the colour in the resume
        - arg1 :
            -f for full colour
            -c for partial
        - arg2 :
            - colour name
                supported: red, green, blue, pink, emerald
-cl : cover-letter mode.
"""

#FUNCTIONS
def doc(section):
    f = open(PATH+section+".tex","r")
    temp = f.read()
    f.close()
    return temp
def bold(word):
    for section in SECTIONS:
        bolding(word,section)
def unbold(word):
    for section in SECTIONS:
        unbolding(word,section)
def unbolding(word,section):
    do = doc(section).replace("\\textbf{"+word+"}",word)
    f = open( PATH+section+".tex","w")
    f.write(do)
def bolding(word,section):
    do = doc(section).replace(word,"\\textbf{"+word+"}")
    f = open( PATH+section+".tex","w")
    f.write(do)

def readLine(num,section):
    f = doc(section).split('\n')
    assert( num-1 <= len(f))
    temp = f[num-1]

    return temp
def writeLine(num, content,section):
    f = doc(section).split('\n')
    assert( num-1 <= len(f))
    f[num-1] = content
    w = open(PATH+section+".tex",'w')
    for line in f: w.write(line+"\n")
    w.close()
def comment(section,start,end = -1):
    if end == -1: end = start
    f = doc(section).split('\n')
    for i in range(start,end):
        f[i-1] = "%"+f[i-1]
    w = open(PATH+section+".tex","w")
    for line in f: w.write(line)

def uncomment(section,start):
    if end == -1: end = start

    f = doc(section).split('\n')
    for i in range(start,end):
        f[i-1] = f[i-1][1:]
    w = open(PATH+section+".tex","w")
    for line in f: w.write(line)
def colour(colour):
    if (colour not in COLOURS):
        return
    else:
        writeLine(32,"\colorlet{awesome}{awesome-"+colour+"}")
def main(argv):
    company = argv[1].replace('_',' ')
    title = argv[2].replace('_',' ')
    languages = argv[4:argv.index('-t')]
    tools = argv[argv.index('-t')+1:]
    L = readLine(LANGUAGES,'summary')
    T = readLine(TOOLS, 'summary')
    for l in languages:
        L = L.replace(' '+l+',',"")
        L = L.replace(': ',': '+" \\textbf{"+l+"}, ")
    for t in tools:
        T = T.replace(' '+t+',',"")
        T = T.replace(': ',': '+" \\textbf{"+t+"}, ")
    print(T,'\n',L)
    writeLine(LANGUAGES,L, 'summary')
    writeLine(TOOLS,T,'summary')

#initializing program
from sys import argv

#determine state of program
#__________________________

#prebuilt
if argv[1] == '-p':
    print ( "p")
#bold
elif argv[1] =='-b':
    for i in argv[2:]:
        bold(i)
#remove bold
elif argv[1] =='-rb':
    for i in argv[2:]:
        unbold(i)
#font
elif argv[1] =='-f':
    print("f")
#colour
elif argv[1] =='-colour':
    print("colour")
#skills
elif argv[1] =='-s':
    print("s")
elif argv[1] == '-h':
    print (MAN)
else:
    main(argv)
