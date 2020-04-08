def estimator(data):
	input = data

	periodType = input.periodType
	timeToElapse = input.timeToElapse
	reportedCases = input.reportedCases

	factor = factor_calculator(periodType, timeToElapse)

	impact = impact(reportedCases, factor)
	severe= severeImpact(reportedCases, factor)

	newdata = {

	data: input,
	impact:{
		currentlyInfected : impact[0],
		InfectionsByRequestedTime : impact[1]
		},
	severeImpact:{
		currentlyInfected :severe[0],
		infectionsByRequestedTime : severe[1]
	}

	}
	data = newdata

	return data


def impact(reportedCases, factor):
	currently_infected_impact = reportedCases * 10
	infectionsByRequestedTime_impact = currently_infected *(2**factor)
	return [currently_infected_impact, infectionsByRequestedTime_impact]
		

def severeImpact(reportedCases, factor):
	currently_infected_severe = reportedCases * 50
	infectionsByRequestedTime_severe = currently_infected *(2**factor)
	return [currently_infected_severe, infectionsByRequestedTime_severe]
	
		
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