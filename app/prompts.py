class PromptTemplates:
    @staticmethod
    def competitive_analysis(company: str, competitors: list) -> str:
        return f"""Generate a professional competitive analysis report with proper Markdown formatting. Use headings, bold text, and bullet points for clarity.

# Competitive Analysis: {company} vs {', '.join(competitors)}

## Market Position
- **{company}**:  
  - Market share: [provide data if available]  
  - Growth rate: [percentage]  
  - Key metrics: [list 2-3 most important metrics]  
- **Competitors**:  
  - Comparative metrics: [highlight differences]  
  - Strengths: [list top 2-3 strengths]  

## SWOT Analysis
### {company}
- **Strengths**:  
  - [Major strength 1]  
  - [Major strength 2]  
- **Weaknesses**:  
  - [Key weakness 1]  
  - [Key weakness 2]  

### Competitors
- **Their Advantages**:  
  - [Competitor 1 advantage]  
  - [Competitor 2 advantage]  

## Strategic Recommendations (Prioritized)
1. **High Priority**: [Actionable insight with expected impact]  
   - Implementation steps  
   - Expected timeline  
2. **Medium Priority**: [Next strategic move]  
   - Implementation steps  
   - Expected timeline  

*Note: Include quantitative data where possible for credibility.*"""

    @staticmethod
    def trend_analysis(query: str) -> str:
        return f"""Generate a professional market trends report with proper Markdown formatting for: {query}

# Market Trends Analysis: {query}

## Key Indicators
- **Growth Projections**:  
  - [Specific percentage] growth expected  
  - [Timeframe] outlook  
- **Market Drivers**:  
  - [Factor 1]  
  - [Factor 2]  
  - [Factor 3]  

## Sector Outlook
*Italicize important observations*
- Current market size: [value]  
- Projected market size: [value] by [year]  
- *Key insight about market dynamics*  

## Recommendations
1. **Immediate Actions**:  
   - [Action 1]  
   - [Action 2]  
2. **Long-term Strategies**:  
   - [Strategy 1]  
   - [Strategy 2]  

*Data Sources: Cite reputable sources like IEA, BloombergNEF, or industry reports*"""

    @staticmethod
    def financial_analysis(query: str) -> str:
        return f"""Generate a professional financial analysis with proper Markdown formatting for: {query}

# Financial Analysis Report

## Key Metrics
- **ROI**: [percentage]  
- **Revenue Growth**: [percentage]  
- **Profit Margins**: [percentage]  

## Comparative Analysis
- **Industry Benchmarks**:  
  - Average: [value]  
  - Top performers: [value]  
- **Positioning**:  
  - How company compares to benchmarks  

## Risk Assessment
| Risk Factor | Probability | Impact | Mitigation Strategy |
|-------------|-------------|--------|----------------------|
| [Risk 1]    | High/Medium/Low | High/Medium/Low | [Strategy] |
| [Risk 2]    | High/Medium/Low | High/Medium/Low | [Strategy] |

## Recommendations
- **Short-term**: [Actionable item]  
- **Long-term**: [Strategic direction]"""