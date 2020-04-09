def estimator(data):
    impact = {}
    severeImpact = {}
    reportedCases = data['reportedCases']
    periodType = data['periodType']
    timeToElapse = data['timeToElapse']
    totalHospitalBeds = data['totalHospitalBeds']

    ###Normalizing the duration to just days
    duration = duration_to_days(periodType, timeToElapse)
    factor = duration//3
    
    #CHALLENGE 1

    #For Impact
    impact['currentlyInfected'] = reportedCases * 10
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * (pow(2,factor))

    #For Severe Impact
    severeImpact['currentlyInfected'] = reportedCases * 50
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected']*(pow(2,factor))

    #CHALLENGE 2

    #For Impact
    impact['severeCasesByRequestedTime'] = severeImpact['infectionsByRequestedTime'] * 0.15
    impact['hospitalBedsByRequestedTime'] = beds_available(totalHospitalBeds, impact['severeCasesByRequestedTime'])


    #For Severe Impact
    impact['severeCasesByRequestedTime'] = severeImpact['infectionsByRequestedTime'] * 0.15
    impact['hospitalBedsByRequestedTime'] = beds_available(totalHospitalBeds, impact['severeCasesByRequestedTime'])





    output = {'data':input_data, 'impact':impact, 'severeImpact': severeImpact}

    return output

def duration_to_days(durationType ,time):
    if durationType == "months":
        time *= 30
    elif durationType == "weeks":
        time *= 7

    return time

#calculating the number of beds available
def beds_available(totalbeds,severecases):
    available_beds = (0.35 * totalbeds) - severecases
    return available_beds


