class PromptTemplates:
    @staticmethod
    def competitive_analysis(company: str, competitors: list) -> str:
        return f"""Generate a professional competitive analysis with this structure:
        
        ## Competitive Analysis: {company} vs {', '.join(competitors)}
        
        ### Market Position
        - **{company}**: [Market share, growth rate]
        - **Competitors**: [Comparative metrics]
        
        ### Key Differentiators
        - **{company}**: [Unique advantages]
        - **Competitors**: [Their strengths]
        
        ### Strategic Recommendations
        1. [Actionable insight with priority]
        2. [Next steps]"""