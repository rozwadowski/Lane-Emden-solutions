import numpy as np
import matplotlib.pyplot as plt

n = [0,1,2,3,4,5,6,7,8,9]
theta0 = 1
phi0 = 0
step = 0.00001
ksi0 = 0
ksi_max = 40

theta = theta0
phi = phi0
ksi = ksi0 + step

Theta = [[],[],[],[],[],[],[],[],[],[]]
Phi = [[],[],[],[],[],[],[],[],[],[]]
Ksi = [[],[],[],[],[],[],[],[],[],[]]

for i in n:
	Theta[i].append(theta)
	Phi[i].append(phi)
	Ksi[i].append(ksi)
 
def dTheta_dKsi(phi,ksi):	
	return -phi/ksi**2

def dPhi_dKsi(theta,ksi,n):
	return theta**(n)*ksi**2

for i in n:	
	while ksi<ksi_max:
	 	if theta < 0:
			break
		dTheta = step*dTheta_dKsi(phi,ksi)
		dPhi = step*dPhi_dKsi(theta,ksi,i/2.)
		theta += dTheta
		phi += dPhi
		ksi += step
		Theta[i].append(theta)
		Phi[i].append(phi)
		Ksi[i].append(ksi)
	print i/2., round(ksi,4), round(dTheta_dKsi(phi,ksi),4), round(ksi/3./dTheta_dKsi(phi,ksi),4), round(1./(4*np.pi*(i/2.+1))/dTheta_dKsi(phi,ksi)**2,4)
	theta = theta0
	phi = phi0
	ksi = ksi0 + step
 
f1 = plt.figure()
plt.grid()
plt.ylim(-0.1,1.1)
for i in n:
	plt.plot(Ksi[i],Theta[i], label = i/2.)
plt.legend(loc='best')
plt.xlabel('ksi')
plt.ylabel('theta')
plt.title('Rozwiazanie rownania Lane-Emdena')
f1.savefig('EnergiaOsoemka.png')
