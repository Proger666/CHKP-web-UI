# -*- coding: utf-8 -*-
### required - do no delete



def user(): return dict(form=auth())


def download(): return response.download(request, db)


def call(): return service()


### end requires
@auth.requires_permission('read')
# Default USER - CHKP : P@ssw0rd
def index():
    return dict()


def error():
    return dict()


def req_priv():
    return locals()

