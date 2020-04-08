def estimator(input_data):
    impact = {}
    severeImpact = {}
    ###Normalizing the duration to just days
    duration = duration_normaliser(input_data['periodType'],input_data['timeToElapse'])
    
    ##CHALLENGE 1
    ###calculating the estimated infections by the time duration
    ##IMPACT
    impact['currentlyInfected']=input_data['reportedCases'] * 10
    impact['infectionsByRequestedTime'] = impact['currentlyInfected']*(pow(2,duration//3))
    ##SEVEREIMPACT
    severeImpact['currentlyInfected']=input_data['reportedCases']*50
    severeImpact['infectionsByRequestedTime'] =severeImpact['currentlyInfected']*(pow(2,duration//3))
    
    
    output_data = {'data':input_data, 'impact':impact, 'severeImpact': severeImpact}
    
    return output_data

def duration_normaliser(duration ,value):
    if duration == "months":
        value *= 30
    elif duration == "weeks":
        value *= 7

    return value
