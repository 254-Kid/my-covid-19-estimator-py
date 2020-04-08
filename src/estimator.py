import json

def estimator(data):
	newdata = data
	periodType = data['periodType']
	timeToElapse = data['timeToElapse']
	reportedCases = data['reportedCases']

	#factor = factor_calculator(periodType, timeToElapse)

	i = impact(reportedCases, factor_calculator(periodType, timeToElapse))
	s = severeimpact(reportedCases, factor_calculator(periodType, timeToElapse))

	newdict = {
		'data':data,
		'impact':{'currentlyInfected' : i[0], 'infectionsByRequestedTime' : i[1]},
		'severeImpact':{'currentlyInfected' :s[0], 'infectionsByRequestedTime' : s[1]}
	}

	data = json.dumps(newdict)

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

	return days//3
