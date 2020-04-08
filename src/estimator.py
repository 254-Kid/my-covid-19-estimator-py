finaldata = {

	"data":{},
	"impact":{},
	"severeImpact":{}

	}

def estimator(data):
	newdata = data
	periodType = newdata["periodType"]
	timeToElapse = newdata["timeToElapse"]
	reportedCases = newdata["reportedCases"]
	factor = factor_calculator(periodType, timeToElapse)

	impact(reportedCases, factor)
	severeimpact(reportedCases, factor)

	finaldata["data"] = data

	data = finaldata
	return data

def impact(reportedCases, factor):
	currently_infected = reportedCases * 10
	InfectionsByRequestedTime = currently_infected *(2**factor)
	finaldata["impact"]["currently_infected"] = currently_infected
	finaldata["impact"]["InfectionsByRequestedTime"] = InfectionsByRequestedTime
	return

	

def severeImpact(reportedCases, factor):
	currently_infected = reportedCases * 50
	InfectionsByRequestedTime = currently_infected *(2**factor)
	finaldata["severeImpact"]["currently_infected"] = currently_infected
	finaldata["severeImpact"]["InfectionsByRequestedTime"] = InfectionsByRequestedTime
	return
	
#Function to calculate and return the factor with all period type variations
def factor_calculator(periodType, timeToElapse):
	if periodType == "days":
		days = timeToElapse
	elif periodType == "weeks":
		days = 7 * timeToElapse
	elif periodType == "months":
		days = 30 * timeToElapse

	factor = days//3

	return factor