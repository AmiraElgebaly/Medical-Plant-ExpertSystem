from pyknow import *

class human(Fact):
    pass
class plant(Fact):
    pass
class exhuman(KnowledgeEngine):

    boollen=0
    @ Rule(human(symp=MATCH.symp,age=MATCH.age))
    def checksymp(self, symp,age):

        if int(age) <=5:
            list1 = symp.split(",")
            count = 0
            for x in list1:
                if x == "shakiness" or x == "hunger" or x == "sweating" or x == "headache" or x == "pale":
                    count += 1
            if count >= 2:
                booll=0
                for x in list1:
                    if x == "diabetic parents" :
                         print("the patient could be diabetic 😞 ")
                         booll=1
                         self.boollen=1
                         break
                if booll==0:
                    print("he/she has signs of low sugar 😞 ")
                    self.boollen = 1

    @Rule(human(symp=MATCH.symp, age=MATCH.age))
    def checksymp2(self, symp, age):
        if int(age) <= 5:
            list1 = symp.split(",")
            count = 0
            for x in list1:

                if x == "thirst" or x == "blurred vision" or x == "headache" or x == "dry mouth" or x == "smelling breath" or x=="shortness of breath":
                    count += 1
            if count >= 2:
                print("he / she has sign of high sugar 😞 ")
                self.boollen = 1

    @Rule(human(symp=MATCH.symp,age=MATCH.age))
    def checksymp3(self, symp,age):
        if int(age) <= 5:
            list1 = symp.split(",")
            count = 0
            for x in list1:

                if x == "cold" or x == "brownish-pink rash" or x == "high temperature" or x == "fast temperature" or x == "bloodshot eyes" or x == "white spots inside cheek":
                    count += 1
            if count == 6:
                print("he / she has sign of measles 😞 ")
                self.boollen = 1

    @Rule(human(symp=MATCH.symp, age=MATCH.age))
    def checksymp4(self, symp, age):
        if int(age) <= 5:
            list1 = symp.split(",")
            count = 0
            for x in list1:
                if x == "moderate temperature" or x == "saliva is not normal" or x == "swollen lymph" or x == "mouth dry":
                    count += 1
            if count == 4:
                print("he / she has sign of mumps 😞 ")
                self.boollen = 1


    @Rule(human(symp=MATCH.symp))
    def checksymp5(self, symp):

        list1 = symp.split(",")
        count = 0
        for x in list1:
            if x == "runny nose" or x == "harsh cough":
                count += 1
        if count == 2:
            print("he / she has sign of cold 😞 ")
            self.boollen = 1


    @Rule(human(symp=MATCH.symp, age=MATCH.age))
    def checksymp6(self, symp, age):
        if int(age) >5:
            list1 = symp.split(",")
            count = 0
            for x in list1:
                if x == "cold" or x == "conjunctives" or x == "strong body aches" or x == "weakness" or x == "vomiting" or x == "sore throat" or x == "sneezing":
                    count += 1
            if count == 7:
                print("he / she has sign of adult-flu😞 ")
                self.boollen = 1

    @Rule(human())
    def checksympp7(self):

        if self.boollen == 0:
            print("the human hasn't any  thing")

    @Rule(human(symp=MATCH.symp, age=MATCH.age))
    def checksymp7(self, symp, age):
        if int(age) <= 5:
            list1= symp.split(",")
            count = 0
            for x in list1:

                if x == "cold" or x == "conjunctives" or x == "strong body aches" or x == "weakness" or x == "vomiting" or x == "sore throat" or x == "sneezing":
                    count += 1
            if count == 7:
                print("he / she has sign of child-flu😞 ")
                self.boollen = 1

 #-------------------------------------------------------------------------------

    @Rule(plant(symp=MATCH.symp))
    def checksympp1(self, symp):

            list = symp.split(",")
            count=0
            for x in list:

                if x == "high temperature" or x == "normal humidity" or x == "tuber color is reddish-brown" or x == "tuber has spots":
                    count+=1
            if count==4:
                print("the plant has black heart 😞 ")
                self.boollen = 1

    @Rule(plant(symp=MATCH.symp))
    def checksympp2(self, symp):

            list = symp.split(",")
            count = 0
            for x in list:

                if x == "low temperature" or x == "high humidity" or x == "normal tuber" or x == "tuber has spots":
                    count += 1
            if count==4:
                print("the plant has late blight 😞 ")
                self.boollen = 1

    @Rule(plant(symp=MATCH.symp))
    def checksympp3(self, symp):

            list = symp.split(",")
            count = 0
            for x in list:

                if x == "high temperature" or x == "normal humidity" or x == "tuber is dry" or x == "tuber has circles":
                    count += 1
            if count == 4:
                print("the plant has dry rot😞 ")
                self.boollen = 1

    @Rule(plant(symp=MATCH.symp))
    def checksympp4(self, symp):

            list = symp.split(",")
            count = 0
            for x in list:

                if x == "normal temperature" or x == "normal humidity" or x == "tuber color is brown" or x == "tuber has wrinkles":
                    count += 1
            if count == 4:
                print("the plant has early blight😞 ")
                self.boollen = 1

    @Rule(plant())
    def checksympp5(self):

       if self.boollen ==0:
           print("the plant hasn't any thing")


def main():
    patientorplant = exhuman()
    patientorplant.reset()
    type=input("enter type do you want to examine (plant/human)")
    if(type=='plant'):
        patientorplant.declare(plant(symp=input("enter the symps")))
        patientorplant.run()
    elif(type=='human'):
        patientorplant.declare(human(age=input("enter the age"),symp=input("enter the symps")))
        patientorplant.run()

main()