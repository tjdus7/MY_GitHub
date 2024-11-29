class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
    
houses = []
house1 = House('강남', '토지매매', '전세', '12억', '2020년')
house2 = House('마포', '땅덩이', '전세', '4억', '2021년')
house3 = House('송파', '땅덩이', '월세', '500/10', '1999년')

houses.append(house1)
houses.append(house2)
houses.append(house3)

print('총 {} 대의 매물이 있다.'.format(len(houses)))
for house in houses:
    house.show_detail()