class AutonomousAffectiveNpcBehaviorTreeEngineClient:
    def update_npc_cognitive_state(self, npc_persona_id='npc_tavern_keeper_elena', player_dialogue='Can you tell me where the forbidden dungeon entrance is hidden?'):
        return {
            'cognitive_turn_id': 'spd_npc_8812',
            'npc_id': npc_persona_id,
            'affective_state': {'fear': 0.12, 'curiosity': 0.85, 'trust': 0.64},
            'active_goal': 'ASSESS_PLAYER_INTENT_BEFORE_REVEALING_SECRET',
            'behavior_tree_node_executed': 'QUERY_EPISODIC_MEMORY_NODE',
            'dialogue_response': 'The Whispering Crypts lie past the weeping willow, but only those bearing the silver crest may enter safely.',
            'speech_audio_stream_url': 'https://assets.genpark.ai/speedrun/npc_speech_8812.mp3',
            'turn_latency_ms': 48
        }
