import pyttsx3
talk = pyttsx3.init()
talk.say("Pora puuka")
talk.say("Pedda scamei, amma baboi")



Speak =input("Talk anything")
talk.say(Speak)


talk.runAndWait()