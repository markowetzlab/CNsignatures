#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 macint01 <macint01@jblab-srv001>
#
# Distributed under terms of the MIT license.

import requests
headers = {'Authorization': '<insert your authorisation here'}
payload = {'cancer_type': 'OVSE', 'title': 'TCGA_CGI_genelist'}
r = requests.post('https://www.cancergenomeinterpreter.org/api/v1',
                headers=headers,verify=False,
                files={
                    'mutations': open('tcga_mutations_for_CGI.txt', 'rb')},
data=payload)
r.json()

headers = {'Authorization': '<insert your authorisation here'}
payload = {'cancer_type': 'OVSE', 'title': 'PCAWG_CGI_genelist'}
r = requests.post('https://www.cancergenomeinterpreter.org/api/v1',
                headers=headers,verify=False,
                files={
                    'mutations': open('pcawg_mutations_for_CGI.txt', 'rb')},
data=payload)
r.json()

headers = {'Authorization': '<insert your authorisation here'}
payload = {'cancer_type': 'OVSE', 'title': 'BRITROC_CGI_genelist'}
r = requests.post('https://www.cancergenomeinterpreter.org/api/v1',
                headers=headers,verify=False,
                files={
                    'mutations': open('britroc_mutations_for_CGI.txt', 'rb')},
data=payload)
r.json()

headers = {'Authorization': '<insert your authorisation here'}
payload = {'cancer_type': 'OVSE', 'title': 'CN'}
r = requests.post('https://www.cancergenomeinterpreter.org/api/v1',
                headers=headers,verify=False,
                files={
                    'mutations': open('cn_for_CGI.txt', 'rb')},
data=payload)
r.json()
