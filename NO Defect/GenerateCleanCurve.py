import numpy as npimport pandas as pdimport matplotlib.pyplot as pltimport mathclass GenerateCleanCurve:    number_of_data = 500    x_left = 0    x_right = 100    #degree_of_radom = 10        def __init__(self):        pass            def generate(self,degree_of_radom):                x = np.linspace(self.x_left,self.x_right,self.number_of_data) #在-5到5之間均勻產生200個點                        #yA ===========================================================        e = 2.414        a = 1/(1+e**(-(x-30))) - 1/(1+e**(-(x-80)))        b = 1/(1+e**(-(x-15))) - 1/(1+e**(-(x-30)))        k = 1/(1+e**(-(x-65))) - 1/(1+e**(-(x-80)))        c =  1/(1+e**(-((0.2*(x+45))-15))) - 1/(1+e**(-((0.2*(x+45))-20)))        y = a + 0.5*b  -0.5*k        y = y*400        yA = y + degree_of_radom*np.random.rand(self.number_of_data)                                #yB ===========================================================        yB = np.zeros(self.number_of_data)        for i in range(self.number_of_data):            yB[i] = (math.sin(0.2*x[i]))*10 + 170         yB = yB + degree_of_radom*np.random.rand(self.number_of_data)                                        #yC ===========================================================        yC = np.zeros(self.number_of_data)        for i in range(self.number_of_data):            yC[i] = (math.log(x[i]*10 +1)) * 50 - x[i]*0.7        yC = yC + degree_of_radom*np.random.rand(self.number_of_data)                                #yD ===========================================================        yD = np.zeros(self.number_of_data)        for i in range(self.number_of_data):            yD[i] = ((math.log((x[i]+5)*10 +1)) * 50 - x[i]*0.7) * (-1) +340        yD = yD + degree_of_radom*np.random.rand(self.number_of_data)                        #yE ===========================================================        yE =  0*x + 20        yE = yE + degree_of_radom*np.random.rand(self.number_of_data)                                        plt.scatter(x,yA)        plt.scatter(x,yB)        plt.scatter(x,yC)        plt.scatter(x,yD)        plt.scatter(x,yE)                                """plt.show()"""                        #np.savetxt('sample.csv', x, delimiter=",")        a = np.asarray([x,yA])        new_a = np.transpose(a)        #np.savetxt('sample.csv', new_a, delimiter=",", fmt='%f')                        return x,yA,yB,yC,yD,yE            if __name__ == "__main__":        """a = GenerateCleanCurve()        ans = a.generate(0) #return x,yA,yB,yC,yD,yE            print(ans)"""