# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())


def download(): return response.download(request, db)


def call(): return service()


### end requires
@auth.requires_membership('Super root')
# Default USER - chkp@wins.yes : P@ssw0rd
def index():
    return dict()


def error():
    return dict()
