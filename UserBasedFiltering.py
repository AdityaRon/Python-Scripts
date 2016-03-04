# -*- coding: utf-8 -*-
"""
Mining Assignment 1
"""

import math

#################################################
# recommender class does user-based filtering and recommends items 
class UserBasedFilteringRecommender:
    
    # class variables:    
    # none
    
    ##################################
    # class instantiation method - initializes instance variables
    #
    # usersItemRatings:
    # users item ratings data is in the form of a nested dictionary:
    # at the top level, we have User Names as keys, and their Item Ratings as values;
    # and Item Ratings are themselves dictionaries with Item Names as keys, and Ratings as values
    # Example: 
    #     {"Angelica":{"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
    #      "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}}
    #
    # metric:
    # metric is in the form of a string. it can be any of the following:
    # "minkowski", "cosine", "pearson"
    #     recall that manhattan = minkowski with r=1, and euclidean = minkowski with r=2
    # defaults to "pearson"
    #
    # r:
    # minkowski parameter
    # set to r for minkowski, and ignored for cosine and pearson
    #
    # k:
    # the number of nearest neighbors
    # defaults to 1
    #
    def __init__(self, usersItemRatings, metric='pearson', r=1, k=1):
        
        # set self.usersItemRatings
        self.usersItemRatings = usersItemRatings

        # set self.metric and self.similarityFn
        if metric.lower() == 'minkowski':
            self.metric = metric
            self.similarityFn = self.minkowskiFn
        elif metric.lower() == 'cosine':
            self.metric = metric
            self.similarityFn = self.cosineFn
        elif metric.lower() == 'pearson':
            self.metric = metric
            self.similarityFn = self.pearsonFn
        else:
            print ("    (DEBUG - metric not in (minkowski, cosine, pearson) - defaulting to pearson)")
            self.metric = 'pearson'
            self.similarityFn = self.pearsonFn
        
        # set self.r
        if (self.metric == 'minkowski'and r > 0):
            self.r = r
        elif (self.metric == 'minkowski'and r <= 0):
            print ("    (DEBUG - invalid value of r for minkowski (must be > 0) - defaulting to 1)")
            self.r = 1
            
        # set self.k
        if k > 0:   
            self.k = k
        else:
            print ("    (DEBUG - invalid value of k (must be > 0) - defaulting to 1)")
            self.k = 1
            
    
    #################################################
    # minkowski distance (dis)similarity - most general distance-based (dis)simialrity measure
    # notation: if UserX is Angelica and UserY is Bill, then:
    # userXItemRatings = {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}
    # userYItemRatings = {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}
    def minkowskiFn(self, userXItemRatings, userYItemRatings):
        
        distance = 0
        commonRatings = False 
        
        for item in userXItemRatings:
            # inlcude item rating in distance only if it exists for both users
            if item in userYItemRatings:
                distance += pow(abs(userXItemRatings[item] - userYItemRatings[item]), self.r)
                commonRatings = True
                
        if commonRatings:
            return round(pow(distance,1/self.r), 2)
        else:
            # no ratings in common
            return -2

    #################################################
    # cosince similarity
    # notation: if UserX is Angelica and UserY is Bill, then:
    # userXItemRatings = {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}
    # userYItemRatings = {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}
    def cosineFn(self, userXItemRatings, userYItemRatings):
        
        sum_xy = 0
        sum_x2 = 0
        sum_y2 = 0
        
        for item in userXItemRatings:
            if item in userYItemRatings:
                x = userXItemRatings[item]
                y = userYItemRatings[item]
                sum_xy += x * y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        
        denominator = math.sqrt(sum_x2) * math.sqrt(sum_y2)
        if denominator == 0:
            return -2
        else:
            return round(sum_xy / denominator, 3)

    #################################################
    # pearson correlation similarity
    # notation: if UserX is Angelica and UserY is Bill, then:
    # userXItemRatings = {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}
    # userYItemRatings = {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}
    def pearsonFn(self, userXItemRatings, userYItemRatings):
        
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        
        for item in userXItemRatings:
            if item in userYItemRatings:
                n += 1
                x = userXItemRatings[item]
                y = userYItemRatings[item]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
       
        if n == 0:
            return -2
        
        denominator = math.sqrt(sum_x2 - pow(sum_x, 2) / n) * math.sqrt(sum_y2 - pow(sum_y, 2) / n)
        if denominator == 0:
            return -2
        else:
            return round((sum_xy - (sum_x * sum_y) / n) / denominator, 2)
            

    #################################################
    # make recommendations for userX from the most similar k nearest neigibors (NNs)
    def recommendKNN(self, userX):
        
        # YOUR CODE HERE
        
        # for given userX, get the sorted list of users - by most similar to least similar        
        
        # calcualte the weighted average item recommendations for userX from userX's k NNs
        
        # return sorted list of recommendations (sorted highest to lowest ratings)
        
        self.userX = userX
        users =[]
        similaritySum=0
        rankings=[]
        if self.userX in self.usersItemRatings.keys():
            for other in self.usersItemRatings:
                # don't compare to self
                if other != self.userX: 
                    if self.metric == 'pearson':     
                        sim=self.pearsonFn(self.usersItemRatings[self.userX],self.usersItemRatings[other])  
                        sim = (sim + 1)/2
                        users.append((sim,other))
                    else:
                        sim=self.similarityFn(self.usersItemRatings[self.userX],self.usersItemRatings[other]) 
                        users.append((sim, other)) 
            if (self.metric == "cosine") or (self.metric == "pearson"):
                #For Cosine and Pearson the Similiarty measure of the greatest value will be nearest neighbour
                users.sort(reverse = True)
            else:
                #For Minkowski the similarity measure(distance) should be small
                users.sort(reverse = False)
                #Sum of all the similarities
            if (self.metric == "pearson"):    
                for i in range(self.k):
                    similaritySum += users[i][0]
                    #Calculating the Weighted averages 
                for i in range(self.k):
                    for item in self.usersItemRatings[users[i][1]]:
                        if item not in self.usersItemRatings[self.userX] or self.usersItemRatings[self.userX][item]==0:
                            c = (item, self.usersItemRatings[users[i][1]][item]*(users[i][0]/similaritySum)) 
                            rankings.append(c)
                #adding the list of tuples based on the key values.
                recommendations={}
                for item in rankings:
                    recommendations.setdefault(item[0],0)
                    recommendations[item[0]] += item[1]
                for item in recommendations:
                    recommendations[item] = round(recommendations[item],2)
                return sorted(recommendations.items(), key=lambda recommendations:recommendations[1], reverse=True)
            elif self.k > 1:
                print("K cannot be greater than 1 for Minkowski and Cosine Measures")
                self.k = 1
                print("Defaulting the K value to 1 to calculate similarity measure and recommendations")
                for i in range(1):
                    for item in self.usersItemRatings[users[i][1]]:
                        if item not in self.usersItemRatings[self.userX] or self.usersItemRatings[self.userX][item]==0:
                            c = (item, self.usersItemRatings[users[i][1]][item]) 
                            rankings.append(c)
                recommendations={}
                for item in rankings:
                    recommendations.setdefault(item[0],0)
                    recommendations[item[0]] += item[1]
                return sorted(recommendations.items(), key=lambda recommendations:recommendations[1], reverse=True)
            else:
                for i in range(1):
                    for item in self.usersItemRatings[users[i][1]]:
                        if item not in self.usersItemRatings[self.userX] or self.usersItemRatings[self.userX][item]==0:
                            c = (item, self.usersItemRatings[users[i][1]][item]) 
                            rankings.append(c)
                recommendations={}
                for item in rankings:
                    recommendations.setdefault(item[0],0)
                    recommendations[item[0]] += item[1]
                print (recommendations)
                print (recommendations.items[1])
                return sorted(recommendations.items(), key=lambda recommendations:recommendations[1], reverse=True)                 
        else:
            print("User entered not found in the data\nPlease enter the correct user")