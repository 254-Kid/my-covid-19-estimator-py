def estimator(data):
	newdata = data
	periodType = newdata.periodType
	timeToElapse = newdata.timeToElapse
	reportedCases = newdata.reportedCases

	factor = factor_calculator(periodType, timeToElapse)



	i = impact(reportedCases, factor)
	s = severeimpact(reportedCases, factor)

	return {
		data:newdata,
		impact:{currentlyInfected : impact[0], InfectionsByRequestedTime : impact[1]},
		severeImpact:{currentlyInfected :severe[0], infectionsByRequestedTime : severe[1]}
	}


def impact(reportedCases, factor):
	currently_infected = reportedCases * 10
	InfectionsByRequestedTime = currently_infected *(2**factor)
	return [currently_infected, InfectionsByRequestedTime]

	

def severeimpact(reportedCases, factor):
	currently_infected = reportedCases * 50
	InfectionsByRequestedTime = currently_infected *(2**factor)
	return [currently_infected, InfectionsByRequestedTime]
	

def factor_calculator(periodType, timeToElapse):
	if periodType == "days":
		days = timeToElapse
	elif periodType == "weeks":
		days = 7 * timeToElapse
	elif periodType == "months":
		days = 30 * timeToElapse

	factor = days//3

	return factor
