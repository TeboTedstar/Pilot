# Circular Resource Flow Dashboard - Weekly HTML Report Generator

import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# Sample data simulating resource inputs and outputs
resource_flow_data = pd.DataFrame({
    "Stage": ["Mining Site", "Processing Plant", "Community Reuse", "Recycling Facility", "Waste Landfill"],
    "Input (tons)": [1000, 850, 400, 300, 50],
    "Output (tons)": [850, 400, 300, 50, 0],
    "Circular Contribution (%)": [0, 50, 35, 10, 0]
})

reuse_breakdown = pd.DataFrame({
    "Material": ["Metal", "Plastic", "Wood", "Rubber"],
    "Reused (tons)": [200, 80, 70, 50]
})

# Charts
fig_flow = px.bar(
    resource_flow_data,
    x="Stage",
    y=["Input (tons)", "Output (tons)"],
    barmode="group",
    title="Material Input vs Output at Each Stage"
)
fig_reuse = px.pie(
    reuse_breakdown,
    names="Material",
    values="Reused (tons)",
    title="Proportion of Materials Reused"
)

# Circularity KPI
circular_percent = round((resource_flow_data["Output (tons)"].sum() / resource_flow_data["Input (tons)"].sum()) * 100, 2)

# Generate HTML report
html_report = f"""
<html>
<head>
    <title>Weekly Circular Dashboard Report</title>
</head>
<body>
    <h1>Weekly Circular Resource Flow Report</h1>
    <p><strong>Date:</strong> {datetime.today().strftime('%Y-%m-%d')}</p>
    <h2>Key Performance Indicator</h2>
    <p><strong>Overall Circular Resource Utilization:</strong> {circular_percent}%</p>
    <h2>Material Flow Chart</h2>
    {fig_flow.to_html(full_html=False, include_plotlyjs='cdn')}
    <h2>Material Reuse Chart</h2>
    {fig_reuse.to_html(full_html=False, include_plotlyjs='cdn')}
    <h2>Resource Flow Data</h2>
    {resource_flow_data.to_html(index=False)}
    <h2>Reuse Breakdown</h2>
    {reuse_breakdown.to_html(index=False)}
</body>
</html>
"""

# Save to HTML file
output_file = f"weekly_circular_dashboard_report_{datetime.today().strftime('%Y%m%d')}.html"
with open(output_file, "w") as f:
    f.write(html_report)

print(f"Weekly report generated: {output_file}")
