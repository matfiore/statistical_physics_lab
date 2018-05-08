import copy
import random

def surface_stats(surface):
    surf_copy = copy.deepcopy(surface) # defining the copy of the original surface with "=" does not create a new object with the same features, but 
                                       # creates a new object that is bound to the old one (something similat to a pointer/view)
    n_clusters=0
    height_distr = {}
    area_distr = {}
    vol_distr = {}
    #height_ls = []
    #area_ls = []
    #vol_ls = []
    pd = 0
    # A container evaluate to false if it is empty
    while surf_copy.adsorbate:
        s = random.choice(list(surf_copy.adsorbate.values()))
        height, area, volume = find_cluster(surf_copy,s)
        if volume > 1: n_clusters += 1 # I do not want to count "clusters" made of one particle only
        # dictionaries woth distr.
        height_distr[height] = height_distr.get(height, 0) + 1
        area_distr[area] = area_distr.get(area, 0) + 1
        vol_distr[volume] = vol_distr.get(volume, 0) + 1
        # rak lists
        #height_ls.append(height)
        #area_ls.append(area)
        #vol_ls.append(volume)
    return n_clusters, height_distr,area_distr,vol_distr
    #return n_clusters, height_ls,area_ls,vol_ls

def surface_counts(surface):
    surf_copy = copy.deepcopy(surface) # defining the copy of the original surface with "=" does not create a new object with the same features, but 
                                       # creates a new object that is bound to the old one (something similat to a pointer/view)
    n_clusters=0
    height_ls = []
    area_ls = []
    vol_ls = []
    pd = 0
    # A container evaluate to false if it is empty
    while surf_copy.adsorbate:
        s = random.choice(list(surf_copy.adsorbate.values()))
        height, area, volume = find_cluster(surf_copy,s)
        if volume > 1: n_clusters += 1 # I do not want to count "clusters" made of one particle only
        # rak lists
        height_ls.append(height)
        area_ls.append(area)
        vol_ls.append(volume)
    return n_clusters, height_ls, area_ls, vol_ls

def find_cluster(surface,site,height=0,area=0,volume=0):
    if site.occ > height: height = site.occ
    area += 1
    volume += site.occ # every particle is a cube
    neighbours = surface.site_neighbours(site)
    surface.remove_site(site)
    for n in neighbours: # works if n is a shallow copy/view (a pointer) of(/to) n
        if n.occ > 0: height, area, volume = find_cluster(surface,n,height,area,volume)
    return height, area, volume
    
    



