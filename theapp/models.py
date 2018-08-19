import random

raceList = ['white', 'black', 'native american','asian','hispanic']
genderList = ['male', 'female']
sexualityList = ['straight','gay','bisexual']


class characterMaker():
    def race(self, list=raceList):
        selection = random.randint(0,len(list)-1)
        return list[selection]

    def age(self, low_age=12, high_age=100):
        selection = random.randint(low_age, high_age)
        return selection

    def gender(self, list=genderList):
        selection = random.randint(0, len(list)-1)
        return list[selection]

    def sexuality(self, list=sexualityList):
        selection = random.randint(0, len(list)-1)
        return list[selection]