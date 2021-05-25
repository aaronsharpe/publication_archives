This archive contains the data and Python code generating figures for:

Emergent ferromagnetism near three-quarters filling in twisted bilayer graphene
Authors: Aaron L. Sharpe, Eli J. Fox, Arthur W. Barnard, Joe Finney, Kenji Watanabe, 
			Takashi Taniguchi, M. A. Kastner, David Goldhaber-Gordon
https://arxiv.org/abs/1901.03520

Contents of the archive:

	TBG_ferromagnetism_figures.ipynb
		- Jupyter notebook loading data and generating figures. The notebook has been 
			tested with Python version 3.6.7 and Jupyter notebook server version 5.5.0.
	
	HTML_notebook directory
		- Contains 'TBG_ferromagnetism_figures.html' an HTML file generated from the 
			Jupyter notebook, and PNG files loaded by the HTML file
		
	scripts directory
		- Contains additional files used by the Jupyter notebook
	
	data directory
		- All data used to generate figures for the manuscript, stored as JSON objects. 
			Refer to the notebook for figure captions describing the data. Files and 
			associated data are as follows:
			
			fig1a.json -- Data for Fig. 1A
				temp: temperature in K
				Vbg: back gate voltage in V
				Vtg: top gate voltage in V
				rxxt: R_xx in ohm
				n: density in 10^12 cm^-2
				D: displacement field in V/nm
			
			fig1b.json -- Data for Fig. 1B
				rxxt: R_xx in ohm
				n: density in 10^12 cm^-2
			
			fig2a.json -- Data for Fig. 2A
				B: applied magnetic field in T
				down_rxxt: R_xx on downward sweep of B, in ohm
				down_ryxl: R_yx on downward sweep of B, in ohm
				up_rxxt: R_xx on upward sweep of B, in ohm
				up_ryxl: R_yx on upward sweep of B, in ohm
			
			fig2b.json -- Data for Fig. 2B
				nu: fractional density n/n_s
				R_AH: extracted anomalous Hall resistance in ohm
				R_AH_sigma: estimated error of extracted anomalous Hall resistance in ohm
				R_H: extracted ordinary Hall slope in ohm/T
				R_H_sigma: estimated error of extracted ordinary Hall slope in ohm/T
			
			fig2cd_figs5ab.json -- Data for Figs. 2C, 2D, S5A, S5B
				B: applied magnetic field in T
				down_temp: temperature on downward sweep of B, in K
				up_temp: temperature on upward sweep of B, in K
				down_rxxt: R_xx on downward sweep of B, in ohm
				down_ryxl: R_yx on downward sweep of B, in ohm
				up_rxxt: R_xx on upward sweep of B, in ohm
				up_ryxl: R_yx on upward sweep of B, in ohm
				Bcorctemp: extracted coercive field in T
				R_AH: extracted anomalous Hall resistance in ohm
				R_AH_sigma: estimated error of extracted anomalous Hall resistance in ohm
			
			fig3.json -- Data for Figs. 3A, 3B
				B: applied magnetic field in T
				n: density in 10^12 cm^-2
				down_r12: R_{54,12} on downward sweep of B, in ohm
				down_r1: R_{54,14} on downward sweep of B, in ohm
				up_r12: R_{54,12} on upward sweep of B, in ohm
				up_r1: R_{54,14} on upward sweep of B, in ohm
			
			fig4.json -- Data for Fig. 4
				d1_Idc: DC current on first downward sweep, in A
				d1_ryxl: R_yx on first downward sweep, in ohm
				u1_Idc: DC current on first upward sweep, in A
				u1_ryxl: R_yx on first upnward sweep, in ohm
				d2_Idc: DC current on second downward sweep, in A
				d2_ryxl: R_yx on second downward sweep, in ohm
				u2_Idc: DC current on second upward sweep, in A
				u2_ryxl: R_yx on second upward sweep, in ohm
				d3_Idc: DC current on third downward sweep, in A
				d3_ryxl: R_yx on third downward sweep, in ohm
			
			figs2.json -- Data for Fig. S2
				nu: fractional density n/n_s
				D: displacement field in V/nm
				rxxt: R_xx in ohm
			
			figs3.json -- Data for Fig. S3
				nu: fractional density n/n_s
				D: displacement field in V/nm
				rxx78: R_xx in ohm
				
			figs4.json -- Data for Fig. S4
				B: applied magnetic field in T
				down_rxxt: R_xx on downward sweep of B, in ohm
				down_ryxl: R_yx on downward sweep of B, in ohm
				up_rxxt: R_xx on upward sweep of B, in ohm
				up_ryxl: R_yx on upward sweep of B, in ohm
				
			figs5cd_figs7ab.json -- Data for Figs. S5C, S5D, S7A, S7B
				B: applied magnetic field in T
				n: density in 10^12 cm^-2
				down_temp: temperature on downward sweep of B, in K
				down_rxxt: R_xx on downward sweep of B, in ohm
				down_ryxl: R_yx on downward sweep of B, in ohm
				up_rxxt: R_xx on upward sweep of B, in ohm
				up_ryxl: R_yx on upward sweep of B, in ohm
				R_AH: extracted anomalous Hall resistance in ohm
				R_AH_sigma: estimated error of extracted anomalous Hall resistance in ohm
				R_H: extracted ordinary Hall slope in ohm/T
				R_H_sigma: estimated error of extracted ordinary Hall slope in ohm/T
				
			figs6a_old.json -- Data for Fig. S6A (old version)
				time: elapsed time at zero field in s
				ryxl: R_yx in ohm
				
			figs6b_old.json -- Data for Fig. S6B (old version)
				prior_B: applied magnetic field for sweeps before delay, in T
				prior_ryxld: R_yx for downward sweep before delay, in ohm
				prior_ryxlu: R_yx for upward sweep before delay, in ohm
				post_B: applied magnetic field for upward sweep after delay, in T
				post_ryxl: R_yx for upward sweep after delay, in ohm
				
			figs6a.json -- Data for Fig. S6A
				time: elapsed time at zero field in s
				ryxl: R_yx in ohm
				
			figs6b.json -- Data for Fig. S6B
				prior_Bd: applied magnetic field for downward sweep before delay, in T
				prior_ryxld: R_yx for downward sweep before delay, in ohm
				prior_Bu: applied magnetic field for upward sweep before delay, in T
				prior_ryxlu: R_yx for upward sweep before delay, in ohm
				post_B: applied magnetic field for upward sweep after delay, in T
				post_ryxl: R_yx for upward sweep after delay, in ohm
			
			figs8.json -- Data for Fig. S8
				D1_d_B: applied magnetic field for downward sweep at D = -0.07 V/nm, in T
				D1_d_rxxt: R_xx for downward sweep at D = -0.07 V/nm, in ohm
				D1_d_ryxl: R_yx for downward sweep at D = -0.07 V/nm, in ohm
				D1_u_B: applied magnetic field for upward sweep at D = -0.07 V/nm, in T
				D1_u_rxxt: R_xx for upward sweep at D = -0.07 V/nm, in ohm
				D1_u_ryxl: R_yx for upward sweep at D = -0.07 V/nm, in ohm
				D2_d_B: applied magnetic field for downward sweep at D = -0.56 V/nm, in T
				D2_d_rxxt: R_xx for downward sweep at D = -0.56 V/nm, in ohm
				D2_d_ryxl: R_yx for downward sweep at D = -0.56 V/nm, in ohm
				D2_u_B: applied magnetic field for upward sweep at D = -0.56 V/nm, in T
				D2_u_rxxt: R_xx for upward sweep at D = -0.56 V/nm, in ohm
				D2_u_ryxl: R_yx for upward sweep at D = -0.56 V/nm, in ohm
			
			figs9a.json -- Data for Fig. S9A
				m100mt_d2_Idc: DC current on downward sweep for B = -100 mT, in A
				m100mt_d2_ryxl: R_yx on downward sweep for B = -100 mT, in ohm
				m100mt_u2_Idc: DC current on upward sweep for B = -100 mT, in A
				m100mt_u2_ryxl: R_yx on upward sweep for B = -100 mT, in ohm
				0mt_d2_Idc: DC current on downward sweep for B = 0 mT, in A
				0mt_d2_ryxl: R_yx on downward sweep for B = 0 mT, in ohm
				0mt_u2_Idc: DC current on upward sweep for B = 0 mT, in A
				0mt_u2_ryxl: R_yx on upward sweep for B = 0 mT, in ohm
				100mt_d2_Idc: DC current on downward sweep for B = 100 mT, in A
				100mt_d2_ryxl: R_yx on downward sweep for B = 100 mT, in ohm
				100mt_u2_Idc: DC current on upward sweep for B = 100 mT, in A
				100mt_u2_ryxl: R_yx on upward sweep for B = 100 mT, in ohm
			
			figs9b.json -- Data for Fig. S9B
				tr_curr: DC current in A
				tr_rate: transition rate in Hz
				tr_err: standard error in transition rate in Hz
				tr_n: sample size
			
			figs10a.json -- Data for Fig. S10A
				B: applied magnetic field in T
				n: density in 10^12 cm^-2
				rxxt: R_xx in ohm
				ryxl: R_yx in ohm