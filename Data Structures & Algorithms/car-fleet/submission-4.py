class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       carlist = sorted(zip(position, speed))
       cars = reversed(carlist)
       fleets = 0
       leader_time = -1
       for car in cars:
        arrival = (target - car[0]) / car[1]
        if arrival > leader_time:
            fleets += 1
            leader_time = arrival
       return fleets