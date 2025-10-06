from agents.idea_agent import IdeaAgent
from agents.market_agent import MarketAgent
from agents.financial_agent import FinancialAgent
from agents.pitch_agent import PitchAgent

def startup_pitch_pipeline(idea: str) -> str:
    print('Starting Start-up Pitch Analysis')

    idea_agent= IdeaAgent()
    market_agent= MarketAgent()
    financial_agent= FinancialAgent()
    pitch_agent= PitchAgent()

    idea_summary= idea_agent.analyze_idea(idea)
    print("Idea Analyzed")

    market= market_agent.market_research(idea)
    print("Market Research Complete")

    financials= financial_agent.analyze_financials(idea)
    print("Financial Done")

    pitch= pitch_agent.write_pitch(idea_summary, market, financials)
    print("Pitch Generated")

    return {
        "idea_summary": idea_summary,
        "market": market,
        "financials": financials,
        "pitch": pitch
    }
