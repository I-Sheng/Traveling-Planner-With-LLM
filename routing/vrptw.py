#!/usr/bin/env python3
# Copyright 2010-2024 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START program]
"""Capacitated Vehicle Routing Problem with Time Windows (CVRPTW).

   This is a sample using the routing library python wrapper to solve a CVRPTW
   problem.
   A description of the problem can be found here:
   http://en.wikipedia.org/wiki/Vehicle_routing_problem.

   Distances are in meters and time in minutes.
"""

# [START import]
import functools
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
# [END import]


# [START data_model]
def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Locations in block unit
    data["time_matrix"] = [
            [0, 6, 9, 8, 7, 3, 6, 2, 3, 2, 6, 6, 4, 4, 5, 9, 7],
            [6, 0, 8, 3, 2, 6, 8, 4, 8, 8, 13, 7, 5, 8, 12, 10, 14],
            [9, 8, 0, 11, 10, 6, 3, 9, 5, 8, 4, 15, 14, 13, 9, 18, 9],
            [8, 3, 11, 0, 1, 7, 10, 6, 10, 10, 14, 6, 7, 9, 14, 6, 16],
            [7, 2, 10, 1, 0, 6, 9, 4, 8, 9, 13, 4, 6, 8, 12, 8, 14],
            [3, 6, 6, 7, 6, 0, 2, 3, 2, 2, 7, 9, 7, 7, 6, 12, 8],
            [6, 8, 3, 10, 9, 2, 0, 6, 2, 5, 4, 12, 10, 10, 6, 15, 5],
            [2, 4, 9, 6, 4, 3, 6, 0, 4, 4, 8, 5, 4, 3, 7, 8, 10],
            [3, 8, 5, 10, 8, 2, 2, 4, 0, 3, 4, 9, 8, 7, 3, 13, 6],
            [2, 8, 8, 10, 9, 2, 5, 4, 3, 0, 4, 6, 5, 4, 3, 9, 5],
            [6, 13, 4, 14, 13, 7, 4, 8, 4, 4, 0, 10, 9, 8, 4, 13, 4],
            [6, 7, 15, 6, 4, 9, 12, 5, 9, 6, 10, 0, 1, 3, 7, 3, 10],
            [4, 5, 14, 7, 6, 7, 10, 4, 8, 5, 9, 1, 0, 2, 6, 4, 8],
            [4, 8, 13, 9, 8, 7, 10, 3, 7, 4, 8, 3, 2, 0, 4, 5, 6],
            [5, 12, 9, 14, 12, 6, 6, 7, 3, 3, 4, 7, 6, 4, 0, 9, 2],
            [9, 10, 18, 6, 8, 12, 15, 8, 13, 9, 13, 3, 4, 5, 9, 0, 9],
            [7, 14, 9, 16, 14, 8, 5, 10, 6, 5, 4, 10, 8, 6, 2, 9, 0],
            ]
    data["numlocations_"] = len(data["time_matrix"])
    data["time_windows"] = [
            # fmt: off
            (0, 100),  # depot
            (75, 85), (75, 85),  #  1,  2
            (60, 70), (45, 55),  #  3,  4
            (0, 8), (50, 60),    #  5,  6
            (0, 10), (10, 20),   #  7,  8
            (0, 10), (75, 85),   #  9, 10
            (85, 95), (5, 15),   # 11, 12
            (15, 25), (10, 20),  # 13, 14
            (45, 55), (30, 40),
            # 15, 16
            # fmt: on
            ]
    data["service"] = [
            # fmt: off
            0,     # depot
            1, 1,  #  1,  2
            2, 4,  #  3,  4
            2, 4,  #  5,  6
            8, 8,  #  7,  8
            1, 2,  #  9, 10
            1, 2,  # 11, 12
            4, 4,  # 13, 14
            8, 8,
            # 15, 16
            # fmt: on
            ]
    data["num_vehicles"] = 4
    data["service_unit"] = 1
    data["depot"] = 0
    return data
# [END data_model]



def create_time_evaluator(data):
    """Creates callback to get total times between locations."""

    def service_time(data, node):
        """Gets the service time for the specified location."""
        return data["service"][node] * data["service_unit"]

    def travel_time(data, from_node, to_node):
        """Gets the travel times between two locations."""
        if from_node == to_node:
            travel_time = 0
        else:
            travel_time = data["time_matrix"][from_node][to_node]
        return travel_time

    total_time_ = {}
    # precompute total time to have time callback in O(1)
    for from_node in range(data["numlocations_"]):
        total_time_[from_node] = {}
        for to_node in range(data["numlocations_"]):
            if from_node == to_node:
                total_time_[from_node][to_node] = 0
            else:
                total_time_[from_node][to_node] = int(
                        service_time(data, from_node)
                        + travel_time(data, from_node, to_node)
                        )

    def time_evaluator(manager, from_node, to_node):
        """Returns the total time between the two nodes."""
        return total_time_[manager.IndexToNode(from_node)][manager.IndexToNode(to_node)]

    return time_evaluator


def add_time_window_constraints(routing, manager, data, time_evaluator_index):
    """Add Global Span constraint."""

    def service_time(data, node):
        """Gets the service time for the specified location."""
        return data["service"][node] * data["service_unit"]


    time = "Time"
    horizon = 1440 # set waiting time for time window & total routing time
    routing.AddDimension(
            time_evaluator_index,
            horizon,  # allow waiting time
            horizon,  # maximum time per vehicle
            False,  # don't force start cumul to zero
            time,
            )
    time_dimension = routing.GetDimensionOrDie(time)
    # Add time window constraints for each location except depot
    # and 'copy' the slack var in the solution object (aka Assignment) to print it
    for location_idx, time_window in enumerate(data["time_windows"]):
        if location_idx == data["depot"]:
            continue
        index = manager.NodeToIndex(location_idx)
        open_time = time_window[0] + service_time(data, location_idx)
        close_time = time_window[1]
        if open_time >= close_time:
            print(f'location: {location_idx}')
            print(f'open_time: {open_time}')
            print(f'close_time: {close_time}')
            assert("something wrong")

        open_time = int(open_time)
        close_time = int(close_time)
        print("open", open_time, "close",  close_time)
        time_dimension.CumulVar(index).SetRange(open_time, close_time)
        routing.AddToAssignment(time_dimension.SlackVar(index))
    # Add time window constraints for each vehicle start node
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        time_dimension.CumulVar(index).SetRange(
                data["time_windows"][0][0], data["time_windows"][0][1]
                )
        routing.AddToAssignment(time_dimension.SlackVar(index))
        # The time window at the end node was impliclty set in the time dimension
        # definition to be [0, horizon].
        # Warning: Slack var is not defined for vehicle end nodes and should not
        # be added to the assignment.


# [START solution_printer]
def print_solution(
        data, manager, routing, assignment
        ):  # pylint:disable=too-many-locals
    """Prints assignment on console."""
    print(f"Objective: {assignment.ObjectiveValue()}")

    intervals = assignment.IntervalVarContainer()
    for i in range(intervals.Size()):
        brk = intervals.Element(i)
        if brk.PerformedValue() == 1:
            print(
                    f"{brk.Var().Name()}:"
                    f" Start({brk.StartValue()}) Duration({brk.DurationValue()})"
                    )
        else:
            print(f"{brk.Var().Name()}: Unperformed")

    total_time = 0
    time_dimension = routing.GetDimensionOrDie("Time")
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        plan_output = f"Route for vehicle {vehicle_id}:\n"
        while not routing.IsEnd(index):
            time_var = time_dimension.CumulVar(index)
            slack_var = time_dimension.SlackVar(index)
            node = manager.IndexToNode(index)
            plan_output += (
                    f" {node}"
                    f" Time({assignment.Min(time_var)}, {assignment.Max(time_var)})"
                    f" Slack({assignment.Min(slack_var)}, {assignment.Max(slack_var)})"
                    " ->"
                    )
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        node = manager.IndexToNode(index)
        plan_output += (
                f" {node}"
                f" Time({assignment.Min(time_var)}, {assignment.Max(time_var)})\n"
                )
        plan_output += f"Time of the route: {assignment.Value(time_var)}\n"
        print(plan_output)
        total_time += assignment.Value(time_var)
    print(f"Total Time of all routes: {total_time}min")
    # [END solution_printer]


def routing(data:dict):
    """Entry point of the program."""
    # Instantiate the data problem.
    # [START data]
    # data = create_data_model()
    # [END data]

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(
            data["numlocations_"], data["num_vehicles"], data["depot"]
            )

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Add Time Window constraint
    time_evaluator_index = routing.RegisterTransitCallback(
            functools.partial(create_time_evaluator(data), manager)
            )
    add_time_window_constraints(routing, manager, data, time_evaluator_index)


    # Setting first solution heuristic (cheapest addition).
    # [START parameters]
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.ALL_UNPERFORMED
            )  # pylint: disable=no-member
    # [END parameters]

    # Solve the problem.
    # [START solve]
    assignment = routing.SolveWithParameters(search_parameters)
    # [END solve]

    # Print solution on console.
    # [START print_solution]
    if assignment:
        print_solution(data, manager, routing, assignment)
    else:
        print("No solution found!")
    # [END print_solution]


if __name__ == "__main__":
    data:dict = create_data_model()
    routing(data)
# [END program]
