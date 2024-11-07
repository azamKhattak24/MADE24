# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation between Amazon Deforesation, Forest fires and CO2 emssions in Brazil.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How does deforestation in the Amazon correlate with forest fires and CO₂ emissions in Brazil?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Amazon deforestation is an important issue due to its significant impact on global climate change and biodiversity loss. This project analyzes the correlation between deforestation, forest fires, and CO₂ emissions in Brazil, using statistical analysis and data visualization techniques. The results may provide insights into the broader environmental consequences of deforestation and inform strategies for forest conservation and climate mitigation.

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

### Datasource3: CO2 emissions in Brazil (Amazon Forest)
* Metadata URL: https://gwis.jrc.ec.europa.eu/apps/country.profile/charts/emi
* Data URL: https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/emission_gfed_full_2002_2023.zip
* Data Type: Zipped CSV

The dataset provides monthly emissions(Tons) data from 2002 to 2023, categorized by pollutant and covering all countries including Brazil.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/made-template/issues/1