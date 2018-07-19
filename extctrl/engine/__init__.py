# -*- coding: utf-8 -*-
'''
Created on 2018. 4. 27.
@author: HyechurnJang
'''

from acidipy import Controller
from pygics import rest, Lock

lock = Lock()
controller = Controller('10.72.86.21', 'admin', '1234Qwer')

@rest('GET', '/apic/create/tn')
def create_tn(request, tn_name):
    lock.on()
    try:
        tn = controller.Tenant.create(name=tn_name)
    except Exception as e:
        ret = {'result' : None, 'error' : str(e)}
    else:
        ret = {'result' : tn}
    lock.off()
    return ret

@rest('GET', '/apic/delete/tn')
def delete_tn(request, tn_name):
    lock.on()
    try:
        controller.Tenant(tn_name).delete()
    except Exception as e:
        ret = {'result' : False, 'error' : str(e)}
    else:
        ret = {'result' : True}
    lock.off()
    return ret

@rest('GET', '/apic/create/bd')
def create_bd(request, tn_name, bd_name):
    lock.on()
    try:
        tn = controller.Tenant(tn_name)
        bd = tn.BridgeDomain.create(name=bd_name)
    except Exception as e:
        ret = {'result' : None, 'error' : str(e)}
    else:
        ret = {'result' : bd}
    lock.off()
    return ret

@rest('GET', '/apic/delete/bd')
def delete_bd(request, tn_name, bd_name):
    lock.on()
    try:
        controller.Tenant(tn_name).BridgeDomain(bd_name).delete()
    except Exception as e:
        ret = {'result' : False, 'error' : str(e)}
    else:
        ret = {'result' : True}
    lock.off()
    return ret

@rest('GET', '/apic/create/ap')
def create_ap(request, tn_name, ap_name):
    lock.on()
    try:
        tn = controller.Tenant(tn_name)
        ap = tn.AppProfile.create(name=ap_name)
    except Exception as e:
        ret = {'result' : None, 'error' : str(e)}
    else:
        ret = {'result' : ap}
    lock.off()
    return ret

@rest('GET', '/apic/delete/ap')
def delete_ap(request, tn_name, ap_name):
    lock.on()
    try:
        controller.Tenant(tn_name).AppProfile(ap_name).delete()
    except Exception as e:
        ret = {'result' : False, 'error' : str(e)}
    else:
        ret = {'result' : True}
    lock.off()
    return ret

@rest('GET', '/apic/create/epg')
def create_epg(request, tn_name, ap_name, epg_name):
    lock.on()
    try:
        ap = controller.Tenant(tn_name).AppProfile(ap_name)
        epg = ap.EPG.create(name=epg_name)
    except Exception as e:
        ret = {'result' : None, 'error' : str(e)}
    else:
        ret = {'result' : epg}
    lock.off()
    return ret

@rest('GET', '/apic/delete/epg')
def delete_epg(request, tn_name, ap_name, epg_name):
    lock.on()
    try:
        controller.Tenant(tn_name).AppProfile(ap_name).EPG(epg_name).delete()
    except Exception as e:
        ret = {'result' : False, 'error' : str(e)}
    else:
        ret = {'result' : True}
    lock.off()
    return ret
