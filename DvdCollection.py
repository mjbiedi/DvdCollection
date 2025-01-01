#!/usr/bin/python3

import os
import sys

sys.path.insert(0, '../Collection')
import Collection

sys.path.insert(0, '../Html')
import Html

sys.path.insert(0, '../DbMgmt')
import DbMgmt

###########################################################
if __name__ == '__main__':

    movies = {}
    cover_art = {}
    path = '/mnt/Data/Movies'
    Collection.get_files(movies, path, '.iso')
    Collection.get_files(cover_art, path, '.jpg')

    dvd_info = DbMgmt.db_open('./dvds.db')

    #all_dvds = DbMgmt.get_all_dvd(dvd_info)
    #print(all_dvds)
    
    count = 0
    for key in sorted(movies):
        count += 1
        jpg_file = ''
        if key in cover_art:
            jpg_file = cover_art[key]
        else:
            print(f"Missing cover art for: {movies[key]}")
        #print("[%4d] %35s : %s, %s" %(count, key, movies[key], jpg_file))
        print(Collection.get_base_name(movies[key]))

        Title = Collection.get_base_name(movies[key])
        print(Title)
        print(DbMgmt.db_get_record(dvd_info, 'dvds', 'Title', Title))
        break
    DbMgmt.db_close(dvd_info)
