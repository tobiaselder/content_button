import os, sys
import itertools

import zkill
import settings
import pycrest
import database as db

from sqlalchemy.sql.expression import or_, and_

import pdb

crest = pycrest.EVE()
crest()

def getByAttrVal(objlist, attr, val):
    return getByAttrVals(objlist, attr, [val])

def getByAttrVals(objlist, attr, vals):
    ''' Searches list of dicts for a dict with dict[attr] == val '''
    # matches = [getattr(obj, attr) in vals for obj in objlist]
    matches = filter(lambda obj: getattr(obj, attr) in vals, objlist)
    # index = matches.index(True)  # find first match, raise ValueError if not found
    return matches

def getAllItems(page):
    ''' Fetch data from all pages '''
    ret = page().items
    while hasattr(page(), 'next'):
        page = page().next()
        ret.extend(page().items)
    return ret

def get_bulk_system_data(sys_ids):
    z = zkill.get_kills(sys_ids)
    systems = getByAttrVals(crest.systems().items, 'id_str', sys_ids)
    for s in [systems[0]]:

        print s().stats
        # exit()
        # st = s().stats()
        # pdb.set_trace()
    

    # return score, explanation
    


def nearby_systems(sys_id, num_jumps):
    sys_list = set()
    sys_list.add(sys_id)

    last_sys_list = sys_list
    for i in range(num_jumps):
        new_sys_list = set()
        for s in last_sys_list:
            # pdb.set_trace()
            q = db.sdd.query(
                    db.SDDSystemConnection.toSolarSystemID,
                    db.SDDSystemConnection.fromSolarSystemID).\
                    filter(and_(
                        db.SDDSystemConnection.fromSolarSystemID==s,
                        ~db.SDDSystemConnection.toSolarSystemID.in_(last_sys_list),
                        ~db.SDDSystemConnection.toSolarSystemID.in_(sys_list),
                    )).\
                    all()
            new_sys_list.update(itertools.chain(*[(r.fromSolarSystemID, r.toSolarSystemID) for r in q]))
        last_sys_list = new_sys_list
        sys_list.update(new_sys_list)

    return sys_list

def self_test(argv):
    # print get_bulk_system_data(argv)
    print nearby_systems(int(argv[0]), 30)

if __name__ == '__main__':
    self_test(sys.argv[1:])
    exit(0)
