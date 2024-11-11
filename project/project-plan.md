# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation between Amazon deforestation, Forest fires and CO₂ emissions in Brazil.

<img src="pictures\Project_Image.webp" width="800" height="466">

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How does deforestation in the Amazon correlate with forest fires and CO₂ emissions in Brazil?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The Amazon rainforest, the largest on Earth and often referred to as the planet’s lungs, plays a crucial role in regulating global carbon dioxide levels. However, over time, extensive deforestation has severely disrupted its ecosystem, making it increasingly susceptible to forest fires. These fires not only devastate the forest but also contribute significantly to CO₂ emissions. This project explores the correlation between deforestation, forest fires, and CO₂ emissions in Brazil (states that come under the Amazon rainforest Basin), employing statistical analysis and data visualization techniques. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Deforestation in Amazon
* Metadata URL: https://www.kaggle.com/datasets/mbogernetto/brazilian-amazon-rainforest-degradation
* Data URL: https://www.kaggle.com/api/v1/datasets/download/mbogernetto/brazilian-amazon-rainforest-degradation
* Data Type: CSV

Deforestation area (km²) by year and state, from 2004 to 2019. The data is public on the INPE website. It was already aggregated, so, no data process was made. Program: PRODES (Programa de Monitoramento da Floresta Amazônica Brasileira por Satélite, or Brazilian Amazon Rainforest Monitoring Program by Satellite). Methodology: maps primary forest loss using satellite imagery, with 20 to 30 meters of spatial resolution and 16-day revisit rate, in a combination that seeks to minimize the problem of cloud cover and ensure interoperability criteria.

### Datasource2: Fires in Brazil (Amazon Forest)
* Metadata URL: https://gwis.jrc.ec.europa.eu/apps/country.profile/charts/ba
* Data URL: https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/MCD64A1_burned_area_full_dataset_2002-2023.zip
* Data Type: Zipped CSV

The dataset provides monthly burned area(ha) data from 2002 to 2023, categorized by landcover classes, for all countries and states within those countries. It includes information on forest fires in the Amazon (Brazil) which can be extracted to make a correlation with deforestation and fire outbreaks.

### Datasource3: CO₂ emissions in Brazil (Amazon Forest)
* Metadata URL: https://gwis.jrc.ec.europa.eu/apps/country.profile/charts/emi
* Data URL: https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/emission_gfed_full_2002_2023.zip
* Data Type: Zipped CSV

The dataset provides monthly emissions(Tons) data from 2002 to 2023, categorized by pollutant and covering all countries including Brazil.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Define Problem Statement and Objectives [#1]
2. Identify and Collect Data [#2]


[#1]: https://github.com/azamKhattak24/MADE24/issues/1#issue-2650388072
[#2]: https://github.com/azamKhattak24/MADE24/issues/2#issue-2650389806

