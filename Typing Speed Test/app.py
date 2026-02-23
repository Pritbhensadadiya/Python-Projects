from time import *
import random as r


def misktake (partest,usertest):
    error = 0
    for i in range (len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error   

def speed_time (time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R   
    return round(speed)

    
test = [
    "Python is a versatile programming language used in web development, data science, artificial intelligence, and automation due to its simplicity and readability.",
    "In today's evolving technological world, learning Python can enhance problem-solving skills and create many career opportunities across industries.",
    "Data analysis involves collecting and interpreting data to find patterns and insights that help businesses make better decisions.",
    "Machine learning is a part of artificial intelligence that enables systems to learn from data and make decisions with minimal human input.",
    "Web development involves building and maintaining websites using technologies like HTML, CSS, JavaScript, and backend languages such as Python.",
    "Natural language processing helps computers understand and generate human language, enabling chatbots, translators, and voice assistants.",
    "Software development includes planning, coding, testing, and maintaining applications to meet user requirements and perform efficiently.",
    "Cybersecurity protects systems and data from digital attacks, ensuring information security and preventing unauthorized access.",
    "Cloud computing allows users to store and access data online, making applications scalable, cost-effective, and accessible anywhere.",
    "Artificial intelligence enables machines to perform tasks like speech recognition, decision-making, and language translation.",
]

test1 = r.choice(test)
print ("~~~ TYPING SPEED ~~~")
print(test1)
print()
print()
time_1 = time()
testinput = input(" Enter : ")
time_2 = time()

print("Speed : ",speed_time(time_1,time_2,testinput),"W/Sec")
print("Error", misktake(test1,testinput))
