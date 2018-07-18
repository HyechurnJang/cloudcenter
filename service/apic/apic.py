# -*- coding: utf-8 -*-
'''
Created on 2018. 4. 27.
@author: HyechurnJang
'''

import argparse
from acidipy import Controller

def create_application(tn_name, bd_name, ap_name, epg_names):
    controller = Controller('10.72.86.21', 'admin', '1234Qwer')
    tenant = controller.Tenant.create(name=tn_name)
    bd = tenant.BridgeDomain.create(name=bd_name)
    ap = tenant.AppProfile.create(name=ap_name)
    epgs = []
    for epg_name in epg_names:
        epg = ap.EPG.create(name=epg_name)
        epg.relate(bd)
        epgs.append(epg)
    controller.close()

def delete_application(tn_name, bd_name, ap_name, epg_names):
    controller = Controller('10.72.86.21', 'admin', '1234Qwer')
    tenant = controller.Tenant(tn_name)
    bd = tenant.BridgeDomain(bd_name)
    ap = tenant.AppProfile(ap_name)
    epgs = ap.EPG.list()
    for epg in epgs: epg.delete()
    ap.delete()
    bd.delete()
    tenant.delete()
    controller.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-m', '--mode', help='Working Mode (create|delete)', required=True)
    parser.add_argument('-t', '--tenant', help='Tenant Name', required=True)
    parser.add_argument('-b', '--bridgedomain', help='Bridge Domain Name', required=True)
    parser.add_argument('-a', '--application', help='Application Name', required=True)
    parser.add_argument('-e', '--epgs', help='Endpoint Group List', required=True)
    
    args = parser.parse_args()
    mode = args.mode
    tn_name = args.tenant
    bd_name = args.bridgedomain
    ap_name = args.application
    epg_names = args.epgs.split(',')
    
    print mode, tn_name, bd_name, ap_name, epg_names
    
    if mode == 'create': create_application(tn_name, bd_name, ap_name, epg_names)
    elif mode == 'delete': delete_application(tn_name, bd_name, ap_name, epg_names)
    
    

    
