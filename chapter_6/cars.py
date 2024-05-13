def car_info(manufacturer, model, **more_details):
    features = {}
    features['company'] = manufacturer
    features['model_number'] = model
    for key, value in more_details.items():
        features[key] = value
    return features

attributes = car_info('Honda','Honda Civic', Engine = '1339 cc - 1799 cc', Mileage = '12.9 -20 kmpl')
print(attributes,"\n")

attributes = car_info('Subaru', 'Outback', colour = ' Blue', tow_package = True)
print(attributes, "\n")