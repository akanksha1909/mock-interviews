"""
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively;
that is, the next trip can start immediately after completing the current trip.
Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total.
Return the minimum time required for all buses to complete at least totalTrips trips. 

Example:
time = [1,2,3], totalTrips = 5
Output = 3
-----------------------------------------------------------------------------------------------------------------
at least one bus
at least one trip
-----------------------------------------------------------------------------------------------------------------
3 buses
5 trips

bus 1 -> 3 trips (3 time)
bus 2 -> 1 trip (2 time)
bus 3 -> 1 trip (3 time)
"""

"""
1 - 1 (1) 2(0) 3(0)
2 - 1 (2) 2(1) 3(0)
3 - 1 (3) 2(1) 3(1)
"""

"""
length - 10 ^ 8
"""
def canCompleteTripsInTime(currentTime, time, totalTrips):
    tripsCompleted = 0
    for t in time:
        tripsCompleted += (currentTime//t)
    return tripsCompleted >= totalTrips

def minimumTime(time, totalTrips):
    low = 1
    high = min(time)*totalTrips
    # O(log(high)*O(l))
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if canCompleteTripsInTime(mid, time, totalTrips):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans