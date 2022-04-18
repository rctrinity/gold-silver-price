# usdsats Python script v1.0.0
# Converts US Dollar amount into satoshis 
# RC Trinity
#  2022-04-17
if (__name__ == '__main__'):
    
    import pkg
    from pkg import *
    import json, requests
    import datetime
    import sys
    
    logger = logging.getLogger(__name__)
    logger.setLevel('INFO')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(ColorLogFormatter())
    logger.addHandler(stream_handler)
    
    try:
        dollarmt = sys.argv[1]
        dollaramt_f = float(dollarmt.replace(',',''))
    except:
        logger.info('Usage: usdsats.py ##.##', extra={'prefix': Color.RED, 'suffix': Color.END})
        quit()
    #BTC
    logger.info('Collecting data from CoinDesk...')
    url = requests.get(pkg.BtcURL)
    btc_json = url.text
    btc = json.loads(btc_json)
    try:
        btc_f = float(btc['bpi']['USD']['rate'].replace(',',''))
        satusd = (1/(btc_f * 0.00000001))
        result = (dollaramt_f*satusd)
        logger.info('$'+format(dollaramt_f, ',.2f')+' = '+format(result, ',.0f')+' satoshis')
    except:
        logger.error('Error retrieving Bitcoin data', extra={'prefix': Color.RED, 'suffix': Color.END})

quit()
