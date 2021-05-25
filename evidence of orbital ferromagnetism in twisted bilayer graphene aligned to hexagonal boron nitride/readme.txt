This archive contains the data and Python code generating figures for:

Evidence of orbital ferromagnetism in twistedbilayer graphene aligned to hexagonal boronnitride
Authors: Aaron L. Sharpe, Eli J. Fox, Arthur W. Barnard, Joe Finney, Kenji Watanabe, 
			Takashi Taniguchi, M. A. Kastner, David Goldhaber-Gordon
https://arxiv.org/abs/2102.04039

Contents of the archive:

	tbg_rot_figures.ipynb
		- Jupyter notebook loading data and generating figures. The notebook has been 
			tested with Python version 3.8.5

	tbg_rot_figures.pdf
		- PDF of tbg_rot_figures.ipynb
	
	/data
		- All data used to generate figures for the manuscript, stored as JSON objects. 
			Refer to the notebook for figure captions describing the data. Files and 
			associated data are as follows:
			
			fig1.json -- Data for Fig. 1
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				dn_B: applied magnetic field in T for the downward sweep
				dn_ryx: R_yx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_ryx: R_yx in kOhm for the upward sweep of B
			
			
			fig2.json -- Data for Fig. 2
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				dn_B: applied magnetic field in T for the downward sweep
				dn_ryx: R_yx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_ryx: R_yx in kOhm for the upward sweep of B

			fig3.json -- Data for Fig. 3
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				dn_B: applied magnetic field in T for the downward sweep
				dn_ryx: R_yx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_ryx: R_yx in kOhm for the upward sweep of B
			
			figs2.json -- Data for Fig. S2
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				dn_B: applied magnetic field in T for the downward sweep
				dn_rxx: R_xx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_ryxx: R_xx in kOhm for the upward sweep of B

			figs3.json -- Data for Fig. S3
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				dn_B: applied magnetic field in T for the downward sweep
				dn_rxx: R_xx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_ryxx: R_xx in kOhm for the upward sweep of B

			figs4.json -- Data for Fig. S4
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				dn_B: applied magnetic field in T for the downward sweep
				dn_rxx: R_xx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_rxx: R_xx in kOhm for the upward sweep of B

			figs5a.json -- Data for Fig. S5a
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				B_asym: applied magnetic field in T for the symmetrized curve for between -8 T and +8 T
				ryx_asym: R_yx in kOhm for the symmetrized curve for between -8 T and +8 T
				B_asym_hi: applied magnetic field in T for the symmetrized curve for above +8 T
				ryx_asym_hi: R_yx in kOhm  for the symmetrized curve for above +8 T
				B_asym_lo:  applied magnetic field in T for the symmetrized curve for below -8 T
				ryx_asym_lo: R_yx in kOhm  for the symmetrized curve for above +8 T

			figs5b.json -- Data for Fig. S5b
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				B_asym: applied magnetic field in T for the symmetrized curve
				ryx_asym: R_yx in kOhm for the symmetrized curve

			figs6.json -- Data for Fig. S6
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				dn_B: applied magnetic field in T for the downward sweep
				dn_rxx: R_xx in kOhm for the downward sweep of B
				dn_ryx: R_yx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_rxx: R_xx in kOhm for the upward sweep of B
				up_ryx: R_yx in kOhm for the upward sweep of B

			figs7.json -- Data for Fig. S7
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				dn_B: applied magnetic field in T for the downward sweep
				dn_rxx: R_xx in kOhm for the downward sweep of B
				up_B: applied magnetic field in T for the upward sweep
				up_ryxx: R_xx in kOhm for the upward sweep of B


			figs8.json -- Data for Fig. S8
				thetas_deg: tilt angle of each sweep in degrees
				thetas: tilt angle of each sweep in radians
				labels: string label of each tilt angle
				nu: fractional density n/n_s
				rxx: R_xx in kOhm for each sweep of n/n_s at different value of in plane magnetic field