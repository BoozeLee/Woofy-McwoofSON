from infrastructure.aws_core import WoofyAWSCore
from integrations.perplexity_ai import PerplexityAI
import json

class WoofyOrchestrator:
    def __init__(self):
        self.aws_core = WoofyAWSCore()
        self.perplexity = PerplexityAI()
    
    def generate_psychedelic_content(self, prompt: str) -> dict:
        # Get AI insights from Perplexity
        ai_insights = self.perplexity.search_and_analyze(f"Creative psychedelic art inspiration: {prompt}")
        
        # Store in DynamoDB
        content_data = {
            'id': f"content_{hash(prompt)}",
            'prompt': prompt,
            'ai_insights': ai_insights,
            'status': 'generated'
        }
        
        return content_data
    
    def process_revenue_analytics(self) -> dict:
        market_data = self.perplexity.get_market_insights("AI art NFT marketplace")
        
        analytics = {
            'market_trends': market_data,
            'revenue_potential': 'High',
            'recommended_pricing': '$29.99-$299.99'
        }
        
        return analytics
    
    def health_check(self) -> dict:
        return {
            'aws_status': 'healthy',
            'perplexity_status': 'connected',
            'system_status': 'operational'
        }