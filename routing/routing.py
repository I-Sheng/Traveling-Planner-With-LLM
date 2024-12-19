from distance_matrix import travel_time
from vrptw import routing
from data_time import convert_time_windows, get_stay_time

def create_data_model(day:int, sites: list, start_time: int, end_time:int):
    data = {}
    sites, data["time_windows"] = convert_time_windows(sites)
    sites, data["time_matrix"] = travel_time(sites)
    data["numlocations_"] = len(data["time_matrix"])
    data["name"] = sites
    data["service"] = get_stay_time(sites)
    data["num_vehicles"] = day
    data["service_unit"] = 1
    data["depot"] = 0
    data["start_time"] = start_time
    data["end_time"] = end_time
    return data



def main(day:int, sites:str, start_time:int = 480, end_time:int = 1200, start_point = '嘉義火車站'):
    sites = sites.split(', ')
    sites = [start_point] + [site for site in sites if site != start_point]
    #print(sites)
    data = create_data_model(day, sites, start_time, end_time)
    # print(data)
    return routing(data)



if __name__ == "__main__":
    main(1,  "上紅丸梅製禮品專賣, 嘉義市立美術館, 嘉大植物園, 唐妝漢方生物科技股份有限公司, 東發養蜂場, 慈龍寺, 嘉義火車站, 月桃故事館", 480, 1200 )

