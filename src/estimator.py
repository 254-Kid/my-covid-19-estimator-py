def estimator(data):

	periodType = data.periodType
	timeToElapse = data.timeToElapse
	reportedCases = data.reportedCases

	factor = factor_calculator(periodType, timeToElapse)

	impact(reportedCases, factor)
	severeImpact(reportedCases, factor)



	def impact(reportedCases, factor):
		global currently_infected_impact
		global InfectionsByRequestedTime_impact
		currently_infected_impact = reportedCases * 10
		InfectionsByRequestedTime_impact = currently_infected *(2**factor)
		

	def severeImpact(reportedCases, factor):
		global currently_infected_severeImpact
		global InfectionsByRequestedTime_severeImpact
		currently_infected_severeImpact = reportedCases * 50
		InfectionsByRequestedTime_severeImpact = currently_infected *(2**factor)
	
		
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

	impact(reportedCases, factor)
	severeImpact(reportedCases, factor)

	return {

	data:{data},
	impact:{
		currentlyInfected : currently_infected_impact,
		InfectionsByRequestedTime : InfectionsByRequestedTime_impact
		},
	severeImpact:{
		currentlyInfected :currently_infected_severeImpact
		infectionsByRequestedTime : InfectionsByRequestedTime_severeImpact
	}

	}