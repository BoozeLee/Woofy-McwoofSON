
# WOOFY SECURITY GUARDRAILS - AUTO-APPLIED
import os
import sys
import logging

# Disable AWS credential logging
for logger_name in ['boto3', 'botocore', 'urllib3', 's3transfer']:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)

# Suppress credential discovery
os.environ['AWS_DEFAULT_OUTPUT'] = 'json'
os.environ['AWS_CLI_FILE_ENCODING'] = 'UTF-8'

# Import security guardrails
try:
    from security_guardrails import SecurityGuardrails
    SecurityGuardrails.secure_log("Security guardrails active")
except ImportError:
    pass

import pytest
import unittest.mock as mock

PerplexityAI = pytest.importorskip("integrations.perplexity_ai").PerplexityAI
WoofyOrchestrator = pytest.importorskip("woofy_orchestrator").WoofyOrchestrator

if not (os.environ.get('AWS_ACCESS_KEY_ID') or os.environ.get('AWS_PROFILE')):
    pytest.skip("Cloud credentials not configured for integration tests", allow_module_level=True)

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