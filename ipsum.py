import random,datetime,pyperclip

message='Please disregard -- TESTING --'
randLoop=random.randrange(2,6)
ipsumList=[
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'Proin pretium tellus nec est accumsan finibus.',
    'Fusce sed libero ac dui euismod maximus.',
    'Sed condimentum, libero ac aliquet porta, nibh tortor convallis quam, iaculis pharetra leo erat vitae justo.',
    ]
i=0
ipsum=''
today=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def copy(ipsum):
    ipsum='['+today+']'+' '+message+' '+ipsum
    pyperclip.copy(ipsum)
    print(ipsum)

while i < randLoop:
    randomNumber=random.randrange(len(ipsumList))
    ipsum=ipsum+ipsumList[randomNumber]+' '
    i=i+1

copy(ipsum)