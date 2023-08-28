with open('./A1.dag', 'w') as f:  #A4.dag for station 4 
	for k in range(1,6): #Configs (6 - 1 = 5 for A1)
		for i in range(0,40): ##Number of simulation runs
			f.write('JOB ARA_S1_C'+str(k)+'_Sim'+str(i)+' ARA_job.sub\n')
			f.write('VARS ARA_S1_C'+str(k)+'_Sim'+str(i)+' st="1" config="'+str(k)+'" sim_run="'+str(i)+'"\n')
			f.write('\n')
