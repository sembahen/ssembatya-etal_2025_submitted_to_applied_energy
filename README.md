
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10934193.svg)](https://doi.org/10.5281/zenodo.10934193)

# ssembatya-etal_2025_TBD

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
Ssembatya et al. 2025

## Data references
### Input data
|       Dataset                                   |               Repository Link                                   |               DOI                        |
|:-----------------------------------------------:|:---------------------------------------------------------------:|:----------------------------------------:|
|   STARFIT Output files                          | xx                                                              | xx                                       |
|   FIScH Output                                  | https://github.com/HydroWIRES-PNNL/broman-etal_2025_wrr         | xx                                       |


### Output data
|       Dataset                                              |   Repository Link                              |                   DOI                             |
|:----------------------------------------------------------:|-----------------------------------------------:|:-------------------------------------------------:|
|     DCOPF1 (Perfect, Persistence) LMPs and generation      | https://zenodo.org/uploads/14041719            | https://doi.org/10.5281/zenodo.14041719           |
|     DCOPF2 (Perfect, Persistence) LMPs and generation      | https://zenodo.org/uploads/14041719            | https://doi.org/10.5281/zenodo.14041719           |

## Contributing modeling software
|  Model   | Version |         Repository Link                            | DOI |
|:--------:|:-------:|:--------------------------------------------------:|:---:|
| FIScH      |  v0.4.0  | https://github.com/HydroWIRES-PNNL/fisch        | NA  |
| GO-WEST    |  XX      | https://github.com/romulus97/IM3-GO-WEST        | XX  |
| starfit    | v0.1.0   | https://github.com/IMMM-SFA/starfit             | NA  |


## Reproduce my experiment
Clone this repository to get access to the scripts used in the experiment. Run the 4 instances of the DCOPF model ("DCOPF1 Perfect", "DCOPF1 Persistence", "DCOPF2 Perfect", "DCOPF1 Persistence").
Use the results of LMPs and generation from the 4 DCOPF runs, as well as outputs from FIScH to analyze the trends in changes in price forecasts errors corresponding to changes in streamflow forecast or the DP model's (FIScH) optimal scheduling.

| Script Number | Script Name | Purpose |
| --- | --- | --- |
| 1 | `xx.py` | xx |
| 2 | `xx.py` | xx |

Run the following scripts for the GO ERCOT model.
| Script Number | Script Name | Purpose |
| --- | --- | --- |
| 1 | `xx.py` | xx |


## Reproduce my figures
Use the following scripts to reproduce figures used in this publication.

| Figure Numbers |                Script Name                              |                                  Description                                               | 
|:--------------:|:-------------------------------------------------------:|:------------------------------------------------------------------------------------------:|
|       1        |     `xx.py`     |      xx |
