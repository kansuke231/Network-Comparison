#
#    
#   For graph object G
#   dynamic_robustness(G) returns inverse sum of differences geodesics after removing vertices.  See Yaron
#   Singer's 'Dynamic Measure of Robustness
#
#

def dynamic_robustness(G):
    V_set = G.vs()
    dr = 0.0
    distList = []
    
    for v in V_set:
        G_prime = G.copy()
        v_id = v["id"]
        
        v_prime = G_prime.vs.find(id=v_id)
           
        G_prime.delete_vertices(v_prime)
        
        V_prime = G_prime.vs()
        
        for u in (V_set):
            
            if u != v:
            
                distances = G.shortest_paths(u,weights=None)[0]
                sum_uw = 0.0
                for dist in distances:
                    sum_uw = sum_uw + dist
            
                v_index = v.index
                sum_uw = sum_uw - distances[v_index]
                
                
                u_id = u["id"]

                u_prime = G_prime.vs.find(id=u_id)
    
                new_sum_uw = 0.0
                new_distances = G_prime.shortest_paths(u_prime,weights=None)[0]
                for dist in new_distances:
                    new_sum_uw = new_sum_uw + dist

                difference = (1 /sum_uw) - (1 / new_sum_uw)
                distList.append(difference)
                dr = dr + difference


    dymer = 1.0 / dr
    return dymer


