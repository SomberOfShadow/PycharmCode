#!/usr/bin/python
# --*--coding=utf-8--*--

import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')


def printRecord(tgt):
    rec = gi.record_by_addr(tgt)
    city = rec['city']
    region = rec['region_code']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print('[*] 主机: ' + tgt + ' Geo-located.')
    print('[+] ' + str(city) + ', ' + str(region) + ', ' + str(country))
    print('[+] 经度: ' + str(lat) + ', 维度: ' + str(long))

tgt = '183.141.110.74'
printRecord(tgt)