def estimator(data):
	newdata = data
	periodType = newdata['periodType']
	timeToElapse = newdata['timeToElapse']
	reportedCases = newdata['reportedCases']

	factor = factor_calculator(periodType, timeToElapse)

	i = impact(reportedCases, factor)
	s = severeimpact(reportedCases, factor)

	newdict = {
		'data':newdata,
		'impact':{'currentlyInfected' : i[0], 'infectionsByRequestedTime' : i[1]},
		'severeImpact':{'currentlyInfected' :s[0], 'infectionsByRequestedTime' : s[1]}
	}
	data = newdict

	return data


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
