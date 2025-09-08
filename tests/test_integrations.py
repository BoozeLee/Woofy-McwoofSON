import pytest
import unittest.mock as mock
from integrations.perplexity_ai import PerplexityAI
from woofy_orchestrator import WoofyOrchestrator

class TestIntegrations:
    
    @mock.patch('integrations.perplexity_ai.requests.post')
    def test_perplexity_search(self, mock_post):
        mock_post.return_value.json.return_value = {
            'choices': [{'message': {'content': 'AI insights'}}]
        }
        
        perplexity = PerplexityAI()
        result = perplexity.search_and_analyze("test query")
        
        assert 'choices' in result
        mock_post.assert_called_once()
    
    @mock.patch('infrastructure.aws_core.boto3')
    def test_orchestrator_health_check(self, mock_boto3):
        orchestrator = WoofyOrchestrator()
        health = orchestrator.health_check()
        
        assert health['system_status'] == 'operational'
        assert 'aws_status' in health
        assert 'perplexity_status' in health
    
    def test_revenue_analytics_structure(self):
        orchestrator = WoofyOrchestrator()
        
        with mock.patch.object(orchestrator.perplexity, 'get_market_insights') as mock_insights:
            mock_insights.return_value = {'trend': 'positive'}
            
            analytics = orchestrator.process_revenue_analytics()
            
            assert 'market_trends' in analytics
            assert 'revenue_potential' in analytics
            assert 'recommended_pricing' in analytics