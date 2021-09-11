### This is opensource code project
### Support for Mu Online Gammer for
### Training, AFK, Reset, Uplevel...
### Support: Upper SS6
'''
# Author: Kien Tran
# Email: kien@kienoi.com
# Donation:
# - Paypal: paypal.me/kienoi
# - MoMo: 0888815552
# Thank you!
'''

def mu_client():
    click("mumain.PNG")
    wait(1)

def chat(mes):
    mu_client()
    wait(1)
    type(Key.ENTER + mes)
    wait(1)
    type(Key.ENTER)
    wait(1)

def chon_nv():
    ## Select main
    mu_client()
    wait(2)
    doubleClick(find("1631261711418.png"))
    ## Waiting load game
    wait(4)


def party():
## Move to team PT
    mu_client()
    #click(Pattern("1631334477799.png").targetOffset(104,2))
    click(Pattern("1631334687513.png").targetOffset(2,79))
    click("1631253455667.png")

def reset():
    mu_client()
    while not exists("1631261711418.png"):
        chat("/reset")
        wait(20)
            
    wait(2)

def helper_off():
    mu_client()
    if exists("map.PNG"):
        click("helper-1.PNG")

def congdiem():
    mu_client()
    wait(2)
    type(Key.ENTER + "/addstr 31000")
    wait(1)
    type(Key.ENTER)
    wait(1)
    type(Key.ENTER + "/addagi 15000")
    wait(1)
    type(Key.ENTER)
    wait(1)
    type(Key.ENTER + "/addvit 22000")
    wait(1)
    type(Key.ENTER)
    wait(1)
    type(Key.ENTER + "/addene 8000")
    wait(1)
    type(Key.ENTER)

def runMu():
    for rs in range(15):
        reset()
        chon_nv()
        congdiem()
        party()
        #wait(50)
        #chat("Remind - Keep PM in the spot!!!")
        #chat("It easy for us to go there!!!")
        #chat("BTW! When you rs, Dont put key to me")

if __name__ == "__main__":
    runMu()
    #single()
