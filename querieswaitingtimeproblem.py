def minimumWaitingTime(queries):
	queries.sort()
	totalWaitTime = 0
	
	for idx,duration in enumerate(queries): 
		leftOfQueries = len(queries) - (idx + 1)
		totalWaitTime += duration * leftOfQueries
	return totalWaitTime