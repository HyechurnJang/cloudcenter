# -*- coding: utf-8 -*-
'''
Created on 2018. 4. 27.
@author: HyechurnJang
'''

from acidipy import Controller
from pygics import rest, Lock

lock = Lock()
controller = Controller('10.72.86.21', 'admin', '1234Qwer')

def create_application(tn_name, bd_name, ap_name, epg_names):
    lock.on()
    try:
        tenant = controller.Tenant.create(name=tn_name)
        bd = tenant.BridgeDomain.create(name=bd_name)
        ap = tenant.AppProfile.create(name=ap_name)
        epgs = []
        for epg_name in epg_names:
            epg = ap.EPG.create(name=epg_name)
            epg.relate(bd)
            epgs.append(epg)
    except Exception as e:
        print str(e)
        ret = {'result' : None, 'error' : str(e)}
    else:
        ret = {
            'result' : {
                'tn' : tenant,
                'bd' : bd,
                'ap' : ap,
                'epgs' : epgs
            }
        }
    lock.off()
    return ret

def delete_application(tn_name, bd_name, ap_name, epg_names):
    lock.on()
    try:
        tenant = controller.Tenant(tn_name)
        bd = tenant.BridgeDomain(bd_name)
        ap = tenant.AppProfile(ap_name)
        epgs = ap.EPG.list()
        for epg in epgs: epg.delete()
        ap.delete()
        bd.delete()
        tenant.delete()
    except Exception as e:
        print str(e)
        ret = {'result' : False, 'error' : str(e)}
    else:
        ret = {'result' : True}
    lock.off()
    return ret

@rest('GET', '/apic/create')
def create(request, tn_name, bd_name, ap_name, epg_names):
    epg_names = epg_names.split(',')
    return create_application(tn_name, bd_name, ap_name, epg_names)

@rest('GET', '/apic/delete')
def delete(request, tn_name, bd_name, ap_name, epg_names):
    epg_names = epg_names.split(',')
    return delete_application(tn_name, bd_name, ap_name, epg_names)