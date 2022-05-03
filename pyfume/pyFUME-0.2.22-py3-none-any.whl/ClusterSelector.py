# from .Splitter import DataSplitter
from pyfume import Clusterer
import numpy as np
import scipy.spatial

class ClusterSelector(object):
    """
        Creates a new feature selection object.
        
        Args:
            dataX: The input data.
            dataY: The output data (true label/golden standard).
            nr_clus: Number of clusters that should be identified in the data.
            variable_names: Names of the variables
            **kwargs: Additional arguments to change settings of the fuzzy model.
    """
    def __init__(self, dataX, dataY, nr_clus, variable_names, **kwargs):
        self.dataX=dataX
        self.dataY=dataY
        self.nr_clus = nr_clus
        self.variable_names = variable_names
        
    def fst_pso_cluster_structure_selection(self,max_iter=100, min_clusters=2, max_clusters=10, performance_metric='MAE', **kwargs):
        """
            Perform feature selection using the FST-PSO [1] variant of the Integer and Categorical 
            PSO (ICPSO) proposed by Strasser and colleagues [2]. ICPSO hybridizes PSO and Estimation of Distribution 
            Algorithm (EDA), which makes it possible to convert a discrete problem to the (real-valued) 
            problem of estimating the distribution vector of a probabilistic model. Each fitness 
            evaluation a random solution is generated according to the probability distribution 
            encoded by the particle. Because the implementation is a variant on FST-PSO, the optimal 
            settings for the PSO are set automatically.

            If the number of clusters is set to None, this method simultaneously choses the optimal 
            number of clusters.

            [1] Nobile, M. S., Cazzaniga, P., Besozzi, D., Colombo, R., Mauri, G., & Pasi, G. (2018). 
            Fuzzy Self-Tuning PSO: A settings-free algorithm for global optimization. Swarm and 
            evolutionary computation, 39, 70-85.
            
            [2] Strasser, S., Goodman, R., Sheppard, J., & Butcher, S. (2016). A new discrete 
            particle swarm optimization algorithm. In Proceedings of the Genetic and Evolutionary 
            Computation Conference 2016 (pp. 53-60). 
            
            Args:
                max_iter: The maximum number of iterations used in the PSO (default = 10).
                min_clusters: The minimum number of clusters to be identified in the data set (only 
                when nr_clusters = None)
                max_clusters: The maximum number of clusters to be identified in the data set (only 
                when nr_clusters = None)
                performance_metric: The performance metric on which each solution is evaluated (default
                Mean Absolute Error (MAE))
                **kwargs: Additional arguments to change settings of the fuzzy model.
                
            Returns:
                Tuple containing (selected_features, selected_feature_names, optimal_number_clusters)
                    - selected_features: The indices of the selected features.
                    - selected_feature_names: The names of the selected features.
                    - optimal_number_clusters: If initially nr_clusters = None, this argument encodes the optimal number of clusters in the data set. If nr_clusters is not None, the optimal_number_clusters is set to nr_clusters.

        """
        
        from fstpso import FuzzyPSO


        FP = FuzzyPSO()
        
        # Create the search space for feature selection with number of dimensions D
        D = np.size(self.dataX,1)
        
        s=list([[True, False]]*D)
        
        # Add dimension for cluster number selection
        if self.nr_clus == None:
            s.append(list(range(min_clusters,max_clusters+1)))
        
        # Set search space
        FP.set_search_space_discrete(s)
        
        # Set the fitness function
        args={'x_train': self.dataX, 'y_train': self.dataY, 'verbose':self.verbose}
        FP.set_fitness(self._function, arguments=args)
        
        # solve problem with FST-PSO
        _, best_performance, best_solution = FP.solve_with_fstpso(max_iter=max_iter)
        
        if self.nr_clus == None:
            selected_features=best_solution[:-1]
        else:
           selected_features=best_solution 
    
        
        # Show best solution with fitness value
        varnams=[i for indx,i in enumerate(self.variable_names) if selected_features[indx]]
        print('The following features have been selected:', varnams, 'with a', self.performance_metric, 'of', round(best_performance,2))
        
        if self.nr_clus == None:
            optimal_number_clusters=best_solution[-1]
        else:
            optimal_number_clusters = self.nr_clus
            
            
        return selected_features, varnams, optimal_number_clusters

#    def fun(self, particle):
#        return sum(particle)
    
    def _function(self, particle, arguments, verbose=True, **kwargs):
        from itertools import compress 
        if self.nr_clus == None:
            A = arguments['x_train'][:,particle[:-1]]
            varnams=list(compress(self.variable_names, particle[:-1]))
            nr_clus=particle[-1]
        else:
            A = arguments['x_train'][:,particle[:]]
            varnams=list(compress(self.variable_names, particle[:]))
            nr_clus=self.nr_clus
        
        if A.shape[1]==0: ## If no features are selected, return a infinite high error
            error=np.inf
        else:
            error=self._evaluate_cluster_structure(x_data=A, y_data=arguments['y_train'], nr_clus=nr_clus, var_names=varnams, model_order=self.model_order, performance_metric=self.performance_metric, **kwargs)
            
        if verbose: print(" * Fitness: %.3f" % error)
        return error

        
    def _evaluate_cluster_structure(self, x_data, y_data, nr_clus, **kwargs):
        # Check settings and complete with default settings when needed
        if 'cluster_method' not in kwargs.keys(): kwargs['cluster_method'] = 'fcm'        
        if kwargs['cluster_method'] == 'fcm':
            if 'fcm_m' not in kwargs.keys(): kwargs['fcm_m'] = 2
            if 'fcm_max_iter' not in kwargs.keys(): kwargs['fcm_maxiter'] = 1000
            if 'fcm_error' not in kwargs.keys(): kwargs['fcm_error'] = 0.005
        elif kwargs['cluster_method'] == 'fstpso':
            if 'fstpso_n_particles' not in kwargs.keys(): kwargs['fstpso_n_particles'] = None
            if 'fstpso_max_iter' not in kwargs.keys(): kwargs['fstpso_max_iter'] = 100
            if 'fstpso_path_fit_dump' not in kwargs.keys(): kwargs['fstpso_path_fit_dump'] = None
            if 'fstpso_path_sol_dump' not in kwargs.keys(): kwargs['fstpso_path_sol_dump'] = None
                
        data = np.concatenate((x_data, y_data), axis=1)

        cl = Clusterer(data=data, nr_clus=nr_clus)               
            
        if kwargs['cluster_method'] == 'fcm':
            cluster_centers, partition_matrix, _ = cl.cluster(cluster_method='fcm', fcm_m=kwargs['fcm_m'], 
                fcm_maxiter=kwargs['fcm_maxiter'], fcm_error=kwargs['fcm_error'])
        elif kwargs['cluster_method'] == 'fstpso':
            cluster_centers, partition_matrix, _ = cl.cluster(cluster_method='fstpso', 
                fstpso_n_particles=kwargs['fstpso_n_particles'], fstpso_max_iter=kwargs['fstpso_max_iter'],
                fstpso_path_fit_dump=kwargs['fstpso_path_fit_dump'], fstpso_path_sol_dump=kwargs['fstpso_path_sol_dump'])
        else:
            print('The requested clustering method is not (yet) implemented')
            
        xb = self._xiebeni(data = data, centers = cluster_centers, um = partition_matrix, m=kwargs['fcm_m'])
            
        return xb

    def _xiebeni(data, centers, um, m=2):
    	n = data.shape[0]
    
    	dist = scipy.spatial.distance.cdist(data, centers, metric='sqeuclidean')
    	um_power = np.power(um,m)
    	numerator = np.sum(np.multiply(um_power,dist))
    
    	v2 = self._pairwise_squared_distances(centers,centers)
    	v2[v2 == 0.0] = np.inf
    
    	return numerator/(n*np.min(v2))
    
    def _pairwise_squared_distances(A, B):
        return scipy.spatial.distance.cdist(A, B)**2