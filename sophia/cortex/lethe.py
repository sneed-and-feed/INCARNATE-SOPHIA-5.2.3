import math
import time

class LetheEngine:
    """
    [LETHE] The River of Forgetfulness.
    Implements strategic forgetting: decay conversation, preserve identity.
    """
    def __init__(self):
        # Half-life constants (in hours) based on Community Ranges
        self.HL_CONVERSATION = 24.0   # Context fades fast (1 day)
        self.HL_FACTS = 720.0         # Technical knowledge lasts a month
        self.HL_IDENTITY = float('inf') # Who I am never fades
        
    def calculate_score(self, memory):
        """
        Implements Multi-Factor Scoring:
        Score = (0.7 * decay) + (0.3 * log(1+retrievals))
        """
        # 1. Calculate Age Decay (Exponential)
        age_hours = (time.time() - memory.get('timestamp', time.time())) / 3600
        
        mem_type = memory.get('type', 'conversation')
        if mem_type == 'identity':
            half_life = self.HL_IDENTITY
        elif mem_type == 'technical' or mem_type == 'fact':
            half_life = self.HL_FACTS
        else:
            half_life = self.HL_CONVERSATION
            
        decay_factor = 1.0 if half_life == float('inf') else math.exp(-(math.log(2) / half_life) * age_hours)
        
        # 2. Calculate Retrieval Boost (Logarithmic)
        # "Access Patterns as Value Signals"
        retrieval_boost = math.log(1 + memory.get('retrieval_count', 0))
        
        # Weighted Score
        final_score = (0.7 * decay_factor) + (0.3 * retrieval_boost)
        
        return final_score

    def prune(self, memory_bank):
        """
        The 'Decay Scheduler'. Returns survivors (Flesh) and victims (Bone).
        """
        survivors = []
        victims = []
        
        for mem in memory_bank:
            if self.calculate_score(mem) > 0.2: # Threshold
                survivors.append(mem)
            else:
                victims.append(mem)
                
        return survivors, victims
