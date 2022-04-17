# Gold Silver Price Python script v1.0.1
# RC Trinity
#  2022-04-17
if (__name__ == '__main__'):
    
    import pkg
    from pkg import *
    import json, requests
    import datetime
    import logging
    
    now = datetime.datetime.now()
    logger = logging.getLogger(__name__)
    logger.setLevel('INFO')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(ColorLogFormatter())
    logger.addHandler(stream_handler)

    logger.info('Collecting data from Forex...', extra={'prefix': Color.GREEN, 'suffix': Color.END})

    #gold
    url = requests.get(pkg.GoldForexURL)
    gold_json = url.text
    forex = json.loads(gold_json)
    try:
        for k in forex:
	        if k['topo']['platform'] == 'MT5':
		        logger.info('GOLD    : $'+format(k['spreadProfilePrices'][0]['ask'], ',.2f'), extra={'prefix': Color.YELLOW, 'suffix': Color.END})
    except:
        logger.info('Unable to retrieve GOLD price', extra={'prefix': Color.RED, 'suffix': Color.END})

    #silver
    url = requests.get(pkg.SilverForexURL)
    silver_json = url.text
    forex = json.loads(silver_json)
    try:
        for k in forex:
	        if k['topo']['platform'] == 'MT5':
		        logger.info('SILVER  :    $'+format(k['spreadProfilePrices'][0]['ask'], ',.2f'), extra={'prefix': Color.SILVER, 'suffix': Color.END})
    except:
        logger.info('Unable to retrieve SILVER price', extra={'prefix': Color.RED, 'suffix': Color.END})

    #BTC
    logger.info('Collecting data from CoinDesk...', extra={'prefix': Color.GREEN, 'suffix': Color.END})
    url = requests.get(pkg.BtcURL)
    btc_json = url.text
    btc = json.loads(btc_json)
    try:
        btc_f = float(btc['bpi']['USD']['rate'].replace(',',''))
        satusd = (1/(btc_f * 0.00000001))
        logger.info('BITCOIN :$'+format(btc_f, ',.2f'), extra={'prefix': Color.ORANGE, 'suffix': Color.END})
        logger.info('SATs/USD:     '+format(satusd, ',.0f'), extra={'prefix': Color.ORANGE, 'suffix': Color.END})
    except:
        logger.info('Unable to retrieve BTC price', extra={'prefix': Color.RED, 'suffix': Color.END})

quit()
