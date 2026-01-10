
# Amazon Deforestation, Forest Fires, and CO₂ Emissions in Brazil

<img src="project\\pictures\\Project_Image.webp" width="800" height="466">

## Project Objective

How does **deforestation in the Amazon** correlate with **forest fires** and **CO₂ emissions** in Brazil? This project investigates the intricate relationship between human activity, natural events, and climate impact in one of the world’s most important ecosystems.

---

## Description

The **Amazon rainforest**, often called the "lungs of the planet," plays a critical role in regulating global carbon levels. However, widespread deforestation and increasing forest fires threaten its ecosystem, contributing significantly to **CO₂ emissions**.  

This project explores these interactions using **statistical analysis, data visualization, and correlation studies**, providing both **interactive and static insights** into how deforestation drives environmental changes in Brazil.

---

## Data Sources

### Datasource 1: Deforestation in the Amazon
- **Metadata:** [Kaggle Dataset](https://www.kaggle.com/datasets/mbogernetto/brazilian-amazon-rainforest-degradation)  
- **Data URL:** [Download CSV](https://www.kaggle.com/api/v1/datasets/download/mbogernetto/brazilian-amazon-rainforest-degradation)  
- **Type:** CSV  

Deforested area (km²) by state and year from 2004–2019. Collected via **satellite imagery** (PRODES Program) to track **primary forest loss**.  

### Datasource 2: Fires in the Amazon
- **Metadata:** [JRC GWIS](https://gwis.jrc.ec.europa.eu/apps/country.profile/charts/ba)  
- **Data URL:** [Download CSV](https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/MCD64A1_burned_area_full_dataset_2002-2023.zip)  
- **Type:** Zipped CSV  

Monthly **burned area** (ha) from 2002–2023, classified by land cover. Extracted **Amazon states in Brazil** to correlate fires with deforestation.

### Datasource 3: CO₂ Emissions
- **Metadata:** [JRC GWIS](https://gwis.jrc.ec.europa.eu/apps/country.profile/charts/emi)  
- **Data URL:** [Download CSV](https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/emission_gfed_full_2002_2023.zip)  
- **Type:** Zipped CSV  

Monthly **CO₂ emissions** (tons) from 2002–2023 for Brazil. Used to study the **climate impact** of deforestation and fires.

---

##  Work Packages

1. Define Problem Statement & Objectives [#1]  
2. Identify & Collect Data [#2]  
3. Data Loading, Cleaning & Preprocessing [#3]  
4. Automate Data Pipeline (ETL) [#4]  
5. Testing & Validation [#5]  
6. Create Visualizations [#6]  
7. Correlation Analysis [#7]  
8. Analysis Report [#8]  
9. Presentation [#9]  
10. Record Video Presentation [#10]  

[#1]: https://github.com/azamKhattak24/MADE24/issues/1#issue-2650388072  
[#2]: https://github.com/azamKhattak24/MADE24/issues/2#issue-2650389806  
[#3]: https://github.com/azamKhattak24/MADE24/issues/3#issue-2658580619  
[#4]: https://github.com/azamKhattak24/MADE24/issues/4#issue-2658593120  
[#5]: https://github.com/azamKhattak24/MADE24/issues/5  
[#6]: https://github.com/azamKhattak24/MADE24/issues/6  
[#7]: https://github.com/azamKhattak24/MADE24/issues/7  
[#8]: https://github.com/azamKhattak24/MADE24/issues/8  
[#9]: https://github.com/azamKhattak24/MADE24/issues/9  
[#10]: https://github.com/azamKhattak24/MADE24/issues/10  

---

## Methodology & Analysis

### 1️⃣ Data Preparation
- Imported **CSV datasets** and connected to a **SQLite database**.  
- Cleaned column names, standardized **state names**, and filtered for **2004–2019**.  
- Aggregated fire data by **year and month**, preparing for correlation analysis.

### 2️⃣ Visualization
- **Line & bar charts**: Track deforestation trends per state and per year.  
- **Choropleth maps**: Visualize total deforested area by state.  
- **Fire trends**: Show yearly fire spots and burned areas using **Matplotlib** and **Plotly**.  
- **CO₂ emissions plots**: Analyze trends over time.

### 3️⃣ Correlation Analysis
- Merged **deforestation, fires, and emissions datasets**.  
- Calculated **Pearson correlation coefficients**:  
  - Deforested Area ↔ Forest Burned Area  
  - Deforested Area ↔ CO₂ Emissions  
  - Forest Burned Area ↔ CO₂ Emissions  
- Plotted **scatter plots with regression lines**, heatmaps, and annotated correlation strength.

---

## Key Findings
- **Deforestation and fires are positively correlated**, showing that human activity directly influences forest degradation.  
- **CO₂ emissions increase with both deforestation and fires**, highlighting the Amazon's crucial role in climate regulation.  
- Moderate correlations suggest that **other environmental factors** (El Niño, precipitation, land management) also play roles.

---

## Impact
This analysis provides **actionable insights** for environmental scientists, policymakers, and conservationists:  
- Identifying **high-risk states** for deforestation and fires.  
- Estimating the **climate impact** of forest loss.  
- Supporting data-driven decisions for **Amazon protection** and **climate mitigation**.  

By combining **visualization, statistics, and geospatial analysis**, this project demonstrates the critical links between human activity, forest degradation, and global climate change.

