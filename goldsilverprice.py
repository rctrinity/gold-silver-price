# Gold Silver Price Python script v1.0.1
# RC Trinity
#  2022-04-17
if (__name__ == '__main__'):
    
    import pkg
    import json, requests
    import datetime
    import logging
    
    now = datetime.datetime.now()
    FORMAT = '[%(asctime)-15s] - [%(levelname)s] - %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    logger.info('Collecting data from Forex...')

    #gold
    url = requests.get(pkg.GoldForexURL)
    gold_json = url.text
    forex = json.loads(gold_json)
    try:
        for k in forex:
	        if k['topo']['platform'] == 'MT5':
		        logger.info('GOLD  : $'+format(k['spreadProfilePrices'][0]['ask'], ',.2f'))
    except GoldExportError:
        logger.info('Unable to retrieve GOLD price')

    #silver
    url = requests.get(pkg.SilverForexURL)
    silver_json = url.text
    forex = json.loads(silver_json)
    try:
        for k in forex:
	        if k['topo']['platform'] == 'MT5':
		        logger.info('SILVER:    $'+format(k['spreadProfilePrices'][0]['ask'], ',.2f'))
    except SilverExportError:
        logger.info('Unable to retrieve SILVER price')

quit()
