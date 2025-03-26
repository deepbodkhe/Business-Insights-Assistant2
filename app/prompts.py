class PromptTemplates:
    @staticmethod
    def competitive_analysis(company: str, competitors: list) -> str:
        return f"""Act as a senior business strategist. Generate a comprehensive competitive analysis with this structure:
        
        ## Competitive Analysis: {company} vs {', '.join(competitors)}
        
        ### Market Position (quantitative where possible)
        - **{company}**: Market share, growth rate, key metrics
        - **Competitors**: Comparative metrics with data-driven insights
        
        ### SWOT Analysis
        - **{company}**: [Strengths, Weaknesses]
        - **Competitors**: [Their competitive advantages]
        
        ### Strategic Recommendations (prioritized)
        1. [Actionable insight with estimated impact]
        2. [Next steps with timeline]
        3. [Risk assessment for each recommendation]
        
        Format the output with clear section headers and bullet points for readability."""

    @staticmethod
    def trend_analysis(query: str) -> str:
        return f"""As a market trends expert, analyze current and future trends related to: {query}
        
        Provide:
        1. Key trend indicators (quantitative if possible)
        2. Projected market impact
        3. Recommended business adaptations
        4. Potential risks and mitigation strategies
        
        Use industry-standard forecasting methodologies in your analysis."""

    @staticmethod
    def financial_analysis(query: str) -> str:
        return f"""As a financial analyst, provide insights about: {query}
        
        Include:
        1. Relevant financial metrics and KPIs
        2. Comparative industry benchmarks
        3. ROI projections for suggested actions
        4. Risk assessment with probability/impact matrix"""

    @staticmethod
    def general_business(query: str) -> str:
        return f"""As a business consultant, provide strategic advice about: {query}
        
        Structure your response with:
        1. Key considerations
        2. Data-driven insights
        3. Actionable recommendations
        4. Implementation roadmap"""