class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       cars = sorted(zip(position, speed))
       fleets = 0
       leader_time = -1
       for car in cars[::-1]:
        arrival = (target - car[0]) / car[1]
        if arrival > leader_time:
            fleets += 1
            leader_time = arrival
       return fleets