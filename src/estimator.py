def estimator(data):
    output = {'data':data, 'impact': {}, 'severeImpact': {}}
    output['impact']['currentlyInfected'] = data['reportedCases'] * 10
    output['severeImpact']['currentlyInfected'] = data['reportedCases'] * 50
    output['impact']['infectionsByRequestedTime'] = output['impact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
    output['severeImpact']['infectionsByRequestedTime'] = output['severeImpact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
    output['impact']['severeCasesByRequestedTime'] = int(15/100 * (output['impact']['infectionsByRequestedTime']))
    output['severeImpact']['severeCasesByRequestedTime'] = int(15/100 * (output['severeImpact']['infectionsByRequestedTime']))
    output['impact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['impact']['severeCasesByRequestedTime'])
    output['severeImpact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['severeImpact']['severeCasesByRequestedTime'])
    output['impact']['casesForICUByRequestedTime'] = int(5/100 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForICUByRequestedTime'] = int(5/100 * output['severeImpact']['infectionsByRequestedTime'])
    output['impact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['severeImpact']['infectionsByRequestedTime'])
    output['impact']['dollarsInFlight'] = output['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * 30
    output['severeImpact']['dollarsInFlight'] = output['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * 30
    return output

if __name__ == "__main__":
    data = {
      'region':{
        'name':'Africa', 
        'avgAge':19.7, 
        'avgDailyIncomeInUSD':5, 
        'avgDailyIncomePopulation':0.71
      },
        'periodType':'days', 
        'timeToElapse':58, 
        'reportedCases':674, 
        'population':66622705, 
        'totalHospitalBeds':1380614
    }
    dic = estimator(data)
    print(dic)
