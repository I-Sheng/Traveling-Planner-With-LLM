from distance_matrix import travel_time
from vrptw import routing
from data_time import convert_time_windows, get_stay_time

def create_data_model(day:int, sites: list):
    data = {}
    data["time_matrix"] = travel_time(sites)
    data["numlocations_"] = len(data["time_matrix"])
    data["name"] = sites
    data["time_windows"] = convert_time_windows(sites)
    data["service"] = get_stay_time(sites)
    data["num_vehicles"] = day
    data["service_unit"] = 1
    data["depot"] = 0
    return data



def main(day:int, sites:str):
    sites = sites.split(', ')
    data = create_data_model(day, sites)
    print(data)
    routing(data)



if __name__ == "__main__":
    main(2, "射日塔, 嘉義樹木園, Eleventh Cafe 射日塔景觀咖啡館, 北香湖公園, 嘉義市環市自行車道, 嘉義文化創意產業園區, 堀川茶事")
    # convert_time_windows("射日塔, 嘉義樹木園, Eleventh Cafe 射日塔景觀咖啡館, 北香湖公園, 嘉義市環市自行車道, 嘉義文化創意產業園區, 堀川茶事".split(', '))

