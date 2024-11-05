
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10934193.svg)](https://doi.org/10.5281/zenodo.10934193)

# ssembatya-etal_2025_applied_energy

**Analyzing the Relative Influences of Hydrologic Information and Dams’ Production Decisions on Electricity Price Forecasts**

Henry Ssembatya<sup>1\*</sup>, Jordan D. Kern<sup>1</sup>, Nathalie Voisin<sup>2,3</sup>, Scott Steinschneider
<sup>4</sup>, and Daniel Broman<sup>2</sup>

<sup>1 </sup> North Carolina State University, Raleigh, NC, USA   
<sup>2 </sup> Pacific Northwest National Laboratory, Richland, WA, USA  
<sup>3 </sup> University of Washington, Seattle, WA, USA  
<sup>4 </sup> Cornell University, Ithaca, NY, USA 

\* corresponding author: hssemba@ncsu.edu

## Abstract
Hydropower operators use hydrologic forecasts to better manage water releases and reservoir storage, including hydropower generation schedules.
In this paper, we examine whether short- to medium-range hydrologic forecast errors are a significant driver of errors in electricity price forecasts.
Week-to-week changes in reservoir inflows influence the supply of low marginal cost hydropower, which can, in turn, impact market prices. Using softly
coupled hydrologic, hydropower scheduling, and power systems models representing the operations of 267 dams spanning the U.S. Western Interconnection,
we quantify the importance of short- to medium-range hydrologic forecast accuracy in correctly forecasting wholesale electricity prices. As a point of
comparison, we also quantify the influence of dam operators’ own hourly production decisions on realized market prices. We find that dams’
revenue-maximizing behavior (i.e., scheduling generation to align with the periods of high forecasted prices) causes larger magnitude deviations from
price forecasts than hydrologic forecast errors. Our findings suggest that optimization of hydropower scheduling should anticipate price effects due
to the production decisions of hydropower facilities.

## Journal reference
Ssembatya, H., Kern, J. D., Voisin, N., Steinschneider, S., & Broman, D. (2025). Analyzing the Relative Influences of Hydrologic Information and 
Dams’ Production Decisions on Electricity Price Forecasts. Submitted to Applied Energy

## Code reference
Ssembatya, H., Kern, J. D., Voisin, N., Steinschneider, S., & Broman, D. (2025). Supporting code for 
Ssembatya et al. 2025 - 

## Data references
### Input data
|       Dataset                                   |               Repository Link                        |               DOI                |
|:-----------------------------------------------:|:----------------------------------------------------:|:--------------------------------:|
|   White et al., 2021 model output               | https://data.mendeley.com/datasets/v8mt9d3v6h/1      | https://doi.org/10.17632/v8mt9d3v6h.1            |
| Jones et al., 2022 IM3/HyperFACETS Thermodynamic Global Warming (TGW) simulations | https://tgw-data.msdlive.org | https://doi.org/10.57931/1885756 |
|   Burleyson et al., 2023 meteorology datasets   | https://data.msdlive.org/records/cnsy6-0y610 | https://doi.org/10.57931/1960530 |
|   ERCOT historical reported load                | https://www.ercot.com/gridinfo/load/load_hist        |                   -               |

### Output data
|       Dataset                                           |   Repository Link                            |                   DOI                             |
|:-------------------------------------------------------:|---------------------------------------------:|:-------------------------------------------------:|
|     ML models load output & GO ERCOT simulations    | https://data.msdlive.org/records/nth03-3ta28     | https://doi.org/10.57931/2331202 |

## Contributing modeling software
|  Model              | Version |         Repository Link          | DOI |
|:-------------------:|:-------:|:----------------------------------------------------------------:|:--------------------------------:|
| Ssembatya et al., 2024 Grid Operations (GO) ERCOT model version used | v1.0.0 | https://zenodo.org/records/10475965 | https://doi.org/10.5281/zenodo.10475965 | 


## Reproduce my experiment
Clone this repository to get access to the scripts used in parameretizing the Machine Learning (ML) models used to predict
residential and total load under different scenarios. Download the version of the GO ERCOT model version used in this experiment 
(https://doi.org/10.5281/zenodo.10475841). The accompanying output data contains all the output datasets from these model
runs. Run the following scripts in the workflow directory to process the raw data used in this experiment:

| Script Number | Script Name | Purpose |
| --- | --- | --- |
| 1 | `texas_ht_pred_3_mlp_github.py` | Parameterize the ML model, generate datasets (predictions) of residential load under different scenarios and the non-residential load |
| 2 | `peaking_results_peak_hourly_total.py` | Combines the residential and non-residential load to obtain the total load datasets |

Run the following scripts for the GO ERCOT model.
| Script Number | Script Name | Purpose |
| --- | --- | --- |
| 1 | `reduced_network_data_allocation_hecc.py` | Create different subfolders (using a 150 node reduced topology) each containing a scenario year of the model parameterization |
| 2 | `ERCOTDataSetup.py` | Creates the ERCOT_data.dat file under each subfolder|
| 3 | `ERCOT_simple.py` | Runs the DC OPF model as an LP |


## Reproduce my figures
Use the following scripts to reproduce figures used in this publication.

| Figure Numbers |                Script Name                              |                                  Description                                               | 
|:--------------:|:-------------------------------------------------------:|:------------------------------------------------------------------------------------------:|
|       1        |     `minmax_temp_withhistoricals_from1980_paper.py`     |      Minimum and maximum hourly annual temperature under historical and climate scenarios  |
|       3        |     `nodal_topology_with_lines_ERCOT_paper.py`     |      Reduced topology framework of the selected GO ERCOT version showing nodes and transmission lines  |
|       4        |     `pk_seas_hrly_res_results_visuals_ssp3_paper.py`     |      Season of peak hourly residential load for all future scenario simulations  |
|       5        |     `pk_seas_hrly_tot_results_visuals_ssp3_paper.py`     |      Season of peak hourly total load for all future scenario simulations  |
|       6        |     `plot_year_examples_paper.py`     |      Comparing weather and load for two selected years  |
|       7        |     `peak_totload_ssp3_paper.py`     |      Peak hourly total load for all future scenario simulations  |
|       8a        |     `lol_distribution_rcp85hotterssp3base_paper.py`     |      Nodal location of loss of load on simulation day rcp85hotterssp3_base_3rd_aug_2091  |
|       8c        |     `lol_distribution_rcp45coolerssp3stdd_paper.py`     |      Nodal location of loss of load on simulation day rcp45coolerssp3_stdd_23rd_dec_2069  |
|       8b,d        |     `ercot_temperature_maps_paper.ipynb`     |      Max and min hourly temperature distribution on selected simulation days  |
|       9        |     `lol_visuals_manuscript_SSP3_paper.py`     |      Cumulative loss of load for all scenarios  |

